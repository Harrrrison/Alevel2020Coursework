import platform
import psutil
from datetime import datetime
import GPUtil
from tabulate import tabulate


class data_grabbing ():

    def __init__(self):
        self.uname = platform.uname()
        boot_time_timestamp = psutil.boot_time()
        self.bt = datetime.fromtimestamp(boot_time_timestamp)

    def get_size(self, bytes, suffix="B"):
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor

    def print_system_info(self):
        print("=" * 40, "System Information", "=" * 40)
        uname = platform.uname()
        print(f"System: {uname.system}")
        print(f"Node Name: {uname.node}")
        print(f"Release: {uname.release}")
        print(f"Version: {uname.version}")
        print(f"Machine: {uname.machine}")
        print(f"Processor: {uname.processor}")

    def get_system_name (self):
        return self.uname.system

    def get_system_node (self):
        return self.uname.node

    def get_system_release (self):
        return self.uname.release

    def get_system_version (self):
        return self.uname.version

    def get_system_machine (self):
        return self.uname.machine

    def get_system_processor (self):
        return self.uname.processor

    def print_boot_time(self):
        print("=" * 40, "Boot Time", "=" * 40)
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

    def get_boot_year(self):
        return self.bt.year

    def get_boot_month(self):
        return self.bt.month

    def get_boot_day(self):
        return self.bt.day

    def get_boot_hour(self):
        return self.bt.hour

    def get_boot_minute(self):
        return self.bt.minute

    def get_boot_second(self):
        return self.bt.second

    def print_CPU_info(self):
        print("=" * 40, "CPU Info", "=" * 40)
        # number of cores
        print("Physical cores:", psutil.cpu_count(logical=False))
        print("Total cores:", psutil.cpu_count(logical=True))
        # CPU frequencies
        cpufreq = psutil.cpu_freq()
        print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
        print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
        print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
        # CPU usage
        print("CPU Usage Per Core:")
        for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            print(f"Core {i}: {percentage}%")
        print(f"Total CPU Usage: {psutil.cpu_percent()}%")

    def get_physical_cores(self):
        return psutil.cpu_count(logical=False)

    def get_total_cores(self):
        return psutil.cpu_count(logical=True)

    def get_max_frequency(self):
        cpufreq = psutil.cpu_freq()
        return cpufreq.max

    def get_min_frequency(self):
        cpufreq = psutil.cpu_freq()
        return cpufreq.min

    def get_current_frequency(self):
        cpufreq = psutil.cpu_freq()
        return cpufreq.current

    def get_total_CPU_usage(self):
        return psutil.cpu_percent()

    def get_core_usage(self):
        for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            print(f"Core {i}: {percentage}%")

    def print_memory_details(self):
        # Memory Information
        print("=" * 40, "Memory Information", "=" * 40)
        # get the memory details
        svmem = psutil.virtual_memory()
        print(f"Total: {get_size(svmem.total)}")
        print(f"Available: {get_size(svmem.available)}")
        print(f"Used: {get_size(svmem.used)}")
        print(f"Percentage: {svmem.percent}%")
        print("=" * 20, "SWAP", "=" * 20)
        # get the swap memory details (if exists)
        swap = psutil.swap_memory()
        print(f"Total: {get_size(swap.total)}")
        print(f"Free: {get_size(swap.free)}")
        print(f"Used: {get_size(swap.used)}")
        print(f"Percentage: {swap.percent}%")

    def get_total_memory(self):
        
