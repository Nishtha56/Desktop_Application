from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import pymysql
class UserClass:
    def __init__(self,home_window):
        self.window = Toplevel(home_window)
        # -------------settings ----------------------------
        self.window.title("Hotel Manager")
        w= self.window.winfo_screenwidth()
        h= self.window.winfo_screenheight()
        w1 = int(w-100)
        h1 = int(h-180)

        self.window.minsize(w1,h1)
        self.window.geometry("%dx%d+%d+%d"%(w1,h1,0,0))
        self.window.title("Hotel Manager/USER")


        # --------------------- widgets -----------------------------------------------

        mycolor = '#b6cbfe'
        mycolor2 = '#1449cb'
        myfont1 = ('Trebuchet MS', 15)

        self.window.config(background=mycolor)

        self.hdlbl = Label(self.window,text="USER",background=mycolor2,
                           font=("Georgia",35,'bold'),relief='groove',borderwidth=10,foreground='white')
        self.L1 = Label(self.window,text="Username",background=mycolor,font=myfont1)
        self.L2 = Label(self.window,text="Password",background=mycolor,font=myfont1)
        self.L3 = Label(self.window,text="Usertype",background=mycolor,font=myfont1)

        self.t1 = Entry(self.window,font=myfont1)
        self.t2 = Entry(self.window,font=myfont1,show='*')
        self.v1=StringVar()
        self.c1=Combobox(self.window,values=("Admin","Employee"),textvariable=self.v1,
                         state='readonly',font=myfont1)

        #---------------- table -------------

        self.mytable = Treeview(self.window,columns=['c1','c2'],height=20)
        self.mytable.heading('c1',text='Username')
        self.mytable.heading('c2',text='Usertype')

        self.mytable['show']='headings'

        self.mytable.column("#1",width=250,anchor='center')
        self.mytable.column("#2",width=250,anchor='center')
        self.mytable.bind("<ButtonRelease-1>",lambda e: self.getSelectedRowData())

        #-------------- buttons -----------------------------------------------

        self.b1 = Button(self.window,text="Save",background=mycolor2,foreground='white',font=myfont1,command=self.saveData)
        self.b2 = Button(self.window,text="Update",background=mycolor2,foreground='white',font=myfont1,command=self.updateData)
        self.b3 = Button(self.window,text="Delete",background=mycolor2,foreground='white',font=myfont1,command=self.deleteData)
        self.b4 = Button(self.window,text="Fetch",background=mycolor2,foreground='white',font=myfont1,command=self.fetchData)
        self.b5 = Button(self.window,text="Search",background=mycolor2,foreground='white',font=myfont1,command=self.getAllData)

        #-------------- placements -----------------------------------------------
        self.hdlbl.place(x=0,y=0,width=w1+100,height=80)
        x1 = 20
        y1 = 100

        x_diff=150
        y_diff=50

        self.L1.place(x=x1,y=y1)
        self.t1.place(x=x1+x_diff,y=y1)
        self.b4.place(x=x1+x_diff+x_diff+90,y=y1,width=100,height=30)
        self.mytable.place(x=x1+x_diff+x_diff+300,y=y1)

        y1+=y_diff
        self.L2.place(x=x1,y=y1)
        self.t2.place(x=x1+x_diff,y=y1)
        y1+=y_diff
        self.L3.place(x=x1,y=y1)
        self.c1.place(x=x1+x_diff,y=y1)
        self.b5.place(x=x1+x_diff+x_diff+90,y=y1,width=100,height=30)
        y1+=y_diff
        self.b1.place(x=x1,y=y1,width=100,height=40)
        self.b2.place(x=x1+x_diff+10,y=y1,width=100,height=40)
        self.b3.place(x=x1+x_diff+x_diff+20,y=y1,width=100,height=40)

        self.databaseConnection()
        self.clearPage()
        self.window.mainloop()

    def databaseConnection(self):
        try:
            self.conn = pymysql.connect(host="localhost",db="hotel_manager_db",user="root",password="")
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showinfo("Database Error","Database Connection Error : \n"+str(e),parent=self.window)

    def saveData(self):
        if self.validate_check()==False:
            return
        try:
            qry = "insert into usertable values(%s,%s,%s)"
            rowcount = self.curr.execute(qry,(self.t1.get(), self.t2.get(),self.v1.get()))
            self.conn.commit()
            if rowcount==1:
                messagebox.showinfo("Sucess","User Added successfully :)",parent=self.window)
                self.clearPage()
        except Exception as e:
            messagebox.showerror("Query Error", "Query Error : \n" + str(e), parent=self.window)

    def updateData(self):
        if self.validate_check()==False:
            return
        try:
            qry = "update usertable set password=%s, usertype=%s where username=%s "
            rowcount = self.curr.execute(qry,(self.t2.get(), self.v1.get(),self.t1.get()))
            self.conn.commit()
            if rowcount==1:
                messagebox.showinfo("Sucess","User Updated successfully :)",parent=self.window)
                self.clearPage()
        except Exception as e:
            messagebox.showerror("Query Error", "Query Error : \n" + str(e), parent=self.window)

    def deleteData(self):
        ans = messagebox.askquestion("Confirmation","Are you to delete?",parent=self.window)
        if ans=='yes':
            try:
                qry = "delete from usertable where username=%s "
                rowcount = self.curr.execute(qry,(self.t1.get()))
                self.conn.commit()
                if rowcount==1:
                    messagebox.showinfo("Sucess","User deleted successfully :)",parent=self.window)
                    self.clearPage()
            except Exception as e:
                messagebox.showerror("Query Error", "Query Error : \n" + str(e), parent=self.window)

    def getSelectedRowData(self):
        row_id = self.mytable.focus()
        rowdata = self.mytable.item(row_id)
        row_values = rowdata['values']
        cols_data = row_values[0]
        self.fetchData(cols_data)

    def fetchData(self,pk_col=None):
        if pk_col==None:
            uname = self.t1.get()
        else:
            uname=pk_col
        try:
            qry = "select * from usertable where username=%s"
            rowcount = self.curr.execute(qry,(uname))
            data = self.curr.fetchone()
            self.clearPage()
            if data:
                self.t1.insert(0,data[0])
                self.t2.insert(0,data[1])
                self.v1.set(data[2])

            else:
                messagebox.showwarning("Empty", "No Record Found", parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error", "Query Error : \n" + str(e), parent=self.window)

    def clearPage(self):
        self.t1.delete(0,END)
        self.t2.delete(0,END)
        self.v1.set("Choose Usertype")

    def getAllData(self):
        try:
            self.mytable.delete(*self.mytable.get_children())

            qry = "select * from usertable where usertype like %s "
            rowcount = self.curr.execute(qry,(self.v1.get()+"%"))
            data = self.curr.fetchall()

            if data:
                for myrow in data:
                    my_new_row = [myrow[0],myrow[2]]
                    self.mytable.insert("",END,values=my_new_row)

            else:
                messagebox.showwarning("Empty", "No Record Found", parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error", "Query Error : \n" + str(e), parent=self.window)


    def validate_check(self):
        if len(self.t1.get())<1:
            messagebox.showwarning("Validation Check", "Enter Username", parent=self.window)
            return False
        elif len(self.t2.get())<1:
            messagebox.showwarning("Validation Check", "Enter Password", parent=self.window)
            return False
        elif self.v1.get() == "Choose Usertype":
            messagebox.showwarning("Input Error", "Please Select Department ", parent=self.window)
            return False
        return True


if __name__ == '__main__':
    dummy_homepage = Tk()
    UserClass(dummy_homepage)
    dummy_homepage.mainloop()