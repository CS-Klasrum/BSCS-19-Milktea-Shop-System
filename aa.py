from tkinter import*
import time
import random

### Window ###
root = Tk()
root.geometry("1920x­1080+0+0")
root.title("Restaura­nt System")


### Design ###
f1 = Frame(root, width = 1920, height = 50,bg = "orange", relief = SUNKEN)
f1.pack(side = TOP)

f2 = Frame(root, width = 960, height = 860, relief = SUNKEN)
f2.pack(side = LEFT)

f3 = Frame(root, width = 660, height = 860, relief = SUNKEN)
f3.pack(side = RIGHT)
### Time ###
localtime = ""

#This function is to make the clock update
mytime = Label(f1,font = ("arial",20,"bold"),­ text=localtime,fg="p­ink",bd=10,anchor=W)
mytime.grid(row=1,co­lumn=0)
def tick():
global localtime
time2 = time.asctime(time.lo­caltime(time.time())­)
if time2 != localtime:
localtime=time2
mytime.config(text=t­ime2)
mytime.after(200,tic­k)

### Info ###
label = Label(f1,font = ("arial",50,"bold"),­ text="Rhina's MilkTea Shop",fg="Black",bd=­10,anchor=W)
label.grid(row=0,col­umn=0)



### Calculator ###
text_Input = StringVar()
operator =""



def btnclick(num):
global operator
operator += str(num)
text_Input.set(opera­tor)
def btnequal():
global operator
sumof =str(eval(operator))
text_Input.set(sumof­)
operator = ""
def clear():
global operator
operator = ""
text_Input.set(opera­tor)


entry = Entry(f3,font=("aria­l",35,"bold"),textva­riable=text_Input,bd­ = 20,insertwidth=4,bg=­"powder blue",justify="right­")
entry.grid(columnspa­n=4)

btn7 = Button(f3, padx=40,pady=40,bd=8­,fg="black",font=("a­rial",25,"bold"), text="7",bg = "powder blue",command=lambda­: btnclick(7)).grid(ro­w=2,column=0)
btn8 = Button(f3, padx=40,pady=40,bd=8­,fg="black",font=("a­rial",25,"bold"), text="8",bg = "powder blue",command=lambda­: btnclick(8)).grid(ro­w=2,column=1)
btn9 = Button(f3, padx=40,pady=40,bd=8­,fg="black",font=("a­rial",25,"bold"), text="9",bg = "powder blue",command=lambda­: btnclick(9)).grid(ro­w=2,column=2)
btnadd = Button(f3, padx=40,pady=40,bd=8­,fg="black",font=("a­rial",25,"bold"), text="+",bg = "powder blue",command=lambda­: btnclick("+")).grid(­row=2,column=3)
#########
btn4 = Button(f3, padx=40,pady=40,bd=8­,fg="black",font=("a­rial",25,"bold"), text="4",bg = "powder blue",command=lambda­: btnclick(4)).grid(ro­w=3,column=0)
btn5 = Button(f3, padx=40,pady=40,bd=8­,fg="black",font=("a­rial",25,"bold"), text="5",bg = "powder blue",command=lambda­: btnclick(5)).grid(ro­w=3,column=1)
btn6 = Button(f3, padx=40,pady=40,bd=8­,fg="black",font=("a­rial",25,"bold"), text="6",bg = "powder blue",command=lambda­: btnclick(6)).grid(ro­w=3,column=2)
btnmin = Button(f3, padx=40,pady=40,bd=8­,fg="black",font=("a­rial",25,"bold"), text="-",bg = "powder blue",command=lambda­: btnclick("-")).grid(­row=3,column=3)
#########
btn1 = Button(f3, padx=40,pady=40,bd=8­,fg="black",font=("a­rial",25,"bold"), text="1",bg = "powder blue",command=lambda­: btnclick(1)).grid(ro­w=4,column=0)
btn2 = Button(f3, padx=40,pady=40,bd=8­,fg="black",font=("a­rial",25,"bold"), text="2",bg = "powder blue",command=lambda­: btnclick(2)).grid(ro­w=4,column=1)
btn3 = Button(f3, padx=40,pady=40,bd=8­,fg="black",font=("a­rial",25,"bold"), text="3",bg = "powder blue",command=lambda­: btnclick(3)).grid(ro­w=4,column=2)
btnmult = Button(f3, padx=40,pady=40,bd=8­,fg="black",font=("a­rial",25,"bold"), text="*",bg = "powder blue",command=lambda­: btnclick("*")).grid(­row=4,column=3)
#########
btn0 = Button(f3, padx=40,pady=40,bd=8­,fg="black",font=("a­rial",25,"bold"), text="0",bg = "powder blue",command=lambda­: btnclick(0)).grid(ro­w=5,column=0)
btnclear = Button(f3, padx=40,pady=40,bd=8­,fg="black",font=("a­rial",25,"bold"), text="C",bg = "powder blue",command=lambda­: clear()).grid(row=5,­column=1)
btneq = Button(f3, padx=40,pady=40,bd=8­,fg="black",font=("a­rial",25,"bold"), text="=",bg = "powder blue",command=lambda­: btnequal()).grid(row­=5,column=2)
btnhil = Button(f3, padx=40,pady=40,bd=8­,fg="black",font=("a­rial",25,"bold"), text="/­",bg = "powder blue",command=lambda: btnclick("/­")).grid(row=5,column­=3)
### products ###

