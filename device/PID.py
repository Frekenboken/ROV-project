class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.prev_error = 0
        self.integral = 0

        self.min_output = 0
        self.max_output = 180
        self.offset = 0

    def set_limit(self, min_out, max_out):
        self.min_output = min_out
        self.max_output = max_out

    def set_offset(self, value):
        self.offset = value

    def compute(self, current_value, target_value):
        error = target_value - current_value
        self.integral += error
        derivative = error - self.prev_error

        raw_output = self.kp * error + self.ki * self.integral + self.kd * derivative

        self.prev_error = error

        output = max(min(raw_output + self.offset, self.max_output), self.min_output)

        return output
