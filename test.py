import glob

def get_input_voltage():
    hwmon_paths = glob.glob("/sys/class/hwmon/hwmon*/in*_input")
    for path in hwmon_paths:
        try:
            with open(path, "r") as f:
                voltage = int(f.read().strip()) / 1000  # Преобразуем в вольты
                if 4.5 < voltage < 5.5:  # Фильтруем напряжение в диапазоне 5V
                    return voltage
        except (FileNotFoundError, ValueError):
            continue
    return None

voltage = get_input_voltage()
if voltage:
    print(f"Напряжение питания (USB-C): {voltage:.3f} В")
else:
    print("Не удалось получить напряжение питания")
