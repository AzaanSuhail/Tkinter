from tkinter import *

root=Tk() 
# Now we create a root widget, by calling the Tk(). This automatically creates a graphical window with the title bar, minimize, maximize and close buttons. This handle allows us to put the contents in the window and reconfigure it as necessary.

# In tkinter everything is a widget

#defining label
myLabel=Label(root,text="Hello World!")

#just packing 
myLabel.pack()


root.mainloop()