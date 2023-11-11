from tkinter import *

root=Tk()

def myClick():
    myLabel=Label(root,text="Look I clicked a button")
    myLabel.pack()
    
myButton=Button(root,text="Click Me!",padx=30,pady=20,command=myClick,fg="white",bg="blue")

myButton.pack()
root.mainloop()
