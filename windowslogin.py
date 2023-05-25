from msilib.schema import Font
from tkinter import*
import winsound

debi=Tk()

debi.geometry=("1900x1080")

debi.title("WINDOWS LOGIN PAGE_BY_DEBI_PRASAD")

my=Canvas(debi,height="2560",width="1440",bg="#6e0962")

#for 1st square
r1=my.create_rectangle(650,200,551,295,activefill="violet",
activeoutline="violet",fill="#00A4EF",
outline="#00A4EF",offset="nw",state="normal")

#for 2nd square
r2=my.create_rectangle(655,200,754,295,activefill="orange",
activeoutline="orange",fill="#00A4EF",
outline="#00A4EF",offset="ne",state="normal")

#for 3rd square
r3=my.create_rectangle(650,300,551,395,activefill="red",
activeoutline="red",fill="#00A4EF",
outline="#00A4EF",offset="sw",state="normal",)

#for 4th square
r4=my.create_rectangle(754,300,655,395,activefill="yellow",
activeoutline="yellow",fill="#00A4EF",
outline="#00A4EF",offset="se",state="normal")
#for windows name
nam=Label(debi,text="WINDOWS 11",font=("bold",20),
fg="#00A4EF",bg="#6e0962")
#position
nam.place(x=610,y=400)
#welcome text
welcome=Label(debi,text="WELCOME DEBI",font=("bold",30),
fg="#00A4EF",bg="#6e0962")
#position
welcome.place(x=560,y=140)
#security text
stext=Label(debi,text="To sign in, put your windows hello pin.",font=("bold",15),
fg="white",bg="#6e0962")
stext.place(x=560,y=450)
pin=Entry(bg="white",width="30")
pin.place(x=630,y=500)
#play startup sound
winsound.PlaySound('D:\Workspace-D',winsound.SND_FILENAME)
my.pack()
debi.mainloop()