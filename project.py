from tkinter import *
window =Tk()

def weightconv():
    gm = float(e1_var.get()) * 1000
    pound = float(e1_var.get()) * 2.20462
    ounce = float(e1_var.get()) * 35.274
    t1.delete("1.0",END)
    t1.insert(END,gm)
    t2.delete("1.0",END)
    t2.insert(END,pound)
    t3.delete("1.0",END)
    t3.insert(END,ounce)

#t1.insert(END,km)

#b1= Button(window,text='kg')
#b1.grid(row=0,column=0,columnspan=2)
l11= Label(window,text='Title')
l11.grid(row=0,column=0)

e11_var = StringVar()
e11 = Entry(window,textvariable=e11_var)
e11.grid(row=0,column=1,columnspan=2)

l12= Label(window,text='Author')
l12.grid(row=0,column=3)

e12_var = StringVar()
e12 = Entry(window,textvariable=e12_var)
e12.grid(row=0,column=4,columnspan=2)

l21= Label(window,text='Year')
l21.grid(row=1,column=0)

e21_var = StringVar()
e21 = Entry(window,textvariable=e21_var)
e21.grid(row=1,column=1,columnspan=2)

l22= Label(window,text='ISBN')
l22.grid(row=1,column=3)

e22_var = StringVar()
e22 = Entry(window,textvariable=e22_var)
e22.grid(row=1,column=4,columnspan=2)

#b1= Button(window,text='View All',command=weightconv)
b3= Button(window,text='View All')
b3.grid(row=2,column=5)

b4= Button(window,text='Search Entry')
b4.grid(row=3,column=5)

b5= Button(window,text='Add Entry')
b5.grid(row=4,column=5)

b6= Button(window,text='Update Selected')
b6.grid(row=5,column=5)

b7= Button(window,text='Delete Selected')
b7.grid(row=6,column=5)

b8= Button(window,text='Close')
b8.grid(row=7,column=5)

t1=Text(window,height=7,width=30)
t1.grid(row=3,column=0)

window =  mainloop()