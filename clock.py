from tkinter import *
from tkinter.ttk import *
from time import strftime
deb=Tk()
deb.title("DIGITAL CLOCK BY DEBI")
def time():
    string=strftime('%I:%M:%S: %p %Y')
    clock.config(text=string)
    clock.after(1000,time)
clock=Label(deb,font=('DS-digital',80),background="black",foreground="white")
clock.pack(anchor='center')
time()
deb.mainloop()