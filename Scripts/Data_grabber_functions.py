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

    def get_size(self, bytes, suffix="B"):  # Will be applied onto the returned raw number of bytes
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:  # Will add the correct unit after conversion
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor  # Will divide the bytes by the factor untill it is less than to ge the correct unit

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

    def get_bytes_sent(self):
        net_io = psutil.net_io_counters()
        return self.get_size(net_io.bytes_sent)

    def get_bytes_recv(self):
        net_io = psutil.net_io_counters()
        return self.get_size(net_io.bytes_recv)

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