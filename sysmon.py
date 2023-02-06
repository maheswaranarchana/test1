import psutil
import time

while True:
    cpu_percent = psutil.cpu_percent()
    virtual_memory = psutil.virtual_memory()
    disk_usage = psutil.disk_usage("/")

    print("CPU Usage: ", cpu_percent, "%")
    print("Memory Usage: ", virtual_memory.percent, "%")
    print("Disk Usage: ", disk_usage.percent, "%")
    time.sleep(5)
