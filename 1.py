from tkinter import *
from tkinter import filedialog as fd


def add_image():
    filetypes = (
        ('obrazy PNG', '*.png'),
        ('All files','*.*')
    )
    fd.askopenfilename(filetypes=filetypes)

window = Tk()
window.minsize(width=640, height=480)
window.maxsize(width=640, height=480)

photo = PhotoImage(file="123.png")

frame1 = Frame(window, bg="black", height=50)
frame1.pack()

addButton = Button(frame1, command=add_image, text = "Dodaj obrazek", font = ("Arial, 24"))
addButton.pack()

mainFrame = Label(window,
                  text="Moja pierwsza gra",
                  font=("Ariel",28),
                  bd=10,
                  bg="black",
                  fg="white",
                  image=photo,
                  compound="top")

mainFrame.pack()

label2 = Label(window, text="Jakiś tekst", bd=3, bg="blue" , font = ("Arial", 24), fg="white")
label2.pack()



window.mainloop()