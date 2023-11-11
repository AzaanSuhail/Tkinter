from tkinter import *

root=Tk()

e = Entry(root, width=50, borderwidth=10 ,fg="red", bg="#99B080") #taking input from the user
e.pack()
# e.insert(13,"Enter Your name ")  This will automatically put advance text into the input field

# e.get() this is use to for ouput for given Entry input
def myClick():
    myLabel=Label(root,text="Hello "+e.get())
    myLabel.pack()

myButton=Button(root,text="Enter Your Name",command=myClick,fg="white",bg="Black",width=15,height=5)
myButton.pack()

root.mainloop()