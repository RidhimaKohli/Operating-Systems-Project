from tkinter import *
import subprocess





window=Tk()
window.geometry("400x400")

def display():
    subprocess.call("statCode.sh",shell=True)
    output.delete(0.0,END)
    f = open("out.txt", "r")
    data = f.read()
    output.insert(END,data)
    f.close()

window.title("This is window")
window.configure(background="black")
head = Label(window,text="Welcome to GUI for Linux !", font=("Arial", 20),bg="black",fg="white",justify=CENTER)
head.grid(row=1,column=0)
button =Button(window,text="Get memory details",width=25,height=5,command=display,font=("Arial", 15),bg="#A2D2FF",fg="black",activebackground="#90AACB", activeforeground="#fff").grid(row=4,column=0,pady=30)
output=Text(window,width=75,height=6,wrap=WORD,background="white", font=(None, 10))
output.grid(row=7,column=0,columnspan=2,pady=40)



window.mainloop()