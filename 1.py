from tkinter import *


window = Tk()
window.minsize(width=640, height=480)
window.maxsize(width=640, height=480)

label1 = Frame(window, width = 600, height = 400, bd=3, bg="black")
label2 = Label(window, text="Jakiś tekst", bd=3, bg="blue" , font = ("Arial", 24), fg="white")

label1.pack()
label2.pack()



window.mainloop()