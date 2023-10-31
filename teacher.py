from tkinter.messagebox import *
import sqlite3

con = sqlite3.Connection('student_records.db')
cur = con.cursor()
con1 = sqlite3.Connection('teacher_records.db')
cur1 = con1.cursor()
from tkinter import *
def start():
    window = Toplevel()
    window.geometry('1080x600')
    window.title('Login Window')
    Label(window, text='Username  ', font=("Times New", 20)).grid(row=1, column=1)  # v=id
    v = Entry(window, width=25, font=("Times New", 18), bd=5, bg="light blue")
    v.grid(row=1, column=2)
    Label(window, text='Password  ', font=("Times n=New", 20)).grid(row=2, column=1)
    vv = Entry(window, show='*', width=25, font=("Times New", 18), bd=5, bg="light blue")  # vv=password
    vv.grid(row=2, column=2)
    def login():
        id=[int(v.get())]
        z = cur1.execute("select pswd from teacher where tid=?", id)
        x=z.fetchone()
        if ((int(vv.get()) != x[0])):
            showwarning('Login Failed', 'Incorrect Id Or Password Used Or ')
        else:
            menu = Toplevel()
            menu.geometry('1080x600')
            menu.title('Menu Window')

            l = Label(menu, text='Dashboard :', font='Times 20 bold')
            l.grid(row=0, column=0)

            Label(menu).grid(row=1, column=100, rowspan=30)
            #############################################################
            def option1():
                root = Toplevel()
                root.geometry('1080x600')
                root.title('Student Details View')
                l = Label(root, text='View Student Details :', font='Times 20 bold')
                l.grid(row=0, column=3)
                l = Label(root, text=' ')
                l.grid(row=1, column=0)

                l = Label(root, text='Enter Student Id : ')
                l.grid(row=2, column=0)
                ui = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light blue")  # ui=sid
                ui.grid(row=2, column=1)

                l = Label(root, text='Enter class : ')
                l.grid(row=4, column=0)
                f = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light blue")  # f=clno.
                f.grid(row=4, column=1)

                def show1():
                    root = Toplevel()
                    root.geometry('1080x600')
                    root.title('View Window')
                    val = [(int(ui.get()))]
                    row_number = 0
                    Label(root, text="Student ID :", font=("Times New", 20)).grid(row=1, column=row_number)
                    Label(root, text="Name       :", font=("Times New", 20)).grid(row=2, column=row_number)
                    Label(root, text="Father Name:", font=("Times New", 20)).grid(row=3, column=row_number)
                    Label(root, text="Mother Name:", font=("Times New", 20)).grid(row=4, column=row_number)
                    Label(root, text="Class      :", font=("Times New", 20)).grid(row=5, column=row_number)
                    Label(root, text="Mobile no. :", font=("Times New", 20)).grid(row=6, column=row_number)

                    z = cur.execute("select *from student where sid=?", val)
                    for row_number, row in enumerate(z):
                        Label(root, text="" + str(row[0]), font=("Times New", 18)).grid(row=1, column=row_number + 1)
                        Label(root, text="" + str(row[1]), font=("Times New", 18)).grid(row=2, column=row_number + 1)
                        Label(root, text="" + str(row[2]), font=("Times New", 18)).grid(row=3, column=row_number + 1)
                        Label(root, text="" + str(row[3]), font=("Times New", 18)).grid(row=4, column=row_number + 1)
                        Label(root, text="" + str(row[4]), font=("Times New", 18)).grid(row=5, column=row_number + 1)
                        Label(root, text="" + str(row[5]), font=("Times New", 18)).grid(row=6, column=row_number + 1)

                    root.mainloop()

                Button(root, text='Show Student Data', command=show1, width=15, font=("Times New", 10), bd=5,
                       bg="light blue").grid(row=2, column=2, sticky=N + S + E + W)

                ##########################################################################################
                def show2():
                    root = Toplevel()
                    root.geometry('1080x600')
                    root.title('View Window')
                    v = [(f.get())]
                    z = cur.execute("select *from student where clno=?", v)
                    row_number = 0
                    Label(root, text="Student ID").grid(column=1, row=row_number)
                    Label(root, text="Name").grid(column=2, row=row_number)
                    Label(root, text="Father Name").grid(column=3, row=row_number)
                    Label(root, text="Mother Name").grid(column=4, row=row_number)
                    Label(root, text="Class").grid(column=5, row=row_number)
                    Label(root, text="Mobile no.").grid(column=6, row=row_number)

                    y = -1
                    for row_number, row in enumerate(z):
                        y = y + 1
                        Label(root, text="" + str(row[0])).grid(column=1, row=row_number + 1+y)
                        Label(root, text="" + str(row[1])).grid(column=2, row=row_number + 1+y)
                        Label(root, text="" + str(row[2])).grid(column=3, row=row_number + 1+y)
                        Label(root, text="" + str(row[3])).grid(column=4, row=row_number + 1+y)
                        Label(root, text="" + str(row[4])).grid(column=5, row=row_number + 1+y)
                        Label(root, text="" + str(row[5])).grid(column=6, row=row_number + 1+y)

                    root.mainloop()

                Button(root, text='Show All Student Data Of Class', command=show2, width=25, font=("Times New", 10),
                       bd=5, bg="light blue").grid(row=4, column=2, sticky=N + S + E + W)

                ###########################################################################
                def logout():
                    ans = askyesno('Confirmation', 'Do You Want To Exit?')
                    if (ans == True):
                        root.destroy()
                Button(root, text='Exit', command=logout, width=25, font=("Times New", 10), bd=5, bg="light blue").grid(
                    row=8, column=0, sticky=N + S + E + W)
                root.mainloop()

            Button(menu, text='View Student details', command=option1, width=25, font=("Times New", 10), bd=5,
                   bg="light blue").grid(row=1, column=0, sticky=N + S + E + W)
            #############################################################
            def option2():
                    win = Toplevel()
                    win.geometry('1080x600')
                    win.title('Update Attendance')
                    l = Label(win, text='Enter Student Id : ')
                    l.grid(row=2, column=0)
                    f = Entry(win, font=("Times New", 10), bd=5, bg="light blue")  # f=sid.
                    f.grid(row=2, column=1)
                    def fill():
                        Label(win, text="English").grid(column=1, row=3, sticky=N + S + E + W)
                        eng = Entry(win, width=15, font=("Times New", 10), bd=5, bg="light blue")
                        eng.grid(row=4, column=1, sticky=N + S + E + W)

                        Label(win, text="Hindi").grid(column=2, row=3, sticky=N + S + E + W)
                        hin = Entry(win, width=15, font=("Times New", 10), bd=5, bg="light blue")
                        hin.grid(row=4, column=2, sticky=N + S + E + W)

                        Label(win, text="Mathematics").grid(column=3, row=3, sticky=N + S + E + W)
                        mat = Entry(win, width=15, font=("Times New", 10), bd=5, bg="light blue")
                        mat.grid(row=4, column=3, sticky=N + S + E + W)

                        Label(win, text="Science").grid(column=4, row=3)
                        sc = Entry(win, width=15, font=("Times New", 10), bd=5, bg="light blue")
                        sc.grid(row=4, column=4, sticky=N + S + E + W)

                        Label(win, text="Social Science").grid(column=5, row=3, sticky=N + S + E + W)
                        ssc = Entry(win, width=15, font=("Times New", 10), bd=5, bg="light blue")
                        ssc.grid(row=4, column=5, sticky=N + S + E + W)

                        Label(win, text="Sanskrit").grid(column=6, row=3, sticky=N + S + E + W)
                        san = Entry(win, width=15, font=("Times New", 10), bd=5, bg="light blue")
                        san.grid(row=4, column=6, sticky=N + S + E + W)

                        def regist():
                            cur.execute("update student set eng_at=? where sid=?", (eng.get(), f.get()))
                            con.commit()
                            cur.execute("update student set hin_at=? where sid=?", (hin.get(), f.get()))
                            con.commit()
                            cur.execute("update student set mat_at=? where sid=?", (mat.get(), f.get()))
                            con.commit()
                            cur.execute("update student set sc_at=? where sid=?", (sc.get(), f.get()))
                            con.commit()
                            cur.execute("update student set ssc_at=? where sid=?", (ssc.get(), f.get()))
                            con.commit()
                            cur.execute("update student set san_at=? where sid=?", (san.get(), f.get()))
                            con.commit()
                            showinfo('Information', 'Attendance Locked')
                        #######################################################################################################
                        Button(win, text='Submit', command=regist, width=25, font=("Times New", 10), bd=5,
                               bg="light blue").grid(row=5, column=0)

                    Button(win, text='Show', command=fill, width=15, font=("Times New", 10), bd=5,
                           bg="light blue").grid(row=2, column=2)

                    def logout():
                        ans = askyesno('Confirmation', 'Do You Want To Exit?')
                        if (ans == True):
                            win.destroy()

                    Button(win, text='Exit', command=logout, width=15, font=("Times New", 10), bd=5,
                           bg="light blue").grid(row=2, column=3)

                    win.mainloop()


            Button(menu, text='Update Attendance', command=option2, width=25, font=("Times New", 10), bd=5,
                   bg="light blue").grid(row=2, column=0, sticky=N + S + E + W)
            #########################################################################################################################################
            def option3():
                win = Toplevel()
                win.geometry('1080x600')
                win.title('Update Student Marks')
                l = Label(win, text='Enter Student Id : ')
                l.grid(row=2, column=0)
                f = Entry(win, font=("Times New", 10), bd=5, bg="light blue")  # f=sid.
                f.grid(row=2, column=1)

                def fill():
                    Label(win, text="English").grid(column=1, row=3, sticky=N + S + E + W)
                    eng = Entry(win, width=15, font=("Times New", 10), bd=5, bg="light blue")
                    eng.grid(row=4, column=1, sticky=N + S + E + W)

                    Label(win, text="Hindi").grid(column=2, row=3, sticky=N + S + E + W)
                    hin = Entry(win, width=15, font=("Times New", 10), bd=5, bg="light blue")
                    hin.grid(row=4, column=2, sticky=N + S + E + W)

                    Label(win, text="Mathematics").grid(column=3, row=3, sticky=N + S + E + W)
                    mat = Entry(win, width=15, font=("Times New", 10), bd=5, bg="light blue")
                    mat.grid(row=4, column=3, sticky=N + S + E + W)

                    Label(win, text="Science").grid(column=4, row=3)
                    sc = Entry(win, width=15, font=("Times New", 10), bd=5, bg="light blue")
                    sc.grid(row=4, column=4, sticky=N + S + E + W)

                    Label(win, text="Social Science").grid(column=5, row=3, sticky=N + S + E + W)
                    ssc = Entry(win, width=15, font=("Times New", 10), bd=5, bg="light blue")
                    ssc.grid(row=4, column=5, sticky=N + S + E + W)

                    Label(win, text="Sanskrit").grid(column=6, row=3, sticky=N + S + E + W)
                    san = Entry(win, width=15, font=("Times New", 10), bd=5, bg="light blue")
                    san.grid(row=4, column=6, sticky=N + S + E + W)

                    def regist():
                        cur.execute("update student set eng_m=? where sid=?", (eng.get(), f.get()))
                        con.commit()
                        cur.execute("update student set hin_m=? where sid=?", (hin.get(), f.get()))
                        con.commit()
                        cur.execute("update student set mat_m=? where sid=?", (mat.get(), f.get()))
                        con.commit()
                        cur.execute("update student set sc_m=? where sid=?", (sc.get(), f.get()))
                        con.commit()
                        cur.execute("update student set ssc_m=? where sid=?", (ssc.get(), f.get()))
                        con.commit()
                        cur.execute("update student set san_m=? where sid=?", (san.get(), f.get()))
                        con.commit()
                        showinfo('Information', 'Marks Locked')

                    ######################################################################################################

                    Button(win, text='Submit', command=regist, width=15, font=("Times New", 10), bd=5,
                           bg="light blue").grid(row=5, column=0)

                Button(win, text='Show', command=fill, width=15, font=("Times New", 10), bd=5,
                       bg="light blue").grid(row=2, column=2)

                def logout():
                    ans = askyesno('Confirmation', 'Do You Want To Exit?')
                    if (ans == True):
                        win.destroy()

                Button(win, text='Exit', command=logout, width=15, font=("Times New", 10), bd=5,
                       bg="light blue").grid(row=2, column=3)

                win.mainloop()

            Button(menu, text='Update Student Marks', command=option3, width=25, font=("Times New", 10), bd=5,
                   bg="light blue").grid(row=3, column=0, sticky=N + S + E + W)
            ####################################################################
            def option5():
                root = Toplevel()
                root.geometry('1080x600')
                root.title('Change Password')
                l = Label(root, text='Change Password :', font='Times 20 bold')
                l.grid(row=0, column=3)

                l = Label(root, text=' ')
                l.grid(row=1, column=0)

                l = Label(root, text='Enter New Password : ')
                l.grid(row=3, column=0)
                h = Entry(root, width=25, font=("Times New", 10), bd=5, bg="light blue")
                h.grid(row=3, column=1)

                def update1():
                    cur1.execute("update teacher set pswd=? where tid=?", (int(h.get()), id[0]))
                    con1.commit()
                    showinfo('Information', 'Password Changed Successfully')

                Button(root, text='save & change', command=update1, width=25, font=("Times New", 10), bd=5,
                       bg="light blue").grid(row=4, column=0, sticky=N + S + E + W)

                def logout():
                    ans = askyesno('Confirmation', 'Do You Want To Exit?')
                    if (ans == True):
                        root.destroy()

                Button(root, text='Exit', command=logout, width=25, font=("Times New", 10), bd=5,
                       bg="light blue").grid(row=8, column=0)
                root.mainloop()

            Button(menu, text='Change Password', command=option5, width=25, font=("Times New", 10), bd=5,
                   bg="light blue").grid(row=6, column=0, sticky=N + S + E + W)

            ######################################################################################################################################################################
            def logout():
                ans = askyesno('Confirmation', 'Do You Want To Logout?')
                if (ans == True):
                    menu.destroy()

            Button(menu, text='Logout', command=logout, width=25, font=("Times New", 10), bd=5, bg="light blue").grid(
                row=8, column=0, sticky=N + S + E + W)
            menu.mainloop()
            ####################################
    Button(window, text='Login', command=login, width=20, font=("Times New", 15), bd=5, bg="light blue").grid(
        row=3,
        column=2,
        sticky=N + S + E + W)