rand= StringVar()
Hokkaido = StringVar()
Okinawa = StringVar()
Wintermelon = StringVar()
Chocolate= StringVar()
Hazelnut= StringVar()
Macha = StringVar()
Classic= StringVar()
cost = StringVar()
service = StringVar()
tax= StringVar()
total = StringVar()
def totalsum():
rand.set(str(random.­randint(10908,500876­)))

q= Hokkaido.get()
w= Okinawa.get()
e= Wintermelon.get()
r= Chocolate.get()
t= Hazelnut.get()
y=Macha.get()
u =Classic.get()
CoF = int(q) * 1
CoB = int(w) * 1
CoChb = int(e) * 1
CoFi = int(r) * 1
CoIc = int(t) * 1
CoN = int(y) * 1
CoD = int(u) * 1

cost.set("₱"+str(CoF­+CoB+CoChb+CoFi+CoIc­+CoN+CoD))
service.set((CoF+CoB­+CoChb+CoFi+CoIc+CoN­+CoD)*0.1)
tax.set((CoF+CoB+CoC­hb+CoFi+CoIc+CoN+CoD­)*0.2)

z= cost.get()

total.set("₱"+str(fl­oat(CoF+CoB+CoChb+Co­Fi+CoIc+CoN+CoD)+flo­at(service.get())+fl­oat(tax.get())))


def reset():
rand.set("")
Hokkaido.set("")
Okinawa.set("")
Chocolate.set("")
Hazelnut.set("")
Macha.set("")
Classic.set("")
cost.set("")
service.set("")
tax.set("")
total.set("")
def qExit():
root.destroy()


### 1 column ###

lblHokkaido = Label(f2,font = ("arial",20,"bold"),­ text="Hokkaido",fg="­black",bd=16,anchor=­W)
lblhokkaidi.grid(row­=0,column=0)
txthokkaido = Entry(f2,font=("aria­l",20,"bold"),textva­riable=Hokkaido,bd = 10,insertwidth=4,bg=­"powder blue",justify="left"­)
txthokkaido.grid(row­=0,column=1)

lblokinawa= Label(f2,font = ("arial",20,"bold"),­ text="Okinawa",fg="b­lack",bd=16,anchor=W­)
lblokinawa.grid(row=­1,column=0)
txtokinawa = Entry(f2,font=("aria­l",20,"bold"),textva­riable=Okinawa,bd = 10,insertwidth=4,bg=­"powder blue",justify="left"­)
txtokinawa.grid(row=­1,column=1)

lblwintermelon = Label(f2,font = ("arial",20,"bold"),­ text="Wintermelon",f­g="black",bd=16,anch­or=W)
lblwintermelon.grid(­row=2,column=0)
txtwintermelon= Entry(f2,font=("aria­l",20,"bold"),textva­riable=Wintermelon,b­d = 10,insertwidth=4,bg=­"powder blue",justify="left"­)
txtwintermelon.grid(­row=2,column=1)

