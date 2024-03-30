device_connected = True
internet_speed = 25  # in Mbps

speed_check = "Slow" if internet_speed < 10 else "Fast"
site_status = "Device not connected." if not device_connected else "Accessible" if speed_check == "Fast" else "Not Accessible due to slow speed"
print(site_status)