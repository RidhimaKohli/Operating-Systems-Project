from tkinter import font
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import psutil
import collections
plt.rcParams['text.color'] = 'white'
# plt.title('Live Graph')


def my_function(i):
    cpu_usage_array.popleft()
    cpu_usage_array.append(psutil.cpu_percent())

    ram_usage_array.popleft()
    ram_usage_array.append(psutil.virtual_memory().percent)

    cpu_subplot.cla()
    ram_subplot.cla()

    cpu_subplot.plot(cpu_usage_array, c='#05fc2a')
    cpu_subplot.scatter(len(cpu_usage_array)-1,
                        cpu_usage_array[-1], c='#05fc2a')
    cpu_subplot.text(len(cpu_usage_array)-1,
                     cpu_usage_array[-1]+2, "{}%".format(cpu_usage_array[-1]))

    cpu_subplot.set_xticks(np.arange(-1, 10, 2))
    cpu_subplot.set_xticklabels(np.arange(10, -1, -2))
    cpu_subplot.set_xlabel('Time (in seconds)').set_color('white')
    cpu_subplot.set_title('CPU Usage\n')
    cpu_subplot.set_ylim(0, 100)

    # remove spines
    cpu_subplot.spines['left'].set_visible(False)
    cpu_subplot.spines['right'].set_visible(False)
    cpu_subplot.spines['top'].set_visible(False)

    # grid
    cpu_subplot.set_axisbelow(True)
    cpu_subplot.yaxis.grid(linestyle='dashed', alpha=0.8)

    ram_subplot.plot(ram_usage_array, c='#EF1B1B')
    ram_subplot.scatter(len(ram_usage_array)-1,
                        ram_usage_array[-1], c='#EF1B1B')
    ram_subplot.text(len(ram_usage_array)-1,
                     ram_usage_array[-1]+2, "{}%".format(ram_usage_array[-1]))
    # # change color of subplot text
    # ram_subplot.texts[0].set_color('#EF1B1B')
    ram_subplot.set_xticks(np.arange(-1, 10, 2))
    ram_subplot.set_xticklabels(np.arange(10, -1, -2))
    ram_subplot.set_xlabel('Time (in seconds)').set_color('white')
    ram_subplot.set_title('RAM Usage\n')
    ram_subplot.set_ylim(0, 100)
    # remove spines
    ram_subplot.spines['left'].set_visible(False)
    ram_subplot.spines['right'].set_visible(False)
    ram_subplot.spines['top'].set_visible(False)

    # grid
    ram_subplot.set_axisbelow(True)
    ram_subplot.yaxis.grid(linestyle='dashed', alpha=0.8)


cpu_usage_array = collections.deque(np.zeros(10))
ram_usage_array = collections.deque(np.zeros(10))

fig = plt.figure(figsize=(10, 6), facecolor='#434343', num='LIVE GRAPH')

cpu_subplot = plt.subplot(122)
ram_subplot = plt.subplot(121)

cpu_subplot.set_facecolor('#434343')
ram_subplot.set_facecolor('#434343')
cpu_subplot.tick_params(axis='x', colors='white')
cpu_subplot.tick_params(axis='y', colors='white')
ram_subplot.tick_params(axis='x', colors='white')
ram_subplot.tick_params(axis='y', colors='white')
animation = FuncAnimation(plt.gcf(), my_function, interval=1000)

plt.show()
