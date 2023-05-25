from tkinter import *
root = Tk()
root.geometry("500x900")
canvas = Canvas(root, width=550, height=820)
canvas.pack()

a = canvas.create_rectangle(50, 0, 50, 0, fill='red')
canvas.move(a, 20, 20)