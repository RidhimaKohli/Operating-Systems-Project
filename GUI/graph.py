import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import psutil
import collections

def my_function(i):
    cpu_usage_array.popleft()
    cpu_usage_array.append(psutil.cpu_percent())

    ram_usage_array.popleft()
    ram_usage_array.append(psutil.virtual_memory().percent)
    
    cpu_subplot.cla()
    ram_subplot.cla()

    cpu_subplot.plot(cpu_usage_array, c='#008514')
    cpu_subplot.scatter(len(cpu_usage_array)-1, cpu_usage_array[-1], c='#05fc2a')
    cpu_subplot.text(len(cpu_usage_array)-1, cpu_usage_array[-1]+2, "{}%".format(cpu_usage_array[-1]))

    cpu_subplot.set_xticks(np.arange(-1,10,2))
    cpu_subplot.set_xticklabels(np.arange(10,-1,-2))
    cpu_subplot.set_xlabel('Time (in seconds)')
    cpu_subplot.set_title('CPU Usage\n')
    cpu_subplot.set_ylim(0,100)

    # remove spines
    cpu_subplot.spines['left'].set_visible(False)
    cpu_subplot.spines['right'].set_visible(False)
    cpu_subplot.spines['top'].set_visible(False)

    # grid
    cpu_subplot.set_axisbelow(True)
    cpu_subplot.yaxis.grid(linestyle='dashed', alpha=0.8)

    ram_subplot.plot(ram_usage_array, c='#990227')
    ram_subplot.scatter(len(ram_usage_array)-1, ram_usage_array[-1], c='#990227')
    ram_subplot.text(len(ram_usage_array)-1, ram_usage_array[-1]+2, "{}%".format(ram_usage_array[-1]))

    ram_subplot.set_xticks(np.arange(-1,10,2))
    ram_subplot.set_xticklabels(np.arange(10,-1,-2))
    ram_subplot.set_xlabel('Time (in seconds)')
    ram_subplot.set_title('RAM Usage\n')
    ram_subplot.set_ylim(0,100)
    # remove spines
    ram_subplot.spines['left'].set_visible(False)
    ram_subplot.spines['right'].set_visible(False)
    ram_subplot.spines['top'].set_visible(False)

    # grid
    ram_subplot.set_axisbelow(True)
    ram_subplot.yaxis.grid(linestyle='dashed', alpha=0.8)

cpu_usage_array = collections.deque(np.zeros(10))
ram_usage_array = collections.deque(np.zeros(10))

fig = plt.figure(figsize=(10,6), facecolor='#DEDEDE')

cpu_subplot = plt.subplot(122)
ram_subplot = plt.subplot(121)

cpu_subplot.set_facecolor('#DEDEDE')
ram_subplot.set_facecolor('#DEDEDE')

animation = FuncAnimation(plt.gcf(), my_function, interval=1000)

plt.show()