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

def write_id(path,x):
    f = open(path, "w")
    f.write(str(x))
    f.close

def wwrite_id(path,x):
    f = open(path, "w")
    f.write(str(x))
    f.close

def check_file():
    n1 = print_file("num1")
    n2 = print_file("num2")
    if n1 != "" and n2 != "":
        return (1)
    else:
        return (0)

def write_num(x):
    n1 = print_file("num1")
    n2 = print_file("num2")
    res = print_file("res")
    if x == -1:
        write_id("num1","")
        write_id("num2","")
    if x != -1:
        if n1 != "" and n2 != "":
            write_id("num1",res)
            write_id("num2",x)
        elif n1 == "" and n2 == "":
            write_id("num1",x)
        elif n1 != "" and n2 == "":
            write_id("num2",x)
        
def calc_res(n1,op,n2):
    res = 0
    if n1 == "" and op == "+" or op == "-":
        n1 = "0"
    if n2 == "" and op == "+" or op == "-":
        n2 = "0"
    
    if n1 == "" and op == "*":
        n1 = "1"
    if n2 == "" and op == "*":
        n2 = "1"
    
    if op == "+":
        res = int(n1) + int(n2)
        write_id("res",str(res))
        print(res)
    if op == "-":
        res = int(n1) - int(n2)
        write_id("res",str(res))
        print(res)
    if op == "*":
        res = int(n1) * int(n2)
        write_id("res",str(res))
        print(res,n1,n2)   
    if op == "/":
        n1 = print_file("num1")
        n2 = print_file("num2")
        if n2 == "":
            res = int(n1)
        else:
            res = int(n1) / int(n2)
        write_id("res",str(int(res)))
        print(res,n1,n2)   
# Create a function with one parameter, i.e., of
# the text you want to show when button is clicked
def which_button(b,display_res):
    bp = print_file("bpress")
    bpp = int(bp)
    n1 = print_file("num1")
    n2 = print_file("num2")
    op = print_file("op")
    calc_res(n1,op,n2)
    if b == "0":
        write_num("7")
    elif b == "1":
        write_num("8")
    elif b == "2":
        write_num("9")
    elif b == "3":
        write_id("op","/")
        bpp = bpp + 1
        write_id("bpress",str(bpp))
    elif b == "4":
        write_num("4")
    elif b == "5":
        write_num("5")
    elif b == "6":
        write_num("6")
    elif b == "7":
        write_id("op","*")
        bpp = bpp + 1
        write_id("bpress",str(bpp))
    elif b == "8":
        write_num("1")
    elif b == "9":
        write_num("2")
    elif b == "10":
        write_num("3")
    elif b == "11":
        write_id("op","-")
        bpp = bpp + 1
        write_id("bpress",str(bpp))
    elif b == "12":
        write_num("0")
    elif b == "13":
        write_id("num1","")
        write_id("num2","")
        write_id("bpress","0")
    elif b == "14":
        write_id("op","+")
        bpp = bpp + 1
        write_id("bpress",str(bpp))
    elif b == "15":
        print("=")
        bpp = bpp + 1
        write_id("bpress",str(bpp))
    if bpp == 0:
        r = print_file("num1")
    elif bpp == 1:
        r = print_file("num2")    
    else:
        r = print_file("res")
    display_res["text"] = r
    
    

write_id("num1","")
write_id("num2","")
write_id("op","")
write_id("bpress","0")
num_to_display = print_file("num1")
posx = 0
posy = 50
but = []
px = []
py = []
res = 0
button_name = ["7","8","9","/","4","5","6","x","1","2","3","-","0","C","+","="]
for i in range(16):
    posx = posx + 50
    if i % 4 == 0:
        if i > 0:
            posy = posy + 50
        posx = 0
    px.append(posx)
    py.append(posy)


display_res = tkinter.Label(text=num_to_display,width=0,height=0)
display_res.grid()

for i in range(16):
    but.append(" ")
for i in range(len(but)):
    but[i] = Button(app, text=button_name[i],
                command=lambda m=str(i): which_button(m,display_res))

    but[i].place(x=px[i], y=py[i])
    
app.geometry("200x250")
app.mainloop()
