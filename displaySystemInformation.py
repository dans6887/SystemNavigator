
import SystemNavigator

platform = SystemNavigator.platform
psutil = SystemNavigator.psutil
#function 5
#Get System Info
def displaySystemInformation():
    # Get basic system information
    print("System:", platform.system())
    print("Hostname:", platform.node())
    print("Release:", platform.release())
    print("Version:", platform.version())
    print("Machine:", platform.machine())
    print("Processor:", platform.processor())

    #Get CPU information
    cpu_info = platform.processor()
    cpu_count = psutil.cpu_count(logical=False)
    logical_cpu_count = psutil.cpu_count(logical=True)

    print("\nCPU Information:")
    print(f"Processor: {cpu_info}")
    print(f"Physical Cores: {cpu_count}")
    print(f"Logical Cores: {logical_cpu_count}")

    #Get memory information
    memory_info = psutil.virtual_memory()
    #memory_info_gb = int(memory_info / 1000000000)
    print("\nMemory Information:")
    #print(f"Total Memory (GB): {memory_info_gb} GB ")
    print(f"Total Memory: {memory_info.total} bytes")
    print(f"Available Memory: {memory_info.available} bytes")
    print(f"Used Memory: {memory_info.used} bytes")
    print(f"Memory Utilization: {memory_info.percent}%")

    #Get disk information
    disk_info = psutil.disk_usage('/')
    print("\nDisk Information:")    
    print(f"Total Disk Space: {disk_info.total} bytes")
    print(f"Used Disk Space: {disk_info.used} bytes")
    print(f"Free Disk Space: {disk_info.free} bytes")
    print(f"Disk Space Utilization: {disk_info.percent}%")
