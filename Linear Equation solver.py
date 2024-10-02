from tkinter import *
import numpy as np
from tkinter import ttk
from tkinter import messagebox
root=Tk()

root.config(background="#C9F7F3")
root.title("LINEAR EQUATION")
root.maxsize(height=500,width=500)
root.minsize(height=500,width=500)
a11m=StringVar()
a12m=StringVar()
a13m=StringVar()
a21m=StringVar()
a22m=StringVar()
a23m=StringVar()
a31m=StringVar()
a32m=StringVar()
a33m=StringVar()
b11m=StringVar()
b21m=StringVar()
b31m=StringVar()

title=Label(root,text="LINEAR EQUATION IN THREE VARIABLES", font=("Berlin Sans FB Demi",18),bg="#C11B17",fg="white",bd=10,padx=200).pack()
lebel1=Label(root,text="For the First Equation : ", font=("Arial Rounded MT Bold",15),fg="black",bg="Yellow").place(x=1,y=55)
entry1=Entry(root,bd=2,width=8,highlightthickness=2,highlightcolor= "black",textvariable=a11m)
entry1.place(x=1,y=95)
lebel2=Label(root,text="x  + ", font=("Script MT Bold",15),fg="black",bg="#C9F7F3").place(x=60,y=90)
entry2=Entry(root,bd=2,width=8,highlightthickness=2,highlightcolor= "black",textvariable=a12m)
entry2.place(x=100,y=95)
lebel2=Label(root,text="y  + ", font=("Script MT Bold",15),fg="black",bg="#C9F7F3").place(x=160,y=90)
entry3=Entry(root,bd=2,width=8,highlightthickness=2,highlightcolor= "black",textvariable=a13m)
entry3.place(x=200,y=95)
lebel2=Label(root,text="z  = ", font=("Script MT Bold",15),fg="black",bg="#C9F7F3").place(x=265,y=90)
entry4=Entry(root,bd=2,width=8,highlightthickness=2,highlightcolor= "black",textvariable=b11m)
entry4.place(x=300,y=95)
######
lebel1=Label(root,text="For the Second Equation : ", font=("Arial Rounded MT Bold",15),fg="black",bg="Yellow").place(x=1,y=150)
entry5=Entry(root,bd=2,width=8,highlightthickness=2,highlightcolor= "black",textvariable=a21m)
entry5.place(x=1,y=190)
lebel2=Label(root,text="x  + ", font=("Script MT Bold",15),fg="black",bg="#C9F7F3").place(x=65,y=187)
entry6=Entry(root,bd=2,width=8,highlightthickness=2,highlightcolor= "black",textvariable=a22m)
entry6.place(x=100,y=190)
lebel2=Label(root,text="y  + ", font=("Script MT Bold",15),fg="black",bg="#C9F7F3").place(x=160,y=187)
entry7=Entry(root,bd=2,width=8,highlightthickness=2,highlightcolor= "black",textvariable=a23m)
entry7.place(x=200,y=190)
lebel2=Label(root,text="z  = ", font=("Script MT Bold",15),fg="black",bg="#C9F7F3").place(x=260,y=187)
entry8=Entry(root,bd=2,width=8,highlightthickness=2,highlightcolor= "black",textvariable=b21m)
entry8.place(x=300,y=190)
#####
######
lebel1=Label(root,text="For the Third Equation : ", font=("Arial Rounded MT Bold",15),fg="black",bg="Yellow").place(x=1,y=230)
entry9=Entry(root,bd=2,width=8,highlightthickness=2,highlightcolor= "black",textvariable=a31m)
entry9.place(x=1,y=270)
lebel2=Label(root,text="x  + ", font=("Script MT Bold",15),fg="black",bg="#C9F7F3").place(x=65,y=268)
entry10=Entry(root,bd=2,width=8,highlightthickness=2,highlightcolor= "black",textvariable=a32m)
entry10.place(x=100,y=270)
lebel2=Label(root,text="y  + ", font=("Script MT Bold",15),fg="black",bg="#C9F7F3").place(x=160,y=268)
entry11=Entry(root,bd=2,width=8,highlightthickness=2,highlightcolor= "black",textvariable=a33m)
entry11.place(x=200,y=270)
lebel2=Label(root,text="z  = ", font=("Script MT Bold",15),fg="black",bg="#C9F7F3").place(x=260,y=268)
entry12=Entry(root,bd=2,width=8,highlightthickness=2,highlightcolor= "black",textvariable=b31m)
entry12.place(x=300,y=270)
######
Label(root,text="x = ", font=("Script MT Bold",20),fg="black",bg="#C9F7F3").place(x=1,y=350)
Label(root,text="y = ", font=("Script MT Bold",20),fg="black",bg="#C9F7F3").place(x=1,y=400)
Label(root,text="z = ", font=("Script MT Bold",20),fg="black",bg="#C9F7F3").place(x=1,y=450)
xvalue=Label(root,text="         ", font=("Arial Rounded MT Bold",20),fg="black",bg="white")
xvalue.place(x=50,y=350)
yvalue=Label(root,text="         ", font=("Arial Rounded MT Bold",20),fg="black",bg="white")
yvalue.place(x=50,y=400)
zvalue=Label(root,text="         ", font=("Arial Rounded MT Bold",20),fg="black",bg="white")
zvalue.place(x=50,y=450)
def calculate():
    a11=float(a11m.get())
    a12=float(a12m.get())
    a13=float(a13m.get())
    a21=float(a21m.get())
    a22=float(a22m.get())
    a23=float(a23m.get())
    a31=float(a31m.get())
    a32=float(a32m.get())
    a33=float(a33m.get())
    b11=float(b11m.get())
    b21=float(b21m.get())
    b31=float(b31m.get())
    mat1=np.array([[a11,a12,a13],[a21,a22,a23],[a31,a32,a33]])
    mat2=np.array([[b11],[b21],[b31]])
    print("First matrix  ",mat1)
    print("Second matrix  ",mat2)
    A11=(a22*a33)-(a23*a32)
    A12=(a21*a33)-(a23*a31)
    A13=(a21*a32)-(a22*a31)
    det=(a11*A11)-(a12*A12)+(a13*A13)
    print("DEterminant ",det)
    if det!=0:
        print("Unique solution ")
        ainverse=np.linalg.inv(mat1)
        print("A inverse",ainverse)
        sol=np.matmul(ainverse,mat2)
        print("solution",sol)
        print(round(sol[0,0],3))
        print(round(sol[1,0],3))
        print(round(sol[2,0],3))
        xvalue.config(text=round(sol[0,0],3))
        yvalue.config(text=round(sol[1,0],3))
        zvalue.config(text=round(sol[2,0],3))
    if det==0:
        A11=(a22*a33)-(a23*a32)
        A12=(a21*a33)-(a23*a31)
        A13=(a21*a32)-(a22*a31)
        A21=(a12*a33)-(a13*a32)
        A22=(a11*a33)-(a13*a31)
        A23=(a11*a32)-(a12*a31)
        A31=(a12*a23)-(a13*a22)
        A32=(a11*a23)-(a13*a21)
        A33=(a11*a22)-(a12*a21)
        adjointA=np.array([[A11,-A21,A31],[-A12,A22,-A32],[A13,-A32,A33]])
        check=np.matmul(adjointA,mat2)
        zero=np.array([[0],[0],[0]])
        if np.array_equal(check,zero):
            messagebox.showerror("NOT UNIQUE SOLUTION","This system of equation has Infinite solution")
        else:
            messagebox.showerror("NOT UNIQUE SOLUTION","This system of equation has no solution")

def clean1():
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    entry4.delete(0,END)
def clean2():
    entry5.delete(0,END)
    entry6.delete(0,END)
    entry7.delete(0,END)
    entry8.delete(0,END)
def clean3():
    entry9.delete(0,END)
    entry10.delete(0,END)
    entry11.delete(0,END)
    entry12.delete(0,END)


cal=Button(root,text="Calculate",bg="red",fg="White",font=("Arial Black",10),command=calculate)
cal.place(x=200,y=300)
clean1=Button(root,text="Clean",bg="#05550E",fg="White",font=("Courier New",10),command=clean1)
clean1.place(x=400,y=90)
clean1=Button(root,text="Clean",bg="#05550E",fg="White",font=("Courier New",10),command=clean2)
clean1.place(x=400,y=187)
clean1=Button(root,text="Clean",bg="#05550E",fg="White",font=("Courier New",10),command=clean3)
clean1.place(x=400,y=268)
root.mainloop()
