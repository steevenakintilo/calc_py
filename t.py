# Python program to determine which
# button was pressed in tkinter

# Import the library tkinter
from tkinter import *

# Create a GUI app
app = Tk()

# Create a function with one parameter, i.e., of
# the text you want to show when button is clicked
def print_ok():
    for i in range(1000):
        print(i)
def which_button(b):
    if b == "1":
        print_ok()
    elif b == "2":
        print(b)
    elif b == "2":
        print(b)
    elif b == "3":
        print(b)
    elif b == "4":
        print(b)
    elif b == "5":
        print(b)
    elif b == "Quit":
        quit()

# Creating and displaying of button b1
b1 = Button(app, text="1",
			command=lambda m="1": which_button(m))

b1.grid(padx=10, pady=10)

# Creating and displaying of button b2
b2 = Button(app, text="2",
			command=lambda m="2": which_button(m))
b2.grid(padx=10, pady=10)

b3 = Button(app, text="3",
			command=lambda m="3": which_button(m))

b3.grid(padx=10, pady=10)

# Creating and displaying of button b2
b4 = Button(app, text="4",
			command=lambda m="4": which_button(m))
b4.grid(padx=10, pady=10)

b5 = Button(app, text="5",
			command=lambda m="5": which_button(m))

b5.grid(padx=10, pady=10)

b6 = Button(app, text="Quit",
			command=lambda m="Quit": which_button(m))

b6.grid(padx=10, pady=10)

# Make the infinite loop for displaying the app
app.mainloop()
