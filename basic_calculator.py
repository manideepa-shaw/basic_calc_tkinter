from tkinter import *
import pyinputplus as p
root=Tk()
root.title("Basic Calculator")

e=Entry(root,width=35,borderwidth=5)

e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

def butt_click(num):
    curr=e.get()
    e.delete(0,END)
    e.insert(0,str(curr)+str(num))

def clear():
    e.delete(0,END)

def butt_add():
    global firstnum
    global math
    math = "add"
    firstnum=e.get()
    e.delete(0,END)

def butt_sub():
    global firstnum
    global math
    math = "sub"
    firstnum=e.get()
    e.delete(0,END)

def butt_multi():
    global firstnum
    global math
    math = "multi"
    firstnum=e.get()
    e.delete(0,END)

def butt_div():
    global firstnum
    global math
    math = "div"
    firstnum=e.get()
    e.delete(0,END)

def equal():
    secondnum=e.get()
    e.delete(0,END)
    if math == "add":
        e.insert(0,int(firstnum) + int(secondnum))
    elif math== "sub":
        e.insert(0, int(firstnum) - int(secondnum))
    elif math == "multi":
        e.insert(0, int(firstnum) * int(secondnum))
    elif math == "div":
        e.insert(0, int(firstnum) / int(secondnum))

butt1=Button(root,text=1,padx=40,pady=20,command=lambda : butt_click(1))
butt1.grid(row=1,column=0)
butt2=Button(root,text=2,padx=40,pady=20,command=lambda : butt_click(2))
butt2.grid(row=1,column=1)
butt3=Button(root,text=3,padx=40,pady=20,command=lambda : butt_click(3))
butt3.grid(row=1,column=2)
butt4=Button(root,text=4,padx=40,pady=20,command=lambda : butt_click(4))
butt4.grid(row=2,column=0)
butt5=Button(root,text=5,padx=40,pady=20,command=lambda : butt_click(5))
butt5.grid(row=2,column=1)
butt6=Button(root,text=6,padx=40,pady=20,command=lambda : butt_click(6))
butt6.grid(row=2,column=2)
butt7=Button(root,text=7,padx=40,pady=20,command=lambda : butt_click(7))
butt7.grid(row=3,column=0)
butt8=Button(root,text=8,padx=40,pady=20,command=lambda : butt_click(8))
butt8.grid(row=3,column=1)
butt9=Button(root,text=9,padx=40,pady=20,command=lambda : butt_click(9))
butt9.grid(row=3,column=2)
butt10=Button(root,text=0,padx=40,pady=20,command=lambda : butt_click(0))
butt10.grid(row=3,column=3)

b1=Button(root,text="+",font=10,padx=35,pady=15,command=butt_add)
b1.grid(row=4,column=0)
b2=Button(root,text="-",font=10,padx=35,pady=15,command=butt_sub)
b2.grid(row=4,column=1)
b3=Button(root,text="*",font=10,padx=35,pady=15,command=butt_multi)
b3.grid(row=4,column=2)
b4=Button(root,text="/",font=10,padx=35,pady=15,command=butt_div)
b4.grid(row=4,column=3)

b5=Button(root,text="=",padx=40,pady=20,command=equal)
b5.grid(row=1,column=3)
b6=Button(root,text="Clear",font=8,padx=25,pady=15,command=clear)
b6.grid(row=2,column=3)

mainloop()
