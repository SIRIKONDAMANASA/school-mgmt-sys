from tkinter.messagebox import *
import sqlite3

con = sqlite3.Connection('student_records.db')
cur = con.cursor()
con1 = sqlite3.Connection('teacher_records.db')
cur1 = con1.cursor()
from tkinter import *

def start():
    window = Toplevel()
    window.geometry('1180x600')
    window.title('Login Window')

    Label(window, text='Username  ', font=("Times New", 20)).grid(row=1, column=1)  # v=id
    v = Entry(window, width=25, font=("Times New", 18), bd=5, bg="light blue")
    v.grid(row=1, column=2)
    Label(window, text='Password  ', font=("Times n=New", 20)).grid(row=2, column=1)
    vv = Entry(window, show='*', width=25, font=("Times New", 18), bd=5, bg="light blue")  # vv=password
    vv.grid(row=2, column=2)



    def login():
        if (((int(v.get()) != 123) or (int(vv.get()) != 123))):
            showwarning('Login Failed', 'Incorrect Id Or Password Used Or ')
        else:
            menu = Toplevel()
            menu.geometry('1080x600')
            menu.title('Menu Window')

            l = Label(menu, text='Dashboard :', font='Times 20 bold')
            l.grid(row=0, column=0)

            Label(menu).grid(row=1, column=100, rowspan=30)
            def option1():

                    root = Toplevel()
                    root.geometry('1080x600')
                    root.title('Register Students Details')
                    l = Label(root, text='Register Student Details :', font='Times 20 bold')
                    l.grid(row=0, column=3)

                    l = Label(root, text=' ')
                    l.grid(row=1, column=0)

                    l = Label(root, text='Enter Student ID : ')
                    l.grid(row=2, column=0)

                    c = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light blue")  # c=sid
                    c.grid(row=2, column=1)

                    l = Label(root, text='Enter full name : ')
                    l.grid(row=3, column=0)
                    d = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light blue")  # d=fname
                    d.grid(row=3, column=1)
                    l = Label(root, text='Enter father name : ')
                    l.grid(row=4, column=0)
                    e = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light blue")  # e=fname
                    e.grid(row=4, column=1)
                    l = Label(root, text='Enter mother name : ')
                    l.grid(row=5, column=0)
                    g = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light blue")  # e=mname
                    g.grid(row=5, column=1)
                    l = Label(root, text='Enter class : ')
                    l.grid(row=6, column=0)

                    f = StringVar(root)  # f=class no.
                    f.set("Select class")  # default value
                    w = OptionMenu(root, f, "Class 1", "Class 2", "Class 3", "Class 4", "Class 5", "Class 6", "Class 7",
                                   "Class 8", "Class 9", "Class 10", "Class 11", "Class 12")
                    w.grid(row=6, column=1)

                    l = Label(root, text='Enter mobile no. : ')
                    l.grid(row=7, column=0)
                    q = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light blue")  # q=total fee
                    q.grid(row=7, column=1)
                    l = Label(root, text='Enter year due fee : ')
                    l.grid(row=8, column=0)
                    m = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light blue")  # q=mobile no.
                    m.grid(row=8, column=1)

                    l = Label(root, text='Enter Password : ')
                    l.grid(row=9, column=0)
                    p = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light blue")  # q=pswd
                    p.grid(row=9, column=1)

                    cur.execute(
                        "create table if not exists student(sid number primary key, name varchar(20), fname varchar(20),mname varchar(20), clno number(4),mbno number(10), yearduefee number(6),pswd number(6),paidfee number(6),duefee number(6), eng_at number(4), hin_at number(4), mat_at number(4), sc_at number(4), ssc_at number(4), san_at number(4), eng_m number(4), hin_m number(4), mat_m number(4), sc_m number(4), ssc_m number(4), san_m number(4))")

                    def insertinstudent():
                        cur.execute("select * from student where sid=?", (int(c.get()),))
                        #cpy = cur.fetchone()
                        try:

                            cur.execute("insert into student values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (
                            int(c.get()), d.get(), e.get(), g.get(), f.get(), int(q.get()),int(m.get()),int(p.get()), 0, int(m.get()), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0))
                            con.commit()
                            showinfo('Information', 'Student Insertion Successful')

                        ################################################################################################################
                        except sqlite3.IntegrityError as error:
                            showwarning('Error', 'Already exists!')

                    Button(root, text='Insert Data Of Student', command=insertinstudent, width=25,
                           font=("Times New", 10), bd=5, bg="light blue").grid(row=10, column=0, sticky=N + S + E + W)

                    def logout():
                        ans = askyesno('Confirmation', 'Do You Want To Exit?')
                        if (ans == True):
                            root.destroy()

                    Button(root, text='Exit', command=logout, width=25, font=("Times New", 10), bd=5,
                           bg="light blue").grid(row=11, column=0, sticky=N + S + E + W)
                    root.mainloop()

            Button(menu, text='Register Student details', command=option1, width=25, font=("Times New", 10), bd=5,
                   bg="light blue").grid(row=1, column=0, sticky=N + S + E + W)
