# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# from psutil import cpu_percent

# cpu_percent()

# frame_len = 50
# output = []
# def animate(i):
#     output.append(cpu_percent())
#     if(len(output)<=frame_len):
#         plt.cla()
#         plt.plot(output,'r','Real Time CPU Usage')
#     plt.tight_layout()
#     plt.show()




# ani = FuncAnimation(plt.gcf(),animate,interval=1000)
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from psutil import cpu_percent

fig, ax = plt.subplots()
xdata, ydata = [], []
#make list of x and y data initialized with 0





ln, = plt.plot([], [], 'ro')

def init():
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 100)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(cpu_percent())
    print(xdata)
    print(ydata)
    print("------")
    # if(len(xdata)>50):
        # plt.cla()
        # plt.plot(xdata,ydata,'r')
        # xdata.clear()
        # ydata.clear()
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 50, 128),init_func=init, blit=True)
plt.show()