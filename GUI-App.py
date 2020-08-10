from tkinter import *
from tkinter import ttk

#make the GUI window
root = Tk()
#giving it attributes
root.title("MyApp")
root.geometry('400x400')
#Adding a label
label1 = Label(root, text="Enter username: ")
#the first parameter 'root' basically means we want to add the label to our main window which we named root....if we named it canvas the the first parameter would be canvas
#the second is what we want the label to hold...the text
label1.pack()
#pack is one of the things we use to add the widgets to our window
entry1 = Entry(root, width=30, bg="white")
# width is the width of the entry box and bg is the background color of the entry box
entry1.pack()
button1 = Button(root, text="Submit")
button1.pack()

root.mainloop()

