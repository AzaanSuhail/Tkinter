from tkinter import *
root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    # e.delete(0,END)
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
    
def button_clear():
    e.delete(0,END)    

def button_add():
    first_num=e.get()
    global f_num
    global math
    math="addition"
    f_num=int(first_num)
    e.delete(0,END)
    
# def button_equal():
#     second_num=e.get()
#     e.delete(0,END)
#     e.insert(0,f_num+int(second_num))

def button_equal():
    second_num=e.get()
    e.delete(0,END)
    
    if math=="addition":
        e.insert(0,f_num+int(second_num))
        
    elif math=="subtraction":
        e.insert(0,f_num-int(second_num))
        
    elif math=="multiplication":
        e.insert(0,f_num*int(second_num))
    else:
        e.insert(0,f_num/int(second_num))
    
    
def button_subtract():
    first_num=e.get()
    global f_num
    global math
    math="subtraction"
    f_num=int(first_num)
    e.delete(0,END)
    
def button_multiply():
    first_num=e.get()
    global f_num
    global math
    math="multiplication"
    f_num=int(first_num)
    e.delete(0,END)

def button_divide():
    first_num=e.get()
    global f_num
    global math
    math="division"
    f_num=int(first_num)
    e.delete(0,END)
    
#defining Buttons
button_1=Button(root,text="1" ,padx=40 ,pady=20,command=lambda:button_click(1),bg="#A6CF98",fg="black")
button_2=Button(root,text="2" ,padx=40 ,pady=20,command=lambda:button_click(2),bg="#DCBFFF",fg="black")
button_3=Button(root,text="3" ,padx=40 ,pady=20,command=lambda:button_click(3),bg="#BE3144",fg="black")
button_4=Button(root,text="4" ,padx=40 ,pady=20,command=lambda:button_click(4),bg="#FECDA6",fg="black")
button_5=Button(root,text="5" ,padx=40 ,pady=20,command=lambda:button_click(5),bg="#A0E9FF",fg="black")
button_6=Button(root,text="6" ,padx=40 ,pady=20,command=lambda:button_click(6),bg="#DADDB1",fg="black")
button_7=Button(root,text="7" ,padx=40 ,pady=20,command=lambda:button_click(7),bg="#E95793",fg="black")
button_8=Button(root,text="8" ,padx=40 ,pady=20,command=lambda:button_click(8),bg="#176B87",fg="black")
button_9=Button(root,text="9" ,padx=40 ,pady=20,command=lambda:button_click(9),bg="#F4E869",fg="black")

button_0=Button(root,text="0" ,padx=40 ,pady=20,command=lambda:button_click(0),bg="#FCF5ED",fg="black")

button_Add=Button(root,text="+" ,padx=38 ,pady=20,command=button_add,bg="#776B5D",fg="black")
button_Equal=Button(root,text="=" ,padx=89 ,pady=20,command=button_equal,bg="black",fg="white")
button_Clear=Button(root,text="Clear" ,padx=79 ,pady=20,command=button_clear ,bg="black", fg="white")

button_Subtract=Button(root,text="-" ,padx=39 ,pady=20,command=button_subtract,bg="#776B5D",fg="black")
button_Multiply=Button(root,text="x" ,padx=44 ,pady=20,command=button_multiply,bg="#776B5D",fg="black")
button_Divide=Button(root,text="%" ,padx=36 ,pady=20,command=button_divide,bg="#776B5D",fg="black")

#putting buttons on the screen
button_1.grid(row=3 ,column=0)
button_2.grid(row=3 ,column=1)
button_3.grid(row=3 ,column=2)

button_4.grid(row=2 ,column=0)
button_5.grid(row=2 ,column=1)
button_6.grid(row=2 ,column=2)

button_7.grid(row=1 ,column=0)
button_8.grid(row=1 ,column=1)
button_9.grid(row=1 ,column=2)

button_0.grid(row=5,column=0)
button_Add.grid(row=6,column=0)
button_Clear.grid(row=5,column=1,columnspan=2)
button_Equal.grid(row=6,column=1,columnspan=2)
button_Subtract.grid(row=7,column=0)
button_Multiply.grid(row=7,column=1)
button_Divide.grid(row=7,column=2)

root.mainloop()
