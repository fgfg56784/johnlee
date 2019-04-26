import psutil

class CPU:
    def __init__(self, core, temp):
        self.core = core
        self.temp = temp

    def __str__(self):
        return f"'{self.core}': {self.temp}"

if __name__ == "__main__":
    cpudict  = psutil.sensors_temperatures()
    cpuinfo = cpudict['coretemp']
    for i in cpuinfo:
        core = i.label
        temp = i.current
        c = CPU(core, temp)
        print(c)