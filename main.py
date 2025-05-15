from tkinter import *
from tkinter.ttk import Combobox, Treeview
from tkinter import messagebox
import pymysql
from tkcalendar import DateEntry

class RoomClass:
    def __init__(self, home_window):
        self.window = Toplevel(home_window)

        self.window.title('Hotel Manager/ROOM DETAILS')
        self.window.config(background='#c1d1f8')

        # -----setting-----------
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        w1 = int(w - 100)
        h1 = int(h - 180)

        self.window.minsize(w1, h1)
        self.window.geometry("%dx%d+%d+%d" % (w1, h1, 50, 70))

        mycolor = '#032881'
        mycolor2 = '#1449cb'
        myfont1 = ('Trebuchet MS', 15)

        self.hdlbl = Label(self.window, text='BOOKING SLOT', background=mycolor2, font=('Georgia', 35, 'bold'),
                           relief='groove', borderwidth=10, foreground='white')
        self.hdlbl.config(background=mycolor)
        self.l1 = Label(self.window, text='Reg_No', background='#c1d1f8', font=myfont1)
        self.l2 = Label(self.window, text='Room Type', background='#c1d1f8', font=myfont1)
        self.l3 = Label(self.window, text='Room no.', background='#c1d1f8', font=myfont1)

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

        self.t1 = Entry(self.window, font=myfont1)

        self.v1 = StringVar()
        self.c1 = Combobox(self.window, values=('AC', 'Non AC'), state='readonly', textvariable=self.v1, font=myfont1,
                           width=18)
        self.v1.set('Choose Room')



        if self.v1=='AC':
            self.v2 = StringVar()
            self.c2 = Combobox(self.window, values=('1','2','3','4','5'), state='readonly', textvariable=self.v2, font=myfont1,
                           width=18)
            self.v2.delete('5')
            self.v2.set('Room no.')



        # ---------------- table -------------

        self.mytable = Treeview(self.window, columns=['c1', 'c2', 'c3'], height=20)
        self.mytable.heading('c1', text='Reg_No')
        self.mytable.heading('c2', text='Room Type')
        self.mytable.heading('c3', text='Room no.')

        self.mytable['show'] = 'headings'

        self.mytable.column("#1", width=250, anchor='center')
        self.mytable.column("#2", width=250, anchor='center')
        self.mytable.column("#3", width=250, anchor='center')

        self.mytable.bind("<ButtonRelease-1>", lambda e: self.getSelectedRowData())

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
        self.c1.place(x=x1 + x_diff, y=y1)

        y1 += y_diff
        self.l3.place(x=x1, y=y1)
        self.c2.place(x=x1 + x_diff, y=y1)

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
            qry = 'insert into roominfo_table values(%s,%s,%s)'
            rowcount = self.curr.execute(qry, (
                self.t1.get(),self.v1.get(),self.v2.get(),self.v3.get()))
            self.conn.commit()
            if rowcount == 1:
                messagebox.showinfo('Success', 'Room Added Successfully :)', parent=self.window)
                self.clearPage()
        except Exception as e:
            messagebox.showerror('Query Error', 'Querry Error : \n ' + str(e), parent=self.window)

    def updateData(self):
        if self.validate_check() == False:
            return

        try:
            qry = "update booking_table set Room_Type=%s,Room_no where Reg_No=%s "
            rowcount = self.curr.execute(qry, (self.v1.get(),self.v2.get(),self.v3.get()))
            self.conn.commit()
            if rowcount == 1:
                messagebox.showinfo("Sucess", "Room Update successfully :)", parent=self.window)
                self.clearPage()
        except Exception as e:
            messagebox.showerror("Query Error", "Query Error : \n" + str(e), parent=self.window)

    def deleteData(self):

        ans = messagebox.askquestion("Confirmation", "Are you to delete?", parent=self.window)
        if ans == 'yes':
            try:
                qry = "delete from roominfo_table where Reg_Id=%s "
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

    def fetchData(self, pk_col=None):
        if pk_col == None:
            Reg_No = self.t1.get()
        else:
            Reg_No = pk_col
        try:
            qry = "select * from roominfo_table where Reg_No=%s"
            rowcount = self.curr.execute(qry, (Reg_No))
            data = self.curr.fetchone()

            self.clearPage()
            self.clearPage()
            if data:
                self.t1.insert(0, data[0])
                self.v1.set(data[1])
                self.v2.set(data[2])

            else:
                messagebox.showwarning("Empty", "No Record Found", parent=self.window)
        except Exception as e:
            messagebox.showerror("Query Error", "Query Error : \n" + str(e), parent=self.window)

    def getAllData(self):
        try:
            self.mytable.delete(*self.mytable.get_children())

            qry = "select * from roominfo_table where Room_no like %s "
            rowcount = self.curr.execute(qry, (self.c2.get() + "%"))
            data = self.curr.fetchall()
            if data:
                for myrow in data:
                    self.mytable.insert("", END, values=myrow)

            else:
                messagebox.showwarning("Empty", "No Record Found", parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error", "Query Error : \n" + str(e), parent=self.window)

    def clearPage(self):
        self.t1.delete(0, END)
        self.v1.set(None)
        self.v2.set(None)

    def validate_check(self):
        if not (self.t1.get().isdigit()) or len(self.t1.get()) < 1:
            messagebox.showwarning("Validation Check", "Invalid Registration no.", parent=self.window)
            return False
        elif (self.v1.get() == "None") :
            messagebox.showwarning("Input Error", "Please Select Room Type ", parent=self.window)
            return False

        elif (self.v2.get() == "None"):
            messagebox.showwarning("Input Error", "Please Select Room No.", parent=self.window)
            return False
        return True




if __name__ == '__main__':
    dummy_homepage = Tk()
    RoomClass(dummy_homepage)
    dummy_homepage.mainloop()