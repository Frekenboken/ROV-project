import subprocess


def wifi_names():
    result = subprocess.check_output(['netsh', 'wlan', 'show', 'networks'], encoding='cp1251', errors='ignore')
    networks = []
    for line in result.split('\n'):
        if 'SSID ' in line:
            ssid = line.split(':')[1].strip()
            if ssid:  # Добавляем только непустые SSID
                networks.append(ssid)
    return networks

print(o())