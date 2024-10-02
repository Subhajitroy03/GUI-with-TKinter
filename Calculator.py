from tkinter import *
win=Tk()
win.title("Calculator")
win.config(background="Black")

win.maxsize(width=300,height=300)
win.minsize(width=300,height=300)

def sum():
    a=float(e.get())
    b=float(e1.get())
    c=a+b
    l4.config(text=c)
def difference():
    a=float(e.get())
    b=float(e1.get())
    c=a-b
    l4.config(text=c)
def product():
    a=float(e.get())
    b=float(e1.get())
    c=a*b
    l4.config(text=c)
def division():
    a=float(e.get())
    b=float(e1.get())
    c=a/b
    l4.config(text=c)
def clean():
    e.delete(0,END)
    e1.delete(0,END)
    l4.config(text="")

l1=Label(win,text="Enter the first number : ",bg="green",fg="white",bd=5,font=("Arial Black",10))
l1.place(x=2,y=3)
l2=Label(win,text="Enter the second number : ",bg="red",fg="white",bd=5,font=("Arial Black",9))
l2.place(x=2,y=50)
s1=IntVar()
s2=IntVar()
e=Entry(win,bd=5,textvariable=s1)
e.place(x=200,y=3)
e1=Entry(win,bd=5,textvariable=s2)
e1.place(x=200,y=50)
b1=Button(win,text="+",bg="Maroon",fg="white",font=("Arial Black",15),padx=5,pady=3,command=sum)
b1.place(x=20,y=90)
b2=Button(win,text="-",bg="Maroon",fg="white",font=("Arial Black",15),padx=5,pady=3,command=difference)
b2.place(x=70,y=90)
b3=Button(win,text="X",bg="Maroon",fg="white",font=("Arial Black",15),padx=5,pady=3,command=product)
b3.place(x=120,y=90)
b4=Button(win,text="%",bg="Maroon",fg="white",font=("Arial Black",15),padx=5,pady=3,command=division)
b4.place(x=170,y=90)
l3=Label(win,text="Output: ",bg="yellow",fg="black",bd=5,font=("Arial Black",12))
l3.place(x=20,y=150)
l4=Label(win,text=" ",width=20,bg="white",fg="black",bd=10,font=("Arial Black",12))
l4.place(x=20,y=210)
b5=Button(win,text="CE",bg="Maroon",fg="white",font=("Arial Black",15),padx=5,pady=3,command=clean)
b5.place(x=230,y=90)
win.mainloop()