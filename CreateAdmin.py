from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import pymysql
class CreateUserClass:
    def __init__(self):
        self.window = Tk()
        # -------------settings ----------------------------
        self.window.title("Hotel Manager")
        w= self.window.winfo_screenwidth()
        h= self.window.winfo_screenheight()
        w1 = int(w/2)
        h1 = int(h/2 )
        x1 = int(w/2 - w/4)
        y1 = int(h/2 - h/4)

        self.window.minsize(w1,h1)
        self.window.maxsize(w1,h1)
        self.window.geometry("%dx%d+%d+%d"%(w1,h1,x1,y1))  # width,height,x,y
        self.window.title("Hotel Manager/Create Admin")

        #------------------------------background-------------------------------------
        from PIL import Image, ImageTk

        self.b = Image.open("images//hotel.jpg")

        self.bk = ImageTk.PhotoImage(self.b)
        self.blbl = Label(self.window, image=self.bk)
        self.blbl.place(x=0, y=0, width=w1, height=h1)


        # --------------------- widgets -----------------------------------------------

        mycolor = '#032881'
        mycolor2 = '#1449cb'
        myfont1 = ('Trebuchet MS', 15)

        self.window.config(background=mycolor)

        self.hdlbl = Label(self.window,text="Welcome to Hotel Manager",background=mycolor2,
                           font=("Georgia",35,'bold'),relief='groove',borderwidth=10,foreground='white')
        self.L1 = Label(self.window,text="Username",background='#FFC5C5',font=myfont1)
        self.L2 = Label(self.window,text="Password",background='#FFC5C5',font=myfont1)
        self.L3 = Label(self.window,text="Usertype",background='#FFC5C5',font=myfont1)

        self.t1 = Entry(self.window,font=myfont1)
        self.t2 = Entry(self.window,font=myfont1,show='*')
        self.v1=StringVar()
        self.c1=Combobox(self.window,values=("Admin","Employee"),textvariable=self.v1,
                         state='disabled',font=myfont1)
        self.c1.current(0)


        #-------------- buttons -----------------------------------------------

        self.b1 = Button(self.window,text="Save",background=mycolor2,foreground='white',
                         font=myfont1,command=self.saveData)

        #-------------- placements -----------------------------------------------
        self.hdlbl.pack()
        x1 =160
        y1 = 200

        x_diff=150
        y_diff=50

        self.L1.place(x=x1,y=y1)
        self.t1.place(x=x1+x_diff,y=y1)

        y1+=y_diff
        self.L2.place(x=x1,y=y1)
        self.t2.place(x=x1+x_diff,y=y1)
        y1+=y_diff
        self.L3.place(x=x1,y=y1)
        self.c1.place(x=x1+x_diff,y=y1)
        y1+=y_diff
        self.b1.place(x=x1,y=y1,width=100,height=40)

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
                self.window.destroy()
                from Loginpage import LoginClass
                LoginClass()
        except Exception as e:
            messagebox.showerror("Query Error", "Query Error : \n" + str(e), parent=self.window)

    def clearPage(self):
        self.t1.delete(0,END)
        self.t2.delete(0,END)

    def validate_check(self):
        if len(self.t1.get())<1:
            messagebox.showwarning("Validation Check", "Enter Username", parent=self.window)
            return False
        elif len(self.t2.get())<1:
            messagebox.showwarning("Validation Check", "Enter Password", parent=self.window)
            return False
        elif self.v1.get() == "Choose Usertype":
            messagebox.showwarning("Input Error", "Please Select User Type ", parent=self.window)
            return False
        return True


if __name__ == '__main__':
    CreateUserClass()
