from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import pymysql
from tkcalendar import DateEntry


class Report1Class:
    def __init__(self,home_window):
        self.window = Toplevel(home_window)
        # -------------settings ----------------------------
        self.window.title("Hotel Manager")
        w= self.window.winfo_screenwidth()
        h= self.window.winfo_screenheight()
        w1 = int(w-100)
        h1 = int(h-180)
        self.window.minsize(w1,h1)
        self.window.geometry("%dx%d+%d+%d"%(w1,h1,50,70))
        self.window.title("Hotel Manager/Booking Report")
        from PIL import Image, ImageTk

        self.b = Image.open("images//room2.jpg")

        self.bk = ImageTk.PhotoImage(self.b)
        self.blbl = Label(self.window, image=self.bk)
        self.blbl.place(x=0, y=0, width=w, height=h)


        # --------------------- widgets -----------------------------------------------

        mycolor = '#b6cbfe'
        mycolor2 = '#1449cb'
        myfont1 = ('Trebuchet MS', 15)

        self.window.config(background=mycolor)

        self.hdlbl = Label(self.window,text="BOOKING DATE",background=mycolor2,
                           font=("Georgia",35,'bold'),relief='groove',borderwidth=10,foreground='white')





        self.L1 = Label(self.window,text="Check In",font=myfont1)
        self.L2 = Label(self.window,text="Check Out",font=myfont1)
        self.t1 = DateEntry(self.window, width=12, background=mycolor2, foreground='white',
                            borderwidth=2, year=2023,font=myfont1,date_pattern='y-mm-dd')
        self.t2 = DateEntry(self.window, width=12, background=mycolor2, foreground='white',
                            borderwidth=2, year=2023,font=myfont1,date_pattern='y-mm-dd')



        #---------------- table -------------

        self.mytable = Treeview(self.window,columns=['c1','c2','c3','c4','c5','c6','c7'],height=10)
        self.mytable.heading('c1', text='Reg_No')
        self.mytable.heading('c2', text='Name')
        self.mytable.heading('c3', text='Phone')
        self.mytable.heading('c4', text='UID')
        self.mytable.heading('c5', text='Check_In')
        self.mytable.heading('c6', text='Check_Out')
        self.mytable.heading('c7', text='Total_Guest')
        self.mytable['show']='headings'

        self.mytable.column("#1",width=500,anchor='center')
        self.mytable.column("#2",width=200,anchor='center')
        self.mytable.column("#3",width=150,anchor='center')
        self.mytable.column("#4",width=150,anchor='center')
        self.mytable.column("#5",width=100,anchor='center')
        self.mytable.column("#6",width=100,anchor='center')
        self.mytable.column("#7",width=100,anchor='center')



        #-------------- buttons -----------------------------------------------

        self.b1 = Button(self.window,text="Search",background=mycolor2,
                         foreground='white',font=myfont1,command=self.getAllData)

        #-------------- placements -----------------------------------------------
        self.hdlbl.place(x=0,y=0,width=w1+100,height=80)
        x1 = 20
        y1 = 100

        x_diff=150
        y_diff=50

        self.L1.place(x=x1,y=y1)
        self.t1.place(x=x1+100,y=y1)
        self.L2.place(x=x1+300,y=y1)
        self.t2.place(x=x1+420,y=y1)
        self.b1.place(x=x1+600,y=y1,width=100,height=35)
        y1+=y_diff

        self.mytable.place(x=x1,y=y1)

        self.databaseConnection()
        self.window.mainloop()

    def databaseConnection(self):
        try:
            self.conn = pymysql.connect(host="localhost",db="hotel_manager_db",user="root",password="")
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showinfo("Database Error","Database Connection Error : \n"+str(e),parent=self.window)


    def getAllData(self):

        self.mytable.delete(*self.mytable.get_children())

        try:
            qry = "select * from booking_table  where Check_In and Check_Out between %s and %s"
            rowcount = self.curr.execute(qry,(self.t1.get_date(),self.t2.get_date()))
            data = self.curr.fetchall()

            if data:
                for myrow in data:
                    self.mytable.insert("",END,values=myrow)

            else:
                messagebox.showwarning("Empty", "No Record Found", parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error", "Query Error : \n" + str(e), parent=self.window)


if __name__ == '__main__':
    dummy_homepage = Tk()
    Report1Class(dummy_homepage)
    dummy_homepage.mainloop()
