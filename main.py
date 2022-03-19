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


def make_list_from_op(op_l):
    op_list = []
    for i in range(len(op_l)):
        op_list.append(op_l[i])
    return (op_list)
def which_button(b,display_res):
    button_pressed = print_file("bpress")
    number_of_button_pressed = int(button_pressed)
    number_one = print_file("num1")
    number_two = print_file("num2")
    op = print_file("op")
    op_list = print_file("all_op")
    op_l = make_list_from_op(op_list)
    operant = "+*-/"
    digit = "0123456789"
    t = 0
    if len(op_l) > 2:
        if op_l[len(op_l) - 1] not in operant and op_l[len(op_l) - 2] not in operant and b in digit:
            t = 1
        else:
            calc_res(number_one,op,number_two)
    else:
        calc_res(number_one,op,number_two)    
    if b == "0":
        write_num("7")
        wwrite_into_file("all_op","7")
    elif b == "1":
        write_num("8")
        wwrite_into_file("all_op","8")
    elif b == "2":
        write_num("9")
        wwrite_into_file("all_op","9")
    elif b == "3":
        write_into_file("op","/")
        wwrite_into_file("all_op","/")
        number_of_button_pressed = number_of_button_pressed + 1
        write_into_file("bpress",str(number_of_button_pressed))
        write_into_file("check","op")

    elif b == "4":
        write_num("4")
        wwrite_into_file("all_op","4")
    elif b == "5":
        write_num("5")
        wwrite_into_file("all_op","5")
    elif b == "6":
        write_num("6")
        wwrite_into_file("all_op","6")
    elif b == "7":
        write_into_file("op","*")
        wwrite_into_file("all_op","7")
        number_of_button_pressed = number_of_button_pressed + 1
        write_into_file("bpress",str(number_of_button_pressed))
        write_into_file("check","op")

    elif b == "8":
        write_num("1")
        wwrite_into_file("all_op","1")
    elif b == "9":
        write_num("2")
        wwrite_into_file("all_op","2")
    elif b == "10":
        write_num("3")
        wwrite_into_file("all_op","3")
    elif b == "11":
        write_into_file("op","-")
        wwrite_into_file("all_op","-")
        number_of_button_pressed = number_of_button_pressed + 1
        write_into_file("bpress",str(number_of_button_pressed))
        write_into_file("check","op")

    elif b == "12":
        write_num("0")
        wwrite_into_file("all_op","0")
    elif b == "13":
        write_into_file("num1","")
        write_into_file("num2","")
        wwrite_into_file("all_op","")
        write_into_file("bpress","0")
    elif b == "14":
        print("=")
        number_of_button_pressed = number_of_button_pressed + 1
        write_into_file("bpress",str(number_of_button_pressed))
        write_into_file("check","op")
        wwrite_into_file("all_op","=")
    elif b == "15":
        write_into_file("op","+")
        number_of_button_pressed = number_of_button_pressed + 1
        write_into_file("bpress",str(number_of_button_pressed))
        write_into_file("check","num")
        wwrite_into_file("all_op","+")
    if number_of_button_pressed == 0:
        r = print_file("num1")
        write_into_file("res","0")
    elif number_of_button_pressed == 1:
        r = print_file("num2")    
    else:
        r = print_file("res")
    display_res["text"] = r

def size_1():
   text.config(font=('Helvatical bold',20))

l = []
write_into_file("all_op","")
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
button_name = ["7","8","9","/","4","5","6","x","1","2","3","-","0","C","=","+"]
color_list = ["grey","grey","grey","brown","grey","grey","grey","brown","grey","grey","grey","brown","grey","yellow","orange","brown"]
for i in range(16):
    posx = posx + 50
    if i % 4 == 0:
        if i > 0:
            posy = posy + 50
        posx = 0
    px.append(posx)
    py.append(posy)


display_res = tkinter.Label(text=num_to_display,width=0,height=0,fg="blue")
display_res.grid()

for i in range(16):
    button_list.append(" ")
for i in range(len(button_list)):
    button_list[i] = Button(app, text=button_name[i],bg=color_list[i], fg="white",
                command=lambda m=str(i): which_button(m,display_res))

    button_list[i].place(x=px[i], y=py[i])
app.geometry("200x250")
app.mainloop()