################################################################################################
            def option2():

                    root = Toplevel()
                    root.geometry('1080x600')
                    root.title('Register Teacher Details')
                    l = Label(root, text='Register Teacher Details :', font='Times 20 bold')
                    l.grid(row=0, column=3)

                    l = Label(root, text=' ')
                    l.grid(row=1, column=0)

                    l = Label(root, text='Enter Teacher ID : ')
                    l.grid(row=2, column=0)

                    c = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light blue")  # c=sid
                    c.grid(row=2, column=1)
                    #xp = c.get()

                    l = Label(root, text='Enter first name : ')
                    l.grid(row=3, column=0)
                    d = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light blue")  # d=fname
                    d.grid(row=3, column=1)
                    l = Label(root, text='Enter last name : ')
                    l.grid(row=4, column=0)
                    e = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light blue")  # e=lname
                    e.grid(row=4, column=1)


                    l = Label(root, text='Enter Password : ')
                    l.grid(row=5, column=0)
                    q = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light blue")  # q=total fee
                    q.grid(row=5, column=1)

                    cur1.execute(
                        "create table if not exists teacher(tid number primary key, fname varchar(20), lname varchar(20), pswd number(6))")

                    def insertinteacher():
                        cur1.execute("select * from teacher where tid=?", (int(c.get()),))
                        cpy = cur1.fetchone()
                        try:
                            cur1.execute("insert into teacher values(?,?,?,?)", (
                            int(c.get()), d.get(), e.get(), int(q.get())))
                            con1.commit()
                            showinfo('Information', 'Teacher Insertion Successful')

                        ################################################################################################################
                        except sqlite3.IntegrityError as error:
                            showwarning('Error', 'Already exists!')

                    Button(root, text='Insert Data Of Teacher', command=insertinteacher, width=25,
                           font=("Times New", 10), bd=5, bg="light blue").grid(row=7, column=0, sticky=N + S + E + W)

                    def logout():
                        ans = askyesno('Confirmation', 'Do You Want To Exit?')
                        if (ans == True):
                            root.destroy()

                    Button(root, text='Exit', command=logout, width=25, font=("Times New", 10), bd=5,
                           bg="light blue").grid(row=8, column=0, sticky=N + S + E + W)
                    root.mainloop()

            Button(menu, text='Register Teacher details', command=option2, width=25, font=("Times New", 10), bd=5,
                   bg="light blue").grid(row=2, column=0, sticky=N + S + E + W)
            ##################################################################
            def option3():

                    root = Toplevel()
                    root.geometry('1080x600')
                    root.title('Student Fee Updation')
                    l = Label(root, text='Student Fee Updation :', font='Times 20 bold')
                    l.grid(row=0, column=3)

                    l = Label(root, text=' ')
                    l.grid(row=1, column=0)

                    l = Label(root, text='Enter Student ID : ')
                    l.grid(row=2, column=0)
                    g = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light blue")  # g=sid
                    g.grid(row=2, column=1)
                    l = Label(root, text='Enter fee paid : ')
                    l.grid(row=3, column=0)
                    h = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light blue")  # h=fee paid
                    h.grid(row=3, column=1)

                    def update1():
                        p = int(g.get())
                        cur.execute("update student set duefee=duefee-? where sid=?", (int(h.get()), p))
                        con.commit()
                        cur.execute("update student set paidfee=paidfee+? where sid=?", (int(h.get()), p))
                        con.commit()
                        showinfo('Information', 'Fee Updation Successful')

                    Button(root, text='Update Fee', command=update1, width=25, font=("Times New", 10), bd=5,
                           bg="light blue").grid(row=4, column=0, sticky=N + S + E + W)

                    l = Label(root, text=' ')
                    l.grid(row=5, column=0)

                    l = Label(root, text='Enter Student ID to see details : ')
                    l.grid(row=6, column=0)
                    i = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light blue")  # i=sid
                    i.grid(row=6, column=1)

                    def show3():
                        w = [(int(i.get()))]
                        cur.execute("select duefee from student where sid=?", w)
                        x = cur.fetchall()
                        showinfo('Result', x)

                    Button(root, text='Show Student due fee ', command=show3, width=25, font=("Times New", 10), bd=5,
                           bg="light blue").grid(row=7, column=0, sticky=N + S + E + W)

                    def logout():
                        ans = askyesno('Confirmation', 'Do You Want To Exit?')
                        if (ans == True):
                            root.destroy()

                    Button(root, text='Exit', command=logout, width=25, font=("Times New", 10), bd=5,
                           bg="light blue").grid(row=8, column=0)
                    root.mainloop()


            Button(menu, text='Student Fee Updation', command=option3, width=25, font=("Times New", 10), bd=5,
                   bg="light blue").grid(row=3, column=0, sticky=N + S + E + W)

            ######################################################################################################################################################################
            def logout():
                ans = askyesno('Confirmation', 'Do You Want To Logout?')
                if (ans == True):
                    menu.destroy()

            Button(menu, text='Logout', command=logout, width=25, font=("Times New", 10), bd=5, bg="light blue").grid(
                row=8, column=0, sticky=N + S + E + W)

            menu.mainloop()

    Button(window, text='Login', command=login, width=20, font=("Times New", 15), bd=5, bg="light blue").grid(row=3,
                                                                                                              column=2,
                                                                                                              sticky=N + S + E + W)