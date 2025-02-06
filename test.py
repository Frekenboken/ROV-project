import subprocess

def get_voltage_vcgencmd():
    result = subprocess.run(["vcgencmd", "measure_volts core"], capture_output=True, text=True)
    if result.returncode == 0:
        voltage = result.stdout.strip().split("=")[-1].replace("V", "")
        return float(voltage)
    return None

voltage = get_voltage_vcgencmd()
if voltage:
    print(f"Напряжение питания: {voltage:.3f} В")
