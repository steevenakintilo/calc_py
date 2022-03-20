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
    num_one_l = num_one_list()
    num_two_l = num_two_list()
    all_inp = print_file("inp")
    op_list = print_file("all_op")
    op_l = make_list_from_op(op_list)
    #print(all_inp,num_one_l)
    #print(int(all_inp)+1)
    operant = "+*-/"
    if len(op_l) > 0:
        last_op = op_l[len(op_l) - 1]
    else:
        last_op = 0
    if len(op_l) > 0:
        before_last_op = op_l[len(op_l) - 2]
    else:
        before_last_op = 0
    
    if len(op_l) > 0:
        if int(all_inp) in num_one_l:
            #print("Num 1 " + str(all_inp))
            wwrite_into_file("num1",x)
            
        elif int(all_inp) in num_two_l:
            #print("Num 2 " + str(all_inp))
            wwrite_into_file("window",x)
        #else:
            #print("Operant " + str(all_inp))
    write_into_file("check","num")
    number_one = print_file("num1")
    number_two = print_file("num2")
    res = print_file("res")
    check = print_file("check")
    if x == -1:
        write_into_file("num1","")
        write_into_file("num2","")
    if x != -1:
        if number_one != "" and number_two != "":
            #print("aaaaaaaaaaaa")
            if before_last_op in operant:
                print("ccacc")
                write_into_file("num1",res)
                write_into_file("num2",x)
            else:
                print("bBBBba")
                wwrite_into_file("num2",x)
        elif number_one == "" and number_two == "" and int(all_inp) not in num_two_l:
            print("bbbbbbbbbbbb")
            write_into_file("num1",x)
        elif number_one != "" and number_two == "" and int(all_inp) not in num_one_l:
            print("cccccccccccc")
            wwrite_into_file("num2",x)    
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
            res = int(int(number_one) / int(number_two))
            write_into_file("res",str(int(res)))
            write_into_file("num1",str(res))
            write_into_file("num2","")
    if op == "":
        write_into_file("res",r)
    #print(res,number_one,number_two)


def make_list_from_op(op_l):
    op_list = []
    for i in range(len(op_l)):
        op_list.append(op_l[i])
    return (op_list)

def num_one_list():
    l = []
    idx = 1
    for i in range(1,1000):
        l.append(idx)
        idx = idx + 4
    return (l)
    
def num_two_list():
    l = []
    idx = 2
    for i in range(1,1000):
        l.append(idx)
        idx = idx + 4
    return (l)
def which_button(b,display_res):
    list_one = num_one_list()
    list_two = num_two_list()
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
        write_into_file("window","300x300")
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
        wwrite_into_file("all_op","*")
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
        write_into_file("all_op","")
        write_into_file("bpress","0")
        write_into_file("inp","1")
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
    op_list = print_file("all_op")
    op_l = make_list_from_op(op_list)
    all_input = print_file("inp")
    int_input = int(all_input)
    if len(op_l) > 1 and (op_l[len(op_l) - 1] in digit and op_l[len(op_l) - 2] in operant):
        int_input = int_input + 1
        write_into_file("inp",str(int_input))
    if len(op_l) > 1 and (op_l[len(op_l) - 1] in operant and op_l[len(op_l) - 2] in digit):
        int_input = int_input + 1
        write_into_file("inp",str(int_input))
    if len(op_l) > 0:
        last_op = op_l[len(op_l) - 1]
    else:
        last_op = 0
    if number_of_button_pressed == 0:
        r = print_file("num1")
        write_into_file("res",r)
    elif number_of_button_pressed == 1:
        r = print_file("num2")    
    else:
        if str(last_op) in digit:
            r = last_op
        else:
            r = print_file("res")
    display_res["text"] = r

def size_1():
   text.config(font=('Helvatical bold',20))

l = []
write_into_file("inp","1")
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
a = print_file("window")
app.geometry("200x250")
app.mainloop()
