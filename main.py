# Python program to determine which
# button was pressed in tkinter

# Import the library tkinter
from tkinter import *
import time
import tkinter

# Create a GUI app
app = Tk()

def print_file(path):
    f = open(path, 'r')
    content = f.read()
    return(content)
    f.close()

def write_into_file(path,x):
    f = open(path, "w")
    f.write(str(x))
    f.close

def wwrite_into_file(path,x):
    f = open(path, "a")
    f.write(str(x))
    f.close

def check_file():
    number_one = print_file("num1")
    number_two = print_file("num2")
    if number_one != "" and number_two != "":
        return (1)
    else:
        return (0)


def write_num(x):
    write_into_file("check","num")
    number_one = print_file("num1")
    number_two = print_file("num2")
    res = print_file("res")
    check = print_file("check")
    if x == -1:
        write_into_file("num1","")
        write_into_file("num2","")
    if x != -1:
        if check == "op" or check == "num":
            if number_one != "" and number_two != "":
                write_into_file("num1",res)
                write_into_file("num2",x)
            elif number_one == "" and number_two == "":
                write_into_file("num1",x)
            elif number_one != "" and number_two == "":
                write_into_file("num2",x)    
def calc_res(number_one,op,number_two):
    res = 0
    r = print_file("res")
    if op == "+":
        number_one = print_file("num1")
        number_two = print_file("num2")
        if number_two == "":
            try:
                res = int(number_one)
            except:
                res = 0
        else:
            res = int(number_one) + int(number_two)
            write_into_file("res",str(res))
            write_into_file("num1",str(res))
            write_into_file("num2","")
            
    if op == "-":
        number_one = print_file("num1")
        number_two = print_file("num2")
        if number_two == "":
            try:
                res = int(number_one)
            except:
                res = 0
        else:
            res = int(number_one) - int(number_two)
            write_into_file("res",str(res))
            write_into_file("num1",str(res))
            write_into_file("num2","")
    if op == "*":
        number_one = print_file("num1")
        number_two = print_file("num2")
        if number_two == "":
            try:
                res = int(number_one)
            except:
                res = 0
        else:
            res = int(number_one) * int(number_two)
            write_into_file("res",str(res))
            write_into_file("num1",str(res))
            write_into_file("num2","")
    if op == "/":
        number_one = print_file("num1")
        number_two = print_file("num2")
        if number_two == "":
            try:
                res = int(number_one)
            except:
                res = 0
        else:
            res = int(number_one) / int(number_two)
            write_into_file("res",str(int(res)))
            write_into_file("num1",str(res))
            write_into_file("num2","")
    if op == "":
        write_into_file("res",r)
    print(res,number_one,number_two)
    
def which_button(b,display_res):
    button_pressed = print_file("bpress")
    number_of_button_pressed = int(button_pressed)
    number_one = print_file("num1")
    number_two = print_file("num2")
    op = print_file("op")
    calc_res(number_one,op,number_two)
    if b == "0":
        write_num("7")
    elif b == "1":
        write_num("8")
    elif b == "2":
        write_num("9")
    elif b == "3":
        write_into_file("op","/")
        number_of_button_pressed = number_of_button_pressed + 1
        write_into_file("bpress",str(number_of_button_pressed))
        write_into_file("check","op")

    elif b == "4":
        write_num("4")
    elif b == "5":
        write_num("5")
    elif b == "6":
        write_num("6")
    elif b == "7":
        write_into_file("op","*")
        number_of_button_pressed = number_of_button_pressed + 1
        write_into_file("bpress",str(number_of_button_pressed))
        write_into_file("check","op")

    elif b == "8":
        write_num("1")
    elif b == "9":
        write_num("2")
    elif b == "10":
        write_num("3")
    elif b == "11":
        write_into_file("op","-")
        number_of_button_pressed = number_of_button_pressed + 1
        write_into_file("bpress",str(number_of_button_pressed))
        write_into_file("check","op")

    elif b == "12":
        write_num("0")
    elif b == "13":
        write_into_file("num1","")
        write_into_file("num2","")
        write_into_file("bpress","0")
    elif b == "14":
        write_into_file("op","+")
        number_of_button_pressed = number_of_button_pressed + 1
        write_into_file("bpress",str(number_of_button_pressed))
        write_into_file("check","num")

    elif b == "15":
        print("=")
        number_of_button_pressed = number_of_button_pressed + 1
        write_into_file("bpress",str(number_of_button_pressed))
        write_into_file("check","op")

    if number_of_button_pressed == 0:
        r = print_file("num1")
    elif number_of_button_pressed == 1:
        r = print_file("num2")    
    else:
        r = print_file("res")
    display_res["text"] = r

def size_1():
   text.config(font=('Helvatical bold',20))

write_into_file("check","num")
write_into_file("num1","")
write_into_file("num2","")
write_into_file("op","")
write_into_file("bpress","0")
num_to_display = print_file("num1")
posx = 0
posy = 50
button_list = []
px = []
py = []
res = 0
button_name = ["7","8","9","/","4","5","6","x","1","2","3","-","0","C","+","="]
color_list = ["grey","grey","grey","brown","grey","grey","grey","brown","grey","grey","grey","brown","grey","yellow","brown","orange"]
for i in range(16):
    posx = posx + 50
    if i % 4 == 0:
        if i > 0:
            posy = posy + 50
        posx = 0
    px.append(posx)
    py.append(posy)


display_res = tkinter.Label(text=num_to_display,fg="blue")
display_res.grid()

for i in range(16):
    button_list.append(" ")
for i in range(len(button_list)):
    button_list[i] = Button(app, text=button_name[i],bg=color_list[i], fg="white",
                command=lambda m=str(i): which_button(m,display_res))

    button_list[i].place(x=px[i], y=py[i])
    
app.geometry("200x250")
app.mainloop()
