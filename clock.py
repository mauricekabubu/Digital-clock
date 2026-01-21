# import the necessary libraries & modules:tkinter,datetime,
import tkinter
from tkinter import *
from time import strftime

# create the gui :geometry,configurations,title
win = Tk()
win.geometry('400x200')
win.title('Digital Clock')
win.config(bg='black')
# creating the clock labels
label0 = Label(win,text='Digital Clock',bg='black',fg='cyan',
               font=('britannic bold',30))
label0.pack(anchor=CENTER,pady=0)
clock_label = Label(win,bg='black',fg='green',font=('gotham bold',25))
clock_label.place(x=120,y=80)
# creating a function to update the current time on the clock
def update_time():
    current_time = strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000,update_time)

update_time()
win.mainloop()