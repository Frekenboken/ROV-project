import RPi.GPIO as IO
import time

IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(19, IO.OUT)  # Подключение к пину 19 для управления серво

# Настройка ШИМ на пине 19 с частотой 50 Гц
pwm = IO.PWM(19, 50)
pwm.start(0)

# Функция для установки угла
def set_angle(angle):
    duty = (angle / 18) + 2  # Расчёт коэффициента заполнения для углов от 0 до 180 градусов
    pwm.ChangeDutyCycle(duty)  # Изменяем коэффициент заполнения
    time.sleep(0.5)  # Ожидаем завершения движения серво

try:
    while True:
        for angle in range(0, 180, 10):  # Двигаем серво от 0 до 180 градусов
            set_angle(angle)
            time.sleep(0.5)

        for angle in range(180, 0, -10):  # Двигаем серво от 180 до 0 градусов
            set_angle(angle)
            time.sleep(0.5)

except KeyboardInterrupt:
    pwm.stop()  # Останавливаем ШИМ при прерывании программы
    IO.cleanup()  # Очистка GPIO
