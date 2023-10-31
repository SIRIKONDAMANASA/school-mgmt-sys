from tkinter.messagebox import *
import sqlite3

con = sqlite3.Connection('student_records.db')
cur = con.cursor()
from tkinter import *
def start():
    window = Toplevel()
    window.geometry('1080x600')
    window.title('Login Window')
    Label(window, text='ID  ', font=("Times New", 20)).grid(row=1, column=1)  # v=id
    v = Entry(window, width=25, font=("Times New", 18), bd=5, bg="light blue")
    v.grid(row=1, column=2)
    Label(window, text='Mobile no.  ', font=("Times n=New", 20)).grid(row=2, column=1)
    vv = Entry(window, show='*', width=25, font=("Times New", 18), bd=5, bg="light blue")  # vv=password
    vv.grid(row=2, column=2)

    def login():
        id=[int(v.get())]
        z = cur.execute("select mbno from student where sid=?", id)
        x=z.fetchone()
        print(x)
        if ((int(vv.get()) != x[0])):
            showwarning('Login Failed', 'Incorrect Id Or Password Used Or ')
        else:
            menu = Toplevel()
            menu.geometry('1080x600')
            menu.title('Menu Window')

            l = Label(menu, text='Dashboard :', font='Times 20 bold')
            l.grid(row=0, column=0)

            Label(menu).grid(row=1, column=100, rowspan=30)
            ################################################################################
            def option5():
                    root = Toplevel()
                    root.geometry('1080x600')
                    root.title('View Window')
                    Label(root, text="Attendance", font=("Times New", 20)).grid(row=0, column=4)
                    row_number = 0
                    Label(root, text="English    :", font=("Times New", 20)).grid(row=1, column=row_number)
                    Label(root, text="Hindi      :", font=("Times New", 20)).grid(row=2, column=row_number)
                    Label(root, text="Mathematics:", font=("Times New", 20)).grid(row=3, column=row_number)
                    Label(root, text="Science    :", font=("Times New", 20)).grid(row=4, column=row_number)
                    Label(root, text="Social     :", font=("Times New", 20)).grid(row=5, column=row_number)
                    Label(root, text="Sanskrit   :", font=("Times New", 20)).grid(row=6, column=row_number)

                    z = cur.execute("select eng_at,hin_at,mat_at,sc_at,ssc_at,san_at from student where sid=?", id)
                    for row_number, row in enumerate(z):
                        Label(root, text="" + str(row[0]), font=("Times New", 18)).grid(row=1, column=row_number + 1)
                        Label(root, text="" + str(row[1]), font=("Times New", 18)).grid(row=2, column=row_number + 1)
                        Label(root, text="" + str(row[2]), font=("Times New", 18)).grid(row=3, column=row_number + 1)
                        Label(root, text="" + str(row[3]), font=("Times New", 18)).grid(row=4, column=row_number + 1)
                        Label(root, text="" + str(row[4]), font=("Times New", 18)).grid(row=5, column=row_number + 1)
                        Label(root, text="" + str(row[5]), font=("Times New", 18)).grid(row=6, column=row_number + 1)

                    def logout():
                        ans = askyesno('Confirmation', 'Do You Want To Exit?')
                        if (ans == True):
                            root.destroy()

                    Button(root, text='Exit', command=logout, width=25, font=("Times New", 10), bd=5, bg="light blue").grid(
                        row=8, column=0)
                    root.mainloop()

            Button(menu, text='View Attendance', command=option5, width=25, font=("Times New", 10), bd=5,
                   bg="light blue").grid(row=5, column=0, sticky=N + S + E + W)

 #########################################################################################################################################
            def option7():

                    root = Toplevel()
                    root.geometry('1080x600')
                    root.title('View Window')
                    Label(root, text="Marks", font=("Times New", 20)).grid(row=0, column=4)
                    row_number = 0
                    Label(root, text="English    :", font=("Times New", 20)).grid(row=1, column=row_number)
                    Label(root, text="Hindi      :", font=("Times New", 20)).grid(row=2, column=row_number)
                    Label(root, text="Mathematics:", font=("Times New", 20)).grid(row=3, column=row_number)
                    Label(root, text="Science    :", font=("Times New", 20)).grid(row=4, column=row_number)
                    Label(root, text="Social     :", font=("Times New", 20)).grid(row=5, column=row_number)
                    Label(root, text="Sanskrit   :", font=("Times New", 20)).grid(row=6, column=row_number)

                    z = cur.execute("select eng_m,hin_m,mat_m,sc_m,ssc_m,san_m from student where sid=?", id)
                    for row_number, row in enumerate(z):
                        Label(root, text="" + str(row[0]), font=("Times New", 18)).grid(row=1, column=row_number + 1)
                        Label(root, text="" + str(row[1]), font=("Times New", 18)).grid(row=2, column=row_number + 1)
                        Label(root, text="" + str(row[2]), font=("Times New", 18)).grid(row=3, column=row_number + 1)
                        Label(root, text="" + str(row[3]), font=("Times New", 18)).grid(row=4, column=row_number + 1)
                        Label(root, text="" + str(row[4]), font=("Times New", 18)).grid(row=5, column=row_number + 1)
                        Label(root, text="" + str(row[5]), font=("Times New", 18)).grid(row=6, column=row_number + 1)

                    def logout():
                        ans = askyesno('Confirmation', 'Do You Want To Exit?')
                        if (ans == True):
                            root.destroy()

                    Button(root, text='Exit', command=logout, width=25, font=("Times New", 10), bd=5, bg="light blue").grid(
                        row=8, column=0)
                    root.mainloop()

            Button(menu, text='View Marks', command=option7, width=25, font=("Times New", 10), bd=5,
                   bg="light blue").grid(row=7, column=0, sticky=N + S + E + W)

            def logout():
                ans = askyesno('Confirmation', 'Do You Want To Logout?')
                if (ans == True):
                    menu.destroy()

            Button(menu, text='Logout', command=logout, width=25, font=("Times New", 10), bd=5, bg="light blue").grid(
                row=8, column=0, sticky=N + S + E + W)
            ################################################################################
            def option3():
                    root = Toplevel()
                    root.geometry('1080x600')
                    root.title('View Fee')
                    l = Label(root, text='FEE:', font='Times 20 bold')
                    l.grid(row=0, column=3)
                    l = Label(root, text=' ')
                    l.grid(row=5, column=0)
                    cur.execute("select yearduefee from student where sid=?", id)
                    x = cur.fetchall()
                    Label(root, text=' TOTAL FEE : ' + str(x[0][0]), font='Times 16 bold').grid(column=1, row=1)

                    cur.execute("select duefee from student where sid=?", id)
                    y = cur.fetchall()
                    Label(root, text=' DUE FEE : ' + str(y[0][0]), font='Times 16 bold').grid(column=1, row=2)

                    cur.execute("select paidfee from student where sid=?", id)
                    z = cur.fetchall()
                    Label(root, text=' PAID FEE : ' + str(z[0][0]), font='Times 16 bold').grid(column=1, row=3)

                    def logout():
                        ans = askyesno('Confirmation', 'Do You Want To Exit?')
                        if (ans == True):
                            root.destroy()

                    Button(root, text='Exit', command=logout, width=25, font=("Times New", 10), bd=5,
                           bg="light blue").grid(row=8, column=0)
                    root.mainloop()


            Button(menu, text='View Fee', command=option3, width=25, font=("Times New", 10), bd=5,
                   bg="light blue").grid(row=3, column=0, sticky=N + S + E + W)

            menu.mainloop()

    Button(window, text='Login', command=login, width=20, font=("Times New", 15), bd=5, bg="light blue").grid(
        row=3,
        column=2,
        sticky=N + S + E + W)