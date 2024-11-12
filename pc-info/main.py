import psutil

# Get the CPU information
cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
cpu_freq = psutil.cpu_freq(percpu=True)
print("CPU Usage per core: ")
for i, (percent, freq) in enumerate(zip(cpu_percent, cpu_freq), start=1):
  print(f"Core {i}: {percent}% at {freq.current}Mhz")

# Get the memory information
virtual_memory = psutil.virtual_memory()
print("\nVirtual Memory: ")
print(f"Total: {virtual_memory.total/(1024 ** 3):.2f} GB")
print(f"Used: {virtual_memory.used/(1024 ** 3):.2f} GB")
print(f"Available: {virtual_memory.available/(1024 ** 3):.2f} GB")

# Get the network information
network = psutil.net_io_counters()
print("\nNetwork Information: ")
print(f"Bytes Sent: {network.bytes_sent}")
print(f"Bytes Received: {network.bytes_recv}")

# Get the temperature information
try:
  temperatures = psutil.sensors_temperatures()
  if temperatures:
    print("\nTemperatures:")
    for name, entries in temperatures.items():
      for entry in entries:
        print(f"{name}: {entry.current}°C")
  else:
    print("\nNo temperature information available.")
except AttributeError:
  print("\nNo temperature information available.")

# Get the battery information
battery = psutil.sensors_battery()
if battery:
  plugged = "Plugged in" if battery.power_plugged else "Not plugged in"
  print(f"\nBattery Status: {plugged}, {battery.percent}%")
else:
  print("\nNo battery information available.")

# Get the disk information
disk = psutil.disk_usage("/")
print("\nDisk Information: ")
print(f"Total Disk Space: {disk.total/(1024 ** 3):.2f} GB")
print(f"Used Disk Space: {disk.used/(1024 ** 3):.2f} GB")
print(f"Free Disk Space: {disk.free/(1024 ** 3):.2f} GB")