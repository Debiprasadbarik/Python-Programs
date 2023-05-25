from tkinter import*

debi=Tk()
debi.geometry("1900x1080")
debi["bg"]="#fff"
debi.title("SMILE EMOJI- DEBI PRASAD")

wow=Canvas(debi,height="1900",width="1080",bg="#000000")
body=wow.create_oval(320,150,700,500,outline="yellow",width=10,fill="yellow") #bigface

eye_left=wow.create_oval(400,220,470,290,outline="#000000",width=3,fill="#000000") #left eye

#pupil_left=canvas.create_oval(430,250,445,265,outline="#000000",width=3,fill="#000000") #pupile l

eye_right=wow.create_oval(530,221,600,290,outline="#000000",width=3,fill="#000000") #right eye

#pupil_right=canvas.create_oval(560,251,575,265,outline="#000000",width=3,fill="#000000") #pupile R

mouth_happy=wow.create_line(400,380,480,450,590,380,smooth=1, width=10,state=NORMAL) #mouth
img=PhotoImage(file="heart.png")
left_heart=wow.create_image(420,230, anchor=NW,image=img)
right_heart=wow.create_image(550,229,anchor=NW, image=img)
wow.pack()
insert=Button(debi,text="Keep Smiling~Debi Prasad ",font=("bold",20),bg="#26ff60")
insert.place(x=550,y=550)

debi.mainloop()