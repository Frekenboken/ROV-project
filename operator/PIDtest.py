import time
import matplotlib.pyplot as plt
class PIDController:
    def __init__(self, Kp, Ki, Kd, setpoint):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.prev_error = 0
        self.integral = 0

    def compute(self, current_value):
        error = self.setpoint - current_value
        self.integral += error
        derivative = error - self.prev_error

        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative

        self.prev_error = error

        return output

def map_range(value, in_min, in_max, out_min, out_max):
    # Преобразование диапазона
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Пример использования ПИД-регулятора
    # Задайте параметры ПИД-регулятора
Kp = 0.4
Ki = 0.02
Kd = 0.1
setpoint = 50.0  # Заданное значение, которое хотим достичь

# Создайте экземпляр ПИД-регулятора
pid_controller = PIDController(Kp, Ki, Kd, setpoint)

# Моделируем процесс управления (простой пример с температурой)
current_temperature = 1000.0

for i in range(100):
    # Получите выход ПИД-регулятора
    control_output = max(-100, min(100, pid_controller.compute(current_temperature)))

    # Моделируем процесс изменения температуры (в данном случае увеличиваем температуру на выходе нашего процесса)
    current_temperature += control_output
    # Выведите текущую температуру и управляющий сигнал
    # print(f"Current Temperature: {current_temperature:.2f}, Control Output: {control_output:.2f}")

    # time.sleep(0.1)  # Задержка для имитации времени
    plt.scatter(i, current_temperature, color='red')
    plt.scatter(i, control_output, color='blue')
    plt.scatter(i, setpoint, color='black')

plt.show()
