from tkinter import *
root=Tk()

root.title("Grid System")
myLabel1=Label(root,text="Hello World!").grid(row=0,column=1) #python is object oriented programming language and .grid is a object

myLabel2=Label(root,text="My Name is Azaan Suhail Siddiqui")
myLabel3=Label(root,text="                           ")
#there is no row or column in tkinter actually rows and columns are reletive

# myLabel1.grid(row=0,column=0) 
myLabel2.grid(row=1,column=5)
myLabel3.grid(row=1,column=1)

root.mainloop()
 