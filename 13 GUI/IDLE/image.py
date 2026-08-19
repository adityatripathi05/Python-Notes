# Display Images using Label

from tkinter import *

root= Tk()

root.geometry("455x365")
photo=PhotoImage(file="bad.png")

label=Label(image=photo)
label.pack()

root.mainloop()

'''
# for jpeg image [tkinter not supports jpeg image]

from PIL import Image, ImageTk

image= Image.open("photo.jpg")
photo= ImageTk.PhotoImage(image)

'''

'''

from tkinter import *

root=Tk()

root.title("My Window")
root.geometry("600x600")

root.minsize(200,200)

root.maxsize(800,800)

#root.resizable(0,0)


root.mainloop()

'''
