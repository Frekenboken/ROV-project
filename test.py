def get_voltage():
    try:
        with open("/sys/class/hwmon/hwmon0/in0_input", "r") as f:
            voltage = int(f.read().strip()) / 1000  # Значение в милливольтах, переводим в вольты
        return voltage
    except FileNotFoundError:
        print("Файл с данными о напряжении не найден. Попробуйте hwmon0 или другие индексы.")
        return None


voltage = get_voltage()
if voltage:
    print(f"Напряжение питания: {voltage:.3f} В")
