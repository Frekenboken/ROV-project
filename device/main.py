import base64
import os
import cv2
import zmq
import serial
import time
import psutil
import numpy as np
from threading import Thread
from piservo import Servo
import RPi.GPIO as gpio
from gpiozero import CPUTemperature
from rpi_bad_power import new_under_voltage
from PID import PIDController

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind(f"tcp://*:5555")

context2 = zmq.Context()
socket2 = context2.socket(zmq.PAIR)
socket2.bind("tcp://*:5556")

# Настройки
SERIAL_PORT = "/dev/ttyUSB0"
SERIAL_BAUDRATE = 115200
SERIAL_TIMEOUT = 0.5

# PID-контроллеры
depth_pid = PIDController(0.01, 0.0001, 0.1)
depth_pid.set_limit(10, 170)
depth_pid.set_offset(90)

roll_pid = PIDController(0.01, 0.0001, 0.1)
roll_pid.set_limit(-5, 5)
roll_pid.set_offset(0)

pitch_pid = PIDController(0.01, 0.0001, 0.1)
pitch_pid.set_limit(-5, 5)
pitch_pid.set_offset(0)

# Сервоприводы
servo_pins = [19, 20, 21, 22]
motor_pins = [18, 13, 12, 25]

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

# Настройка GPIO пинов для ШИМ
for pin in servo_pins:
    gpio.setup(pin, gpio.OUT)
for pin in motor_pins:
    gpio.setup(pin, gpio.OUT)

# Создаем объекты PWM для каждого пина с частотой 50 Гц
servo_pwm_instances = [gpio.PWM(pin, 50) for pin in servo_pins]
motor_pwm_instances = [gpio.PWM(pin, 50) for pin in motor_pins]

# Запуск ШИМ сигналов с начальной шириной импульса 0%
for pwm in servo_pwm_instances:
    pwm.start(0)
for pwm in motor_pwm_instances:
    pwm.start(0)

# Инициализация камеры
cap = cv2.VideoCapture(0)

# Подключение к Arduino
ser = serial.Serial(SERIAL_PORT, SERIAL_BAUDRATE, timeout=SERIAL_TIMEOUT)
time.sleep(2)  # Ожидание стабилизации соединения7


def get_value(x, y):
    if x > 0 and y > 0:
        if abs(x) > abs(y):
            return x - y  # "Первый октант"
        else:
            return y - x  # "Второй октант"
    elif x < 0 and y > 0:
        if not (abs(x) < abs(y)):
            return 2 ** 0.5 * y  # "Четвертый октант"
    elif x < 0 and y < 0:
        if abs(x) > abs(y):
            return 0  # "Пятый октант"
        else:
            return 0  # "Шестой октант"
    elif x > 0 and y < 0:
        if abs(x) < abs(y):
            return 2 ** 0.5 * x  # "Седьмой октант"
    elif x == 0 and y < 0:
        return 0
    elif y == 0 and x < 0:
        return 0
    return (x ** 2 + y ** 2) ** 0.5


def map_value(value, from_min, from_max, to_min, to_max):
    # Проверяем, чтобы значения в исходном диапазоне не совпадали
    if from_min == from_max:
        raise ValueError("from_min и from_max не могут быть равными.")

    # Вычисляем, в какой пропорции находится value в исходном диапазоне
    from_range = from_max - from_min
    to_range = to_max - to_min
    scaled_value = (value - from_min) / from_range  # Нормализуем значение
    return to_min + (scaled_value * to_range)  # Преобразуем в новый диапазон


# Функция для установки угла для каждого сервомотора
def set_angle(pwm, angle):
    duty = (angle / 18) + 2  # Преобразуем угол в коэффициент заполнения
    pwm.ChangeDutyCycle(duty)


def read_arduino():
    if ser.in_waiting > 0:
        try:
            line = ser.readline().decode("utf-8").strip()
            data = line.split(",")

            if len(data) < 7:
                return [None] * 7  # Защита от неполных данных

            # print(f"Arduino: {line}")  # Логирование данных
            ser.reset_input_buffer()  # Очищаем входной буфер
            return data
        except Exception as e:
            print(f"Ошибка чтения с Arduino: {e}")

    return [None] * 7  # Если данных нет, возвращаем пустой список


def cam_and_data_send():
    while True:
        suc, frame = cap.read()
        if not suc:
            print("Ошибка чтения камеры!")
            break

        # Кодирование изображения в base64
        _, encoded_frame = cv2.imencode('.jpg', frame)
        image_str = base64.b64encode(encoded_frame.tobytes()).decode('utf-8')

        arduino_data = read_arduino()

        # Отправка данных
        data = {'image': image_str, 'data': {'depth': arduino_data[0],
                                             'dy': arduino_data[1],
                                             'dx': arduino_data[2],
                                             'temperature_in': arduino_data[3],
                                             'humidity_in': arduino_data[4],
                                             'pressure_in': arduino_data[5],
                                             'temperature_out': arduino_data[6],
                                             'cpu_temperature': str(psutil.sensors_temperatures()["cpu_thermal"][0][1]),
                                             'cpu_usage': str(psutil.cpu_percent()),
                                             'low_voltage': new_under_voltage().get()}}
        response = socket.recv_string()
        if response == 'c':
            print('Close connection.')
        socket.send_pyobj(data)


def control_send():
    while True:
        try:
            response = socket2.recv_pyobj()
            print(response)
            data = {'status': 'ok'}
            socket2.send_pyobj(data)

            # servos[0].write(map_value(float(response['x']), -1, 1, 0, 180))

            # depth = 100  # Заглушка (здесь нужно получать реальные данные)
            # gx = 0
            # gy = 0
            #
            # depth_speed = depth_pid.compute(depth, 120)  # 120 - пример целевого значения
            # roll_speed = roll_pid.compute(gx, 0)
            # pitch_speed = pitch_pid.compute(gy, 0)
            #
            # servos[0].write(depth_speed - roll_speed + pitch_speed)
            # servos[1].write(depth_speed + roll_speed + pitch_speed)
            # servos[2].write(depth_speed - roll_speed - pitch_speed)
            # servos[3].write(depth_speed + roll_speed - pitch_speed)

            x_value = float(response['x'])
            y_value = float(response['y'])

            set_angle(motor_pwm_instances[0], map_value(get_value(-x_value, -y_value), 0, 1, 80, 100))
            set_angle(motor_pwm_instances[1], map_value(get_value(x_value, -y_value), 0, 1, 80, 100))
            set_angle(motor_pwm_instances[2], map_value(get_value(-x_value, y_value), 0, 1, 80, 100))
            set_angle(motor_pwm_instances[3], map_value(get_value(x_value, y_value), 0, 1, 80, 100))

            s1_value = int(response['s1'])
            s2_value = int(response['s2'])
            s3_value = int(response['s3'])
            s4_value = int(response['s4'])

            set_angle(servo_pwm_instances[0], s1_value)
            set_angle(servo_pwm_instances[1], s2_value)
            set_angle(servo_pwm_instances[2], s3_value)
            set_angle(servo_pwm_instances[3], s4_value)


        except KeyboardInterrupt:
            for pwm in servo_pwm_instances:
                pwm.stop()  # Останавливаем ШИМ на всех портах
            for pwm in servo_pwm_instances:
                pwm.stop()  # Останавливаем ШИМ на всех портах
            gpio.cleanup()  # Очистка GPIO


cdt = Thread(target=cam_and_data_send)
# ct = Thread(target=control_send)
cdt.start()
# ct.start()

control_send()

print("Сервер запущен!")
