from ast import operator
from multiprocessing.sharedctypes import Value
import string
from tkinter import*
import tkinter
from tkinter import messagebox

root =Tk()

val=""
A=0

def btn_1clicked():
 global val
 val=val+"1"
 data.set(val) #it will link the variable which is pressed by the user to the val and then it will concatinate it

def btn_2clicked():
    global val
    val=val+"2" 
    data.set(val)

def btn_3clicked():
 global val
 val=val+"3"
 data.set(val)   

def btn_4clicked():
 global val
 val=val+"4"
 data.set(val) 

def btn_5clicked():
 global val
 val=val+"5"
 data.set(val)  
         

def btn_6clicked():
 global val
 val=val+"6"
 data.set(val)  

def btn_7clicked():
 global val
 val=val+"7"
 data.set(val)  

def btn_8clicked():
 global val
 val=val+"8"
 data.set(val) 

def btn_9clicked():
 global val
 val=val+"9"
 data.set(val) 

def btn_0clicked():
 global val
 val=val+"0"
 data.set(val) 
 
def btn_plusclicked():
 global val
 global A
 global operator
 operator="+"
 A=int(val) #the value of val is made integer and then stored in A
 val=val + "+"
 data.set(val) 

def btn_minusclicked():
 global val
 global A
 global operator
 operator="-"
 A=int(val)
 val=val+"-"
 data.set(val) 

def btn_mulclicked():
 global val
 global A
 global operator
 operator="*"
 A=int(val)
 val=val+"*"
 data.set(val) 

def btn_eqclicked():
 global val
 global A
 global operator
 val2=val #we are transfering all the values of val into val2
 if operator == "+":
        x=int(val2.split("+")[1])
        c=A+x
        data.set(c)      
        val=str(c)
 elif operator=="*":
        x=int(val2.split("*")[1])
        c=A*x
        data.set(c)      
        val=str(c)
 elif operator=="-":
        x=int(val2.split("-")[1])
        c=A-x
        data.set(c)      
        val=str(c)   
 elif operator=="/":
        x=int(val2.split("/")[1])
        c=A/x
        data.set(c)      
        val=str(c)   
           
        if x==0:
            messagebox.showerror("Error","Division By 0 not supported")
            A=""
            val=""
            data.set(val)
        else:
            c=int(A/x)
            data.set(c)
            val=str(c)    
            
        


def btn_slclicked():
 global val
 global A
 global operator
 operator="/"
 A=int(val)
 val=val+"/"
 data.set(val) 

def btn_clclicked():
 global val
 global A
 global operator
 operator=""
 A=""
 val=""
 data.set(val) 

root.title("Calculator app")
root.geometry("300x400+300+300") #creates dimansions and opens approx in centre because of 300+300 Values
root.resizable(0,0) #(0,0) means that it cannot be resized 


data=StringVar()#it is used for storing the values as a string in data variable
lbl=Label(
    root,
    text="Label",
    anchor=SE, #it tells in which direction the text will display(eg-South east as SE)
    font=("verdana",50),
    background="#ffffff",
    fg="#000000",
    textvariable=data #it holds the value which is displayed in label
)
lbl.pack(expand=TRUE,fill="both")


row1=Frame(root) #it creates frame inside parent root
row1.pack(expand=True,fill="both") #it packs the elements functionality inside the row1

row2=Frame(root)
row2.pack(expand=True,fill="both") #here fill both defines that if we maximize windows then automatically elements inside it will fill in both x and y direction

row3=Frame(root)
row3.pack(expand=True,fill="both")

row4=Frame(root)
row4.pack(expand=True,fill="both")



#designing buttons

button1=Button(
row1,
text="1",
font=("Verdana",22),
relief=GROOVE,
border=0,
command=btn_1clicked
)
button1.pack(side=LEFT,expand=True,fill="both")


button2=Button(
row1,
text="2",
font=("Verdana",22),
relief=GROOVE,
border=0,
command=btn_2clicked,
)
button2.pack(side=LEFT,expand=True,fill="both")


button3=Button(
row1,
text="3",
font=("Verdana",22),
relief=GROOVE,
border=0,
command=btn_3clicked
)
button3.pack(side=LEFT,expand=True,fill="both")


buttonplus=Button(
row1,
text="+",
font=("Verdana",20),
relief=GROOVE,
border=0,
command=btn_plusclicked,
)
buttonplus.pack(side=LEFT,expand=True,fill="both")


button4=Button(
row2,
text="4",
font=("Verdana",22),
relief=GROOVE,
border=0,
command=btn_4clicked
)
button4.pack(side=LEFT,expand=True,fill="both")


button5=Button(
row2,
text="5",
font=("Verdana",22),
relief=GROOVE,
border=0,
command=btn_5clicked
)
button5.pack(side=LEFT,expand=True,fill="both")


button6=Button(
row2,
text="6",
font=("Verdana",22),
relief=GROOVE,
border=0,
command=btn_6clicked
)
button6.pack(side=LEFT,expand=True,fill="both")


buttonminus=Button(
row2,
text="-",
font=("Verdana",25),
relief=GROOVE,
border=0,
command=btn_minusclicked,
)
buttonminus.pack(side=LEFT,expand=True,fill="both")


button7=Button(
row3,
text="7",
font=("Verdana",22),
relief=GROOVE,
border=0,
command=btn_7clicked
)
button7.pack(side=LEFT,expand=True,fill="both")


button8=Button(
row3,
text="8",
font=("Verdana",22),
relief=GROOVE,
border=0,
command=btn_8clicked
)
button8.pack(side=LEFT,expand=True,fill="both")


button9=Button(
row3,
text="9",
font=("Verdana",22),
relief=GROOVE,
border=0,
command=btn_9clicked
)
button9.pack(side=LEFT,expand=True,fill="both")


buttonmultiply=Button(
row3,
text="*",
font=("Verdana",22),
relief=GROOVE,
border=0,
command=btn_mulclicked
)
buttonmultiply.pack(side=LEFT,expand=True,fill="both")


buttoncl=Button(
row4,
text="C",
font=("Verdana",22),
relief=GROOVE,
border=0,
command=btn_clclicked
)
buttoncl.pack(side=LEFT,expand=True,fill="both")


button0=Button(
row4,
text="0",
font=("Verdana",22),
relief=GROOVE,
border=0,
command=btn_0clicked,
)
button0.pack(side=LEFT,expand=True,fill="both")


buttonequal=Button(
row4,
text="=",
font=("Verdana",22),
relief=GROOVE,
border=0,
command=btn_eqclicked
)
buttonequal.pack(side=LEFT,expand=True,fill="both")


buttonsl=Button(
row4,
text="/",
font=("Verdana",22),
relief=GROOVE,
border=0,
command=btn_slclicked,
)
buttonsl.pack(side=LEFT,expand=True,fill="both")


root.mainloop()


