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


# def remove_item():
#     db.remove(selected_item[0])
#     clear_text()
#     populate_list()


# def update_item():
#     db.update(selected_item[0], name_text.get(), time_text.get(),
#               freq_text.get(), price_text.get())
#     populate_list()


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

# Price
# price_text = StringVar()
# price_label = ttk.Label(app, text='      Price', font=('bold', 12))
# price_label.grid(row=1, column=2, sticky=W)
# price_entry = ttk.Entry(app, textvariable=price_text, width=30)
# price_entry.grid(row=1, column=3)
# names List (Listbox)
names_list = Text(app, height=6, width=70, border=1)
names_list.grid(row=6, column=0, columnspan=4, rowspan=9, pady=10, padx=20)

rules = """                    To add Frequency

- Add comma separated week numbers (0 for Sunday and so on)
- Eg: For Monday, Wednesday: 1,3
- For Monday to Wednesday: 1-3
- Similarly for months"""

names_list.insert(END, rules)
# names_list.configure(bg=style.lookup('TLabel', 'background'), fg=style.lookup('TLabel', 'foreground'))
# Create scrollbar
# scrollbar = ttk.Scrollbar(app)
# scrollbar.grid(row=6, column=4)
# scrollbar.place(x=535, y=140)
# Set scroll to listbox
# names_list.configure(yscrollcommand=scrollbar.set)
# scrollbar.configure(command=names_list.yview)
# Bind select
# names_list.bind('<<ListboxSelect>>', print("what"))



# to change color
# app.configure(background="white")


# name_text = StringVar()
# name_label = Label(app, text='Current Consumption', font=('bold', 14), pady=40)
# name_label.grid(row=0, column=0, sticky=W)

# apps = ['Chrome', 'Edge', 'Files', 'Email']

# apps_list = Listbox(app, height=8, width=25)
# apps_list.grid(row=1, column=0, pady=20, padx=10)


# usage_percent = Label(app, text='      Total consumption', font=('bold', 14), pady=30)
# usage_percent.grid(row=0, column=1, sticky=W)


# Buttons
# add_btn = ttk.Button(app, text='Submit', width=10, command=add_item)
# add_btn.grid(row=5, column=0, pady=1)
# th_add_btn = ttk.Button(app, text='Add name', width=10, command=add_item)
# th_add_btn.pack()

remove_btn = ttk.Button(app, text='Submit', width=10, command=add_item)
remove_btn.grid(row=5, column=1, pady=20)

# update_btn = Button(app, text='Update name', width=12, command=update_item)
# update_btn.grid(row=2, column=2)

# clear_btn = ttk.Button(app, text='Clear Input', width=10, command=clear_text)
# clear_btn.grid(row=5, column=2)

# populate_list()

# s = ttk.Style()

# s.theme_use('classic')


app.mainloop()