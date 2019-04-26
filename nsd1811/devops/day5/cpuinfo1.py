import psutil

class CPU:
    def __init__(self, core, temp):
        self.core = core
        self.temp = temp

    def __str__(self):
        return f"'{self.core}' : {self.temp}"

    # def __call__(self):


if __name__ == "__main__":
    info = psutil.sensors_temperatures()
    infodist = info['coretemp']
    for i in infodist:
        core = i.label
        temp = i.current
        c = CPU(core, temp)
        print(c)
    