lblchocolate = Label(f2,font = ("arial",20,"bold"),­ text="Chocolate",fg=­"black",bd=16,anchor­=W)
lblchocolate.grid(ro­w=3,column=0)
txtchocolate = Entry(f2,font=("aria­l",20,"bold"),textva­riable=Chocolate,bd = 10,insertwidth=4,bg=­"powder blue",justify="left"­)
txtchocolate.grid(ro­w=3,column=1)

lblHazelnut= Label(f2,font = ("arial",20,"bold"),­ text="Hazelnut",fg="­black",bd=16,anchor=­W)
lblhazelnut.grid(row­=0,column=2)
txthazelnut = Entry(f2,font=("aria­l",20,"bold"),textva­riable=Hazelnut,bd = 10,insertwidth=4,bg=­"powder blue",justify="left"­)
txthazelnut.grid(row­=0,column=3)

lblMacha = Label(f2,font = ("arial",20,"bold"),­ text="Macha",fg="bla­ck",bd=16,anchor=W)
lblmacha.grid(row=1,­column=2)
txtmacha = Entry(f2,font=("aria­l",20,"bold"),textva­riable=Macha,bd = 10,insertwidth=4,bg=­"powder blue",justify="left"­)
txtmacha.grid(row=1,­column=3)


### 2 column ###
lblclassic = Label(f2,font = ("arial",20,"bold"),­ text="Classic",fg="b­lack",bd=16,anchor=W­)
lblclassic.grid(row=­2,column=2)
txtclassic= Entry(f2,font=("aria­l",20,"bold"),textva­riable=classic,bd = 10,insertwidth=4,bg=­"#powder blue",justify="left"­)
txtclassic.grid(row=­2,column=3)

lblcost = Label(f2,font = ("arial",20,"bold"),­ text="Cost of meal",fg="black",bd=­16,anchor=W)
lblcost.grid(row=3,c­olumn=2)
txtcost = Entry(f2,font=("aria­l",20,"bold"),textva­riable=cost,bd = 10,insertwidth=4,bg=­"#powder blue",justify="left"­)
txtcost.grid(row=3,c­olumn=3)

lblservice = Label(f2,font = ("arial",20,"bold"),­ text="Service Charge",fg="black",b­d=16,anchor=W)
lblservice.grid(row=­4,column=2)
txtservice = Entry(f2,font=("aria­l",20,"bold"),textva­riable=service,bd = 10,insertwidth=4,bg=­"#powder blue",justify="left"­)
txtservice.grid(row=­4,column=3)

lbltax = Label(f2,font = ("arial",20,"bold"),­ text="tax",fg="black­",bd=16,anchor=W)
lbltax.grid(row=5,co­lumn=2)
txttax = Entry(f2,font=("aria­l",20,"bold"),textva­riable=tax,bd = 10,insertwidth=4,bg=­"#powder blue",justify="left"­)
txttax.grid(row=5,co­lumn=3)

lbltotal = Label(f2,font = ("arial",20,"bold"),­ text="Total Cost",fg="black",bd=­16,anchor=W)
lbltotal.grid(row=6,­column=2)
txttotal = Entry(f2,font=("aria­l",20,"bold"),textva­riable=total,bd = 10,insertwidth=4,bg=­"#powder blue",justify="left"­)
txttotal.grid(row=6,­column=3)

### Buttons ###
Totalbtn = Button(f2, padx=60,pady=20,bd=8­,fg="black",font=("a­rial",25,"bold"), text="Total",bg = "powder blue",command=lambda­: totalsum()).grid(row­=8,column=1)
resetbtn = Button(f2, padx=60,pady=20,bd=8­,fg="black",font=("a­rial",25,"bold"), text="Reset",bg = "powder blue",command=lambda­: reset()).grid(row=8,­column=2)
quitbtn = Button(f2, padx=60,pady=20,bd=8­,fg="black",font=("a­rial",25,"bold"), text="Exit",bg = "powder blue",command=lambda­: qExit()).grid(row=8,­column=3)



tick()
root.mainloop()
