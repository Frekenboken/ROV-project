from rpi_bad_power import new_under_voltage

under_voltage = new_under_voltage()
if under_voltage is None:
    print("System not supported.")
elif under_voltage.get():
    print("Under voltage detected.")
else:
    print("Voltage is normal.")