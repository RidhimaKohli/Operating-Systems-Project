from tkinter import *
import subprocess
from tkinter import ttk
from ttkthemes import ThemedStyle
from ttkthemes import themed_style


window = Tk()
window.geometry('600x250')


def display():
    subprocess.call(['sh', './statCode.sh'])
    output.delete(0.0, END)
    f = open("memory.txt", "r")
    data = f.read()
    output.insert(END, data)
    f.close()


def display2():
    subprocess.call(['sh', './statCode.sh'])
    output.delete(0.0, END)
    f = open("cpu.txt", "r")
    data = f.read()
    output.insert(END, data)
    f.close()


def display3():
    subprocess.call("python graph.py", shell=True)


window.title("System Stats")

style = ThemedStyle(window)
style.theme_use("equilux")
window.configure(bg=style.lookup('TLabel', 'background'))

# mem
button1 = ttk.Button(window, text='Memory',
                     width=10, command=display)
button1.grid(row=1, column=0, pady=1)
# cpu
button2 = ttk.Button(window, text='Cpu',
                     width=10, command=display2)
button2.grid(row=3, column=0, pady=1)
button3 = ttk.Button(window, text='Graph',
                     width=10, command=display3)
button3.grid(row=5, column=0, pady=1)
output = Text(window, width=75, height=6, wrap=WORD,
              font=(None, 10), bg='#434343', fg='#B4B2B2')
output.grid(row=7, column=0, columnspan=1, pady=10, padx=30)
window.mainloop()
