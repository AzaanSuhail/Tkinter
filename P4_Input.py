from tkinter import *

root=Tk()

e = Entry(root, width=50, fg="red", bg="#99B080")
e.pack()
def myClick():
    myLabel=Label(root,text="Hello "+e.get())
    myLabel.pack()

myButton=Button(root,text="Enter Your Name",command=myClick,fg="white",bg="Black",width=15,height=5)
myButton.pack()

root.mainloop()