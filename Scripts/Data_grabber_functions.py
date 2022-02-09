import platform
import psutil
from datetime import datetime
import GPUtil
from tabulate import tabulate


class data_grabbing():

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

    def get_system_name(self):
        return self.uname.system

    def get_system_node(self):
        return self.uname.node

    def get_system_release(self):
        return self.uname.release

    def get_system_version(self):
        return self.uname.version

    def get_system_machine(self):
        return self.uname.machine

    def get_system_processor(self):
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
        print(f"Total: {self.get_size(svmem.total)}")
        print(f"Available: {self.get_size(svmem.available)}")
        print(f"Used: {self.get_size(svmem.used)}")
        print(f"Percentage: {svmem.percent}%")
        print("=" * 20, "SWAP", "=" * 20)
        # get the swap memory details (if exists)
        swap = psutil.swap_memory()
        print(f"Total: {self.get_size(swap.total)}")
        print(f"Free: {self.get_size(swap.free)}")
        print(f"Used: {self.get_size(swap.used)}")
        print(f"Percentage: {swap.percent}%")

    def get_total_memory(self):
        svmem = psutil.virtual_memory()
        return self.get_size(svmem.total)

    def get_available_memory(self):
        svmem = psutil.virtual_memory()
        return self.get_size(svmem.available)

    def get_used_memory(self):
        svmem = psutil.virtual_memory()
        return self.get_size(svmem.used)

    def get_percent_memory(self):
        svmem = psutil.virtual_memory()
        return svmem.percent

    def get_swap_total_memory(self):
        swap = psutil.swap_memory()
        return self.get_size(swap.total)

    def get_swap_free_memory(self):
        swap = psutil.swap_memory()
        return self.get_size(swap.free)

    def get_swap_used_memory(self):
        swap = psutil.swap_memory()
        return self.get_size(swap.used)

    def get_swap_percent_memory(self):
        swap = psutil.swap_memory()
        return swap.percent

    def print_disk_details(self):
        print("=" * 40, "Disk Information", "=" * 40)
        print("Partitions and Usage:")
        # get all disk partitions
        partitions = psutil.disk_partitions()
        for partition in partitions:
            print(f"=== Device: {partition.device} ===")
            print(f"  Mountpoint: {partition.mountpoint}")
            print(f"  File system type: {partition.fstype}")
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                # this can be caught due to the disk that
                # isn't ready
                continue
            print(f"  Total Size: {self.get_size(partition_usage.total)}")
            print(f"  Used: {self.get_size(partition_usage.used)}")
            print(f"  Free: {self.get_size(partition_usage.free)}")
            print(f"  Percentage: {partition_usage.percent}%")
        # get IO statistics since boot
        disk_io = psutil.disk_io_counters()
        print(f"Total read: {self.get_size(disk_io.read_bytes)}")
        print(f"Total write: {self.get_size(disk_io.write_bytes)}")

    def get_device_partition_name(self, partition_device):
        return partition_device.device

    def get_device_partition_mountpoint(self, partition_device):
        return partition_device.mountpoint

    def get_device_partition_fstype(self, partition_device):
        return partition_device.fstype

    def get_usage_partition_size(self, partition_usage):
        return self.get_size(partition_usage.total)

    def get_usage_partition_used(self, partition_usage):
        return self.get_size(partition_usage.used)

    def get_usage_partition_free(self, partition_usage):
        return self.get_size(partition_usage.free)

    def get_usage_partition_percent(self, partition_usage):
        return partition_usage.percent

    def get_disk_total_read(self):
        disk_io = psutil.disk_io_counters()
        return self.get_size(disk_io.read_bytes)

    def get_disk_total_write(self):
        disk_io = psutil.disk_io_counters()
        return self.get_size(disk_io.write_bytes)

    def print_network_info(self):
        print("=" * 40, "Network Information", "=" * 40)
        # get all network interfaces (virtual and physical)
        if_addrs = psutil.net_if_addrs()
        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                print(f"=== Interface: {interface_name} ===")
                if str(address.family) == 'AddressFamily.AF_INET':
                    print(f"  IP Address: {address.address}")
                    print(f"  Netmask: {address.netmask}")
                    print(f"  Broadcast IP: {address.broadcast}")
                elif str(address.family) == 'AddressFamily.AF_PACKET':
                    print(f"  MAC Address: {address.address}")
                    print(f"  Netmask: {address.netmask}")
                    print(f"  Broadcast MAC: {address.broadcast}")
        # get IO statistics since boot
        net_io = psutil.net_io_counters()
        print(f"Total Bytes Sent: {self.get_size(net_io.bytes_sent)}")
        print(f"Total Bytes Received: {self.get_size(net_io.bytes_recv)}")

    def get_bytes_sent(self):
        net_io = psutil.net_io_counters()
        return self.get_size(net_io.bytes_sent)

    def get_bytes_recv(self):
        net_io = psutil.net_io_counters()
        return self.get_size(net_io.bytes_recv)


    # NEED TO GET THE NETWORKING GET FUNCTIONS WORKING ASAP, THEY NEED TO BE IMPLEMENTED IN A LOOP IN THE MAIN

    def print_GPU_info(self):
        print("*" * 40, "GPU", "*" * 40)
        gpus = GPUtil.getGPUs()
        list_gpus = []
        for gpu in gpus:
            # get the GPU id
            gpu_id = gpu.id
            # name of GPU
            gpu_name = gpu.name
            # get % percentage of GPU usage of that GPU
            gpu_load = f"{gpu.load * 100}%"
            # get free memory in MB format
            gpu_free_memory = f"{gpu.memoryFree}MB"
            # get used memory
            gpu_used_memory = f"{gpu.memoryUsed}MB"
            # get total memory
            gpu_total_memory = f"{gpu.memoryTotal}MB"
            # get GPU temperature in Celsius
            gpu_temperature = f"{gpu.temperature} °C"
            gpu_uuid = gpu.uuid
            list_gpus.append((
                gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
                gpu_total_memory, gpu_temperature, gpu_uuid
            ))

    def get_gpus(self):
        return GPUtil.getGPUs()

    def get_GPU_id(self, gpu):
        return gpu.id

    def get_GPU_name(self, gpu):
        return gpu.name

    def get_GPU_load(self, gpu):
        return gpu.load * 100

    def get_GPU_free_memory(self, gpu):
        return gpu.memoryFree

    def get_GPU_used_memory(self, gpu):
        return gpu.memoryUsed

    def get_GPU_temp(self, gpu):
        return gpu.temperature

if __name__ == '__main__':
    data_grabbing = data_grabbing()
    data_grabbing.print_disk_details()
    data_grabbing.print_GPU_info()
    data_grabbing.print_memory_details()
    data_grabbing.print_network_info()
    data_grabbing.print_boot_time()
    data_grabbing.print_system_info()
