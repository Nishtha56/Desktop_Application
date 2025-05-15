from tkinter import *
from tkinter.ttk import Combobox, Treeview
from tkinter import messagebox
import pymysql
from tkcalendar import DateEntry


class BookingClass:
    def __init__(self, home_window):
        self.window = Toplevel(home_window)

        self.window.title('Hotel Manager/BOOKING')
        self.window.config(background='#c1d1f8')

        # -----setting-----------
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        w1 = int(w - 100)
        h1 = int(h - 180)

        self.window.minsize(w1, h1)
        self.window.geometry("%dx%d+%d+%d" % (w1, h1, 50, 70))



        # --------widgets------------
        mycolor = '#032881'
        mycolor2 = '#1449cb'
        myfont1 = ('Trebuchet MS', 15)

        self.hdlbl = Label(self.window, text='BOOKING SLOT', background=mycolor2, font=('Georgia', 35, 'bold'),
                           relief='groove', borderwidth=10, foreground='white')
        self.hdlbl.config(background=mycolor)
        self.l1 = Label(self.window, text='Reg_No', background='#c1d1f8', font=myfont1)
        self.l2 = Label(self.window, text='Name', background='#c1d1f8', font=myfont1)
        self.l3 = Label(self.window, text='Phone', background='#c1d1f8', font=myfont1)
        self.l4 = Label(self.window, text='UID', background='#c1d1f8', font=myfont1)

        self.l6 = Label(self.window, text='Check In', background='#c1d1f8', font=myfont1)
        self.l7 = Label(self.window, text='Check Out', background='#c1d1f8', font=myfont1)

        self.l8 = Label(self.window, text='Total Guest', background='#c1d1f8', font=myfont1)

        # buttons-------------------------------------------

        self.b1 = Button(self.window, text='Save', background=mycolor2, foreground='white', font=myfont1,
                         command=self.saveData)

        self.b2 = Button(self.window, text='Update', background=mycolor2, foreground='white', font=myfont1,
                         command=self.updateData)

        self.b3 = Button(self.window, text='Delete', background=mycolor2, foreground='white', font=myfont1,
                         command=self.deleteData)

        self.b4 = Button(self.window, text='Fetch', background=mycolor2, foreground='white', font=myfont1,
                         command=self.fetchData)

        self.b5 = Button(self.window, text="Search", background=mycolor2, foreground='white', font=myfont1,
                         command=self.getAllData)

        # ---------------------------------------------------------
        self.t1 = Entry(self.window, font=myfont1)
        self.t2 = Entry(self.window, font=myfont1)
        self.t3 = Entry(self.window, font=myfont1)
        self.t4 = Entry(self.window, font=myfont1)



        self.t6 = DateEntry(self.window, width=12, background='darkblue', foreground='white',
                            borderwidth=2, year=2023, font=myfont1, date_pattern='y-mm-dd')
        self.t7 = DateEntry(self.window, width=12, background='darkblue', foreground='white',
                            borderwidth=2, year=2023, font=myfont1, date_pattern='y-mm-dd')

        self.t8 = Entry(self.window, font=myfont1)

        # ---------------- table -------------

        self.mytable = Treeview(self.window, columns=['c1', 'c2', 'c3', 'c4','c5', 'c6', 'c7'], height=20)
        self.mytable.heading('c1', text='Reg_No')
        self.mytable.heading('c2', text='Name')
        self.mytable.heading('c3', text='Phone')
        self.mytable.heading('c4', text='UID')

        self.mytable.heading('c5', text='Check_In')
        self.mytable.heading('c6', text='Check_Out')
        self.mytable.heading('c7', text='Total_guest')

        self.mytable['show'] = 'headings'

        self.mytable.column("#1", width=100, anchor='center')
        self.mytable.column("#2", width=100, anchor='center')
        self.mytable.column("#3", width=100, anchor='center')
        self.mytable.column("#4", width=100, anchor='center')

        self.mytable.column("#5", width=100, anchor='center')
        self.mytable.column("#6", width=100, anchor='center')
        self.mytable.column("#7", width=100, anchor='center')
        self.mytable.bind("<ButtonRelease-1>", lambda e: self.getSelectedRowData())

        # ----------placements----------------
        x1 = 20
        y1 = 100

        x_diff = 150
        y_diff = 50
        self.hdlbl.place(x=0, y=0, width=w1 + 100, height=80)

        self.l1.place(x=x1, y=y1)
        self.t1.place(x=x1 + x_diff, y=y1)
        self.mytable.place(x=x1 + x_diff + x_diff + 200, y=y1)

        y1 += y_diff

        self.l2.place(x=x1, y=y1)
        self.t2.place(x=x1 + x_diff, y=y1)

        y1 += y_diff
        self.l3.place(x=x1, y=y1)
        self.t3.place(x=x1 + x_diff, y=y1)

        y1 += y_diff
        self.l4.place(x=x1, y=y1)
        self.t4.place(x=x1 + x_diff, y=y1)



        y1 += y_diff
        self.l6.place(x=x1, y=y1)
        self.t6.place(x=x1 + x_diff, y=y1)

        y1 += y_diff
        self.l7.place(x=x1, y=y1)
        self.t7.place(x=x1 + x_diff, y=y1)

        y1 += y_diff
        self.l8.place(x=x1, y=y1)
        self.t8.place(x=x1 + x_diff, y=y1)

        y1 += y_diff
        self.b1.place(x=x1, y=y1, width=100, height=40)
        self.b2.place(x=x1 + x_diff, y=y1, width=100, height=40)
        self.b3.place(x=x1 + x_diff + x_diff, y=y1, width=100, height=40)

        y1 = 100
        self.b4.place(x=x1 + x_diff + x_diff + 70, y=y1, width=100, height=40)

        y1 = 150
        self.b5.place(x=x1 + x_diff + x_diff + 70, y=y1, width=100, height=40)

        # functions--------------------------------------

        self.databaseConnection()
        self.clearPage()

        self.window.mainloop()

    def databaseConnection(self):
        try:
            self.conn = pymysql.connect(host='localhost', db='hotel_manager_db', user='root', password='')
            self.curr = self.conn.cursor()

        except Exception as e:
            messagebox.showinfo('Database Error', 'Database Connection Error')

    def saveData(self):
        if self.validate_check() == False:
            return

        try:
            qry = 'insert into booking_table values(%s,%s,%s,%s,%s,%s,%s)'
            rowcount = self.curr.execute(qry, (
                self.t1.get(), self.t2.get(), self.t3.get(), self.t4.get(), self.t6.get(), self.t7.get(),
                self.t8.get()))
            self.conn.commit()
            if rowcount == 1:
                messagebox.showinfo('Success', 'booking Added Successfully :)', parent=self.window)
                self.clearPage()
        except Exception as e:
            messagebox.showerror('Query Error', 'Querry Error : \n ' + str(e), parent=self.window)

    def updateData(self):
        if self.validate_check() == False:
            return

        try:
            qry = "update booking_table set Name=%s, Phone=%s,UID=%s, Check_In=%s, Check_Out=%s, " \
                  "Total_guests=%s where Reg_No=%s "
            rowcount = self.curr.execute(qry, (self.t2.get(), self.t3.get(), self.t4.get(),
                                                self.t6.get(), self.t7.get(),
                                               self.t8.get(), self.t1.get()))
            self.conn.commit()
            if rowcount == 1:
                messagebox.showinfo("Sucess", "Booking Update successfully :)", parent=self.window)
                self.clearPage()
        except Exception as e:
            messagebox.showerror("Query Error", "Query Error : \n" + str(e), parent=self.window)

    def deleteData(self):

        ans = messagebox.askquestion("Confirmation", "Are you to delete?", parent=self.window)
        if ans == 'yes':
            try:
                qry = "delete from booking_table where Reg_Id=%s "
                rowcount = self.curr.execute(qry, (self.t1.get()))
                self.conn.commit()
                if rowcount == 1:
                    messagebox.showinfo("Sucess", "Booking deleted successfully :)", parent=self.window)
                    self.clearPage()
            except Exception as e:
                messagebox.showerror("Query Error", "Query Error : \n" + str(e), parent=self.window)

    def getSelectedRowData(self):
        row_id = self.mytable.focus()
        print("Row id = ", row_id)
        rowdata = self.mytable.item(row_id)
        print("Row Data = ", rowdata)
        row_values = rowdata['values']
        print("Row Values = ", row_values)
        cols_data = row_values[0]
        print("Column 0 data = ", cols_data)
        self.fetchData(cols_data)

    def fetchData(self, pk_col=None):
        if pk_col == None:
            Reg_No = self.t1.get()
        else:
            Reg_No = pk_col
        try:
            qry = "select * from booking_table where Reg_No=%s"
            rowcount = self.curr.execute(qry, (Reg_No))
            data = self.curr.fetchone()
            # print("data = ",data)
            self.clearPage()
            if data:
                self.t1.insert(0, data[0])
                self.t2.insert(0, data[1])
                self.t3.insert(0, data[2])
                self.t4.insert(0, data[3])
                self.t6.insert(0, data[4])
                self.t7.insert(0, data[5])
                self.t8.insert(0, data[6])



            else:
                messagebox.showwarning("Empty", "No Record Found", parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error", "Query Error : \n" + str(e), parent=self.window)


    def clearPage(self):
        self.t1.delete(0, END)
        self.t2.delete(0, END)
        self.t3.delete(0, END)
        self.t4.delete(0, END)

        self.t6.delete(0, END)
        self.t7.delete(0, END)
        self.t8.delete(0, END)

    def getAllData(self):
        try:
            self.mytable.delete(*self.mytable.get_children())

            qry = "select * from booking_table where Name like %s "
            rowcount = self.curr.execute(qry, (self.t2.get() + "%"))
            data = self.curr.fetchall()
            if data:
                for myrow in data:
                    self.mytable.insert("", END, values=myrow)

            else:
                messagebox.showwarning("Empty", "No Record Found", parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error", "Query Error : \n" + str(e), parent=self.window)




        # --------------warnings----------------------------

    def validate_check(self):
        if not (self.t1.get().isdigit()) or len(self.t1.get()) < 1:
            messagebox.showwarning("Validation Check", "Invalid Registration no.", parent=self.window)
            return False
        elif len(self.t2.get()) < 2:
            messagebox.showwarning("Validation Check", "Enter Proper Name (atleast 2 characters) ", parent=self.window)
            return False
        elif not (self.t3.get().isdigit()) or len(self.t3.get()) != 10:
            messagebox.showwarning("Validation Check", "Enter Valid Phone No \n10 digits only", parent=self.window)
            return False
        elif not (self.t4.get().isdigit()) or len(self.t4.get()) <= 8:
            messagebox.showwarning("Input Error", "Enter Valid UID No ", parent=self.window)
            return False

        elif not (self.t8.get().isdigit()):
            messagebox.showwarning("Input Error", "Enter total guest ", parent=self.window)
            return False
        return True


if __name__ == '__main__':
    dummy_homepage = Tk()
    BookingClass(dummy_homepage)
    dummy_homepage.mainloop()


