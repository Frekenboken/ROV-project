import serial


def gps_connection(address, speed, timeout):
    try:
        serGPS = serial.Serial(address, speed, timeout=timeout)
        serGPS.flush()
        return serGPS
    except:
        return None


def arduino_connection(address, speed, timeout):
    try:
        serArduino = serial.Serial(address, speed, timeout)
        serArduino.flush()
        return serArduino
    except:
        return None
