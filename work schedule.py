from tkinter import*
from tkinter import messagebox as b
a=Tk()
a.title('working time')
a.geometry('400x300')
def process():
    name=en_1.get()
    age=int(en_2.get())
    degree=(Entry.get(en_3))
    Label(a,text=f'Hello{name}',font=('Times New Roman',16)).place(x=100,y=220)
    if degree=='ug' and age>=20 and age<=30:
        Label(a,text=f'working time 9a.m to 8p.m',font=('Times New Roman',16)).place(x=100,y=250)
    elif degree=='pg' and age>=20 and age<30:
        Label(a,text=f'working time 8p.m to 9a.m',font=('Times New Roman',16)).place(x=100,y=250)
    else:
        Label(a,text='not eligible',font=('Times New Roman',16)).palce(x=100,y=250)
Label(a,text='Working Time Prediction',font=('Times New Roman',16)).pack()
Label(a,text='name',font=('Times New Roman',16)).place(x=50,y=50)
Label(a,text='age',font=('Times New Roman',16)).place(x=50,y=90)
Label(a,text='ug or pg',font=('Times New Roman',16)).place(x=50,y=130)
en_1=Entry(a,font=('Arial Black',16),width=15)
en_1.place(x=150,y=50)
en_2=Entry(a,font=('Arial Black',16),width=15)
en_2.place(x=150,y=90)
en_3=Entry(a,font=('Arial Black',16),width=15)
en_3.place(x=150,y=130)
b=Button(a,text='submit',fg='green',command=process)
b.place(x=100,y=170)
a.mainloop()

