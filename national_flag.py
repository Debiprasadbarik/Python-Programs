from tkinter import *
import tkinter.messagebox as MessageBox

deb=Tk()
deb.geometry("1900x1080")
deb["bg"]="#fff"
deb.title("INDIAN NATIONAL FLAG")
canvas=Canvas(deb, height=1900,width=1080, bg="#000000")
canvas.pack()
canvas.create_rectangle(200,100,800,230,outline="#FF9933",fill="#FF9933")

canvas.create_rectangle(200,233,800,370,outline="#fff",fill="#fff")

canvas.create_rectangle(200,373,800,510,outline="#06c75d",fill="#06c75d")
img=PhotoImage(file="de.png")
canvas.create_image(450,245, anchor=NW, image=img)

insert=Button(deb,text="HAPPY REPUBLIC DAY~DEBI☺",font=("bold",20),bg="lightgreen",command=INSERT)
insert.place(x=550,y=600)
deb.mainloop()
