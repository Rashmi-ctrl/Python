from tkinter import *

root = Tk()
root.title('CALCULATOR')

e = Entry(root, width=35, borderwidth=10)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10 )

def button_add(number):
    present = e.get()
    e.delete(0, END)
    e.insert(0, str(present)+str(number))

def button_clear():
    e.delete(0, END)
    
def button_addition():
    fnum = e.get()
    global first
    global math
    math= "addition"
    first = int(fnum)
    e.delete(0, END)
   

def button_sub():
    fnum = e.get()
    global first
    global math
    math= "subtraction"
    first = int(fnum)
    e.delete(0, END)

def button_equal():
    secondnum =e.get()
    e.delete(0, END)
    if math=="addition":
        e.insert(0, first+int(secondnum))

    elif math=="subtraction":
        e.insert(0, first-int(secondnum))

    elif math=="division":
        e.insert(0, first/int(secondnum))

    else:
        e.insert(0, first*int(secondnum))   

def button_divide():
    fnum = e.get()
    global first
    global math
    math= "division"
    first = int(fnum)
    e.delete(0, END)

def button_multi():
    fnum = e.get()
    global first
    global math
    math= "multiplication"
    first = int(fnum)
    e.delete(0, END)
    

b1= Button(root, text='1', padx=40, pady=20, command=lambda:button_add(1))
b2= Button(root, text='2', padx=40, pady=20, command=lambda:button_add(2))
b3= Button(root, text='3', padx=40, pady=20, command=lambda:button_add(3))
b4= Button(root, text='4', padx=40, pady=20, command=lambda:button_add(4))
b5= Button(root, text='5', padx=40, pady=20, command=lambda:button_add(5))
b6= Button(root, text='6', padx=40, pady=20, command=lambda:button_add(6))
b7= Button(root, text='7', padx=40, pady=20, command=lambda:button_add(7))
b8= Button(root, text='8', padx=40, pady=20, command=lambda:button_add(8))
b9= Button(root, text='9', padx=40, pady=20, command=lambda:button_add(9))
b0= Button(root, text='0', padx=40, pady=20, command=lambda:button_add(0))
badd= Button(root, text='+', padx=50, pady=20, command=button_addition)
bsub= Button(root, text='-', padx=50, pady=20, command=button_sub)
bmulti= Button(root, text='*', padx=50, pady=20, command=button_multi)
bdiv= Button(root, text='/', padx=50, pady=20, command=button_divide)
bequal= Button(root, text='=', padx=40, pady=20, command=button_equal)
bclear= Button(root, text='CE', padx=40, pady=20, command=button_clear)

b1.grid(row=3 , column=1)
b2.grid(row=3 , column=2)
b3.grid(row=3 , column=3)

b4.grid(row=2 , column=1)
b5.grid(row=2 , column=2)
b6.grid(row=2 , column=3)

b7.grid(row=1 , column=1)
b8.grid(row=1 , column=2)
b9.grid(row=1 , column=3)

b0.grid(row=4 , column=2)
bclear.grid(row=4, column=1)
badd.grid(row=1, column=4)
bsub.grid(row=2, column=4)
bmulti.grid(row=3, column=4)
bdiv.grid(row=4, column=4)
bequal.grid(row=4, column=3)



root.mainloop()
    
