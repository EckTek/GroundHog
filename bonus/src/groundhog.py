from colorama import init, Fore
import matplotlib.pyplot as plt
import numpy as np
import math as m

class Groundhog:
    sign = False
    idx = 0
    cnt_switch = int(0)
    av = [float("NaN")]
    ev = [float("NaN")]
    der = [float("NaN")]
    inputs = []
    sw_data = []
    weirdests = []

    def __init__(self, days):
        self.days = days

# START: Util methods
    def print_inputs(self):
        print (self.inputs)

    def append_inputs(self, to_append):
        self.inputs.append(to_append)

    def update_index(self):
        self.idx += 1

    def print_switch(self, state):
        if state:
            self.cnt_switch += 1
            self.sign = not self.sign
            print ("\ta switch occurs")
        else:
            print ("")

    def detect_switch(self):
        if m.isnan(self.ev[-1]):
            print ("")
            return
        elif len(self.inputs) < self.days:
            print ("")
            return
        if not self.sign:
            x = min(self.inputs[-self.days-1:-1])
            self.print_switch((x > self.inputs[-1]))
        else:
            x = max(self.inputs[-self.days-1:-1])
            self.print_switch((x < self.inputs[-1]))

    def print_line(self):
        print ("g={:.2f}\tr={:.0f}%\ts={:.2f}".format(
                                                round(self.av[-1], 2),
                                                round(self.ev[-1], 0),
                                                round(self.der[-1], 2)), end='')
        self.detect_switch()

    def data_to_file(self, lst, path):
        f = open(path, "w+")
        for x in lst:
            f.write("%f\n" % x)
        f.close()

    def draw_graph(self):
#        x = np.linspace(0, 20, 1000)
        plt.plot(self.inputs, '-g', label="inputs")
        plt.plot(self.av, '-m', label="g")
        plt.plot(self.ev, '--r', label="r")
        plt.plot(self.der, 'b', label="s")
#        plt.axhline(y=av, color='r', linestyle="-")
        plt.legend(fancybox=True, framealpha=1, borderpad=1, loc="lower right", ncol=2)
        plt.xlabel('Days')
        plt.ylabel('Values')
        plt.show()

    def set_graph(self):
        self.data_to_file(self.av, "data/g.txt")
        self.data_to_file(self.ev, "data/r.txt")
        self.data_to_file(self.der, "data/s.txt")
        self.data_to_file(self.inputs, "data/inputs.txt")
        self.draw_graph()

    def print_end(self, weirdests):
        print("Global tendency switched {} times".format(self.cnt_switch))
        print("5 weirdest values are {}".format(weirdests[:5]))

    def desc_bubble_sort(self, lst):
        for n in range (len(lst)-1, 0, -1):
            for i in range(n):
                if lst[i][0] < lst[i + 1][0]:
                    val = lst[i][0]
                    idx = lst[i][1]
                    lst[i][0] = lst[i + 1][0]
                    lst[i][1] = lst[i + 1][1]
                    lst[i + 1][0] = val
                    lst[i + 1][1] = idx
        return lst

    def compute_weirdests(self):
        if m.isnan(self.av[0]):
            del self.av[0]
        for i in range(1, len(self.inputs[1:-1])):
            x = [abs(round((self.inputs[i - 1] + self.inputs[i + 1]) / 2.0 - self.inputs[i], 5)), i]
            self.sw_data.append(x)
        self.sw_data = self.desc_bubble_sort(self.sw_data)
        return self.sw_data


    def end(self):
        if len(self.inputs) < self.days:
            exit (84)
        self.sw_data = self.compute_weirdests()
        for i in range(len(self.sw_data)):
            self.weirdests.append(self.inputs[self.sw_data[i][1]])
        self.set_graph()
        self.print_end(self.weirdests)

    def enough_len(self, days_nb):
        return len(self.inputs) >= days_nb

    def sum_subs(self, lst):
        return sum([n - curr for curr, n in zip(lst[self.idx:], lst[self.idx + 1:]) if n - curr >= 0])
# END: Util methods

# START: Temperature average
    def compute_average(self):
        if not self.enough_len(self.days + 1):
            return
        self.av.append(self.sum_subs(self.inputs) / self.days)
        self.update_index()
# END

# START: Relative Temperature Evolution
    def compute_evolution(self):
        if not self.enough_len(self.days + 1):
            return
        if self.inputs[-self.days - 1] == 0 and not m.isnan(self.inputs[-self.days - 1]):
            self.ev.append(0)
        else:
            self.ev.append((self.inputs[-1] / self.inputs[-self.days - 1]) * 100 - 100)
# END

# START: Standard derivation code
    def compute_variance(self):
        mean = sum(self.inputs[-self.days:]) / self.days
        variance = sum([m.pow(x - mean, 2) for x in (self.inputs[-self.days:])])
        return variance / self.days

    def compute_derivation(self):
        if not self.enough_len(self.days):
            return
        self.der.append(m.sqrt(self.compute_variance()))
# END: Standard derivation code


def compute_all(inp, ind):
    ind.append_inputs(inp)
    ind.compute_average()
    ind.compute_evolution()
    ind.compute_derivation()
    ind.print_line()

################# DON'T PUSH THAT !!!! ############
def get_file():
    file = open('inputs', "r")
    data = file.readlines()
    data = [float(x.strip()) for x in data]
    file.close()
    return (data)
################# DON'T PUSH THAT !!!! ############

def loop(indicators):
    cnt = 0
    init(autoreset=True)
    inputs = get_file()

    while True:
        if cnt < len(inputs):
            inp = inputs[cnt]
        else:
            try:
                inp = input(Fore.YELLOW + "")
                print("", end="")
            except EOFError:
                exit (84)
            if inp == "STOP":
                indicators.end()
                exit(0)
            try:
                inp = float(inp)
            except:
                exit(84)
        compute_all(inp, indicators)
        cnt += 1

def groundhog(days):
    indicators = Groundhog(days)
    loop(indicators)
