import Admin
import student
import teacher
import parent
from tkinter import *

window = Tk()
window.geometry('1180x600')
window.title('Start Window')
def start():
    window = Toplevel()
    window.geometry('1180x600')
    Label(window, text='Login As', font='Times 20 bold').place(x=450,y=80)

    Button(window, text='Admin', command=Admin.start, width=25, font=("Times New", 10), bd=5,
           bg="light blue").place(x=450,y=120)#.grid(row=2, column=0, sticky=N + S + E + W)
    Button(window, text='Student', command=student.start, width=25, font=("Times New", 10), bd=5,
           bg="light blue").place(x=450,y=150)#.grid(row=3, column=0, sticky=N + S + E + W)
    Button(window, text='Parent', command=parent.start, width=25, font=("Times New", 10), bd=5,
           bg="light blue").place(x=450,y=180)#.grid(row=4, column=0, sticky=N + S + E + W)
    Button(window, text='Teacher', command=teacher.start, width=25, font=("Times New", 10), bd=5,
           bg="light blue").place(x=450,y=210)#.grid(row=5, column=0, sticky=N + S + E + W)

##############################################################################################
img=PhotoImage(file="background.png")
label=Label(window,image=img)
label.place(x=0,y=0)

Button(window, text='start', command=start, width=20, font=("Times New", 15),bd=-5,bg="light blue").place(x=410, y=290)
Label(window,text='E-SCHOOL',font=("Times New",60)).place(x=320,y=120)
window.mainloop()
