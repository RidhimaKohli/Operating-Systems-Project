from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedStyle
from ttkthemes import themed_style


def populate_list():
    f = open('details.txt', 'r')
    for i in f.readlines():
        names_list.insert(END, i)
    f.close()


def add_item():
    f = open('details.txt', 'a')
    prod = name_text.get()
    th = time_text_h.get()
    tm = time_entry_m.get()
    ret = freq_text.get()
    fw = freq_entry_w.get()
    send = "{Name: '"+prod + "',\nHour: " + th + ",\nMins: "+tm + ",\nMonths: '" + ret + "',\nWeeks: '" + fw+"'}"
    f.write(send)
    f.close()
    clear_text()


def select_item(event):
    try:
        global selected_item
        index = names_list.curselection()[0]
        print(index)
        selected_item = names_list.get(index)

        name_entry.delete(0, END)
        name_entry.insert(END, selected_item[1])
        time_entry.delete(0, END)
        time_entry.insert(END, selected_item[2])
        freq_entry.delete(0, END)
        freq_entry.insert(END, selected_item[3])
    except IndexError:
        pass


def clear_text():
    name_entry.delete(0, END)
    time_entry.delete(0, END)
    time_entry_m.delete(0, END)
    freq_entry.delete(0, END)
    freq_entry_w.delete(0, END)


# Create window object
app = Tk()

app.title('System Manager')
app.geometry('600x350')
style = ThemedStyle(app)
style.theme_use("equilux")

app.configure(bg=style.lookup('TLabel', 'background'))

# name
name_text = StringVar()
name_label = ttk.Label(app, text='Name', font=('bold', 9))
name_label.grid(row=0, column=0, sticky=W, pady=10)
name_entry = ttk.Entry(app, textvariable=name_text, width=30)
name_entry.grid(row=0, column=1)
# time
time_text_h = StringVar()

time_label = ttk.Label(app, text='Start Time', font=('bold', 9))
time_label.grid(row=1, column=0, sticky=W, pady=10)

time_entry = ttk.Entry(app, textvariable=time_text_h, width=30)
time_entry.grid(row=1, column=1)

time_label_h = ttk.Label(app, text='hrs', font=('bold', 9), width=5)
time_label_h.grid(row=1, column=2, sticky=W)

time_text_m = StringVar()

time_entry_m = ttk.Entry(app, textvariable=time_text_m, width=30, justify=LEFT)
time_entry_m.grid(row=2, column=1)

time_label_m = ttk.Label(app, text='mins', font=('bold', 9),width=5, justify=LEFT)
time_label_m.grid(row=2, column=2, sticky=W)


# freq
freq_text = StringVar()
freq_label = ttk.Label(app, text='Frequency (Months) ', font=('bold', 9))
freq_label.grid(row=3, column=0, sticky=W, pady=10)
freq_entry = ttk.Entry(app, textvariable=freq_text, width=30)
freq_entry.grid(row=3, column=1, pady=(10,5))

freq_text_w = StringVar()
freq_entry_w = ttk.Entry(app, textvariable=freq_text_w, width=30)
freq_entry_w.grid(row=4, column=1)
freq_label_w = ttk.Label(app, text='Weeks ', font=('bold', 9))
freq_label_w.grid(row=4, column=0, sticky=W)

names_list = Text(app, height=6, width=70, border=1)
names_list.grid(row=6, column=0, columnspan=4, rowspan=9, pady=10, padx=20)

rules = """                    To add Frequency

- Add comma separated week numbers (0 for Sunday and so on)
- Eg: For Monday, Wednesday: 1,3
- For Monday to Wednesday: 1-3
- Similarly for months"""

names_list.insert(END, rules)

remove_btn = ttk.Button(app, text='Submit', width=10, command=add_item)
remove_btn.grid(row=5, column=1, pady=20)


app.mainloop()