from tkinter import *
import subprocess





window=Tk()
window.geometry("400x400")

def display():
    subprocess.call("statCode.sh",shell=True)
    output.delete(0.0,END)
    f = open("memory.txt", "r")
    data = f.read()
    output.insert(END,data)
    f.close()

def display2():
    subprocess.call("statCode.sh",shell=True)
    output.delete(0.0,END)
    f = open("cpu.txt", "r")
    data = f.read()
    output.insert(END,data)
    f.close()

def display3():
    subprocess.call("python graph.py",shell=True)


window.title("This is window")
window.configure(background="black")
head = Label(window,text="Welcome to GUI for Linux !", font=("Arial", 20),bg="black",fg="white",justify=CENTER)
head.grid(row=1,column=0)
#mem
button =Button(window,text="Get memory details",width=10,height=2,command=display,font=("Arial", 15),bg="#A2D2FF",fg="black",activebackground="#90AACB", activeforeground="#fff").grid(row=4,column=0,pady=30)
output=Text(window,width=75,height=6,wrap=WORD,background="white", font=(None, 10))
output.grid(row=7,column=0,columnspan=2,pady=40)
#cpu
button =Button(window,text="Get CPU details",width=10,height=2,command=display2,font=("Arial", 15),bg="#A2D2FF",fg="black",activebackground="#90AACB", activeforeground="#fff").grid(row=8,column=0,pady=30)

button =Button(window,text="Get live graph",width=10,height=2,command=display3,font=("Arial", 15),bg="#A2D2FF",fg="black",activebackground="#90AACB", activeforeground="#fff").grid(row=16,column=0,pady=30)



window.mainloop()