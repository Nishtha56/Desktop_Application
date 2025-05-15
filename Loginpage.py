from tkinter import *
from tkinter import messagebox
import pymysql


class LoginClass:
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
        self.window.maxsize(w1, h1)
        self.window.geometry("%dx%d+%d+%d" % (w1, h1, x1, y1))

        self.window.title("College Manager/Login")

        #-------------------------background image------------------------

        from PIL import Image, ImageTk

        self.b = Image.open("images//hotel.jpg")

        self.bk = ImageTk.PhotoImage(self.b)
        self.blbl = Label(self.window, image=self.bk)
        self.blbl.place(x=0, y=0, width=w1, height=h1)

        # --------------------- widgets -----------------------------------------------

        mycolor = '#b6cbfe'
        mycolor2 = '#1449cb'
        myfont1 = ('Trebuchet MS', 15)

        self.window.config(background=mycolor)

        self.hdlbl = Label(self.window,text="Welcome to Hotel Manager",background=mycolor2,
                           font=("Georgia",35,'bold'),relief='groove',borderwidth=10,foreground='white')
        self.L1 = Label(self.window,text="Username",background='#FFC5C5',font=myfont1)
        self.L2 = Label(self.window,text="Password",background='#FFC5C5',font=myfont1)

        self.t1 = Entry(self.window,font=myfont1)
        self.t2 = Entry(self.window,font=myfont1,show='*')

        #-------------- buttons -----------------------------------------------

        self.b1 = Button(self.window,text="Login",background=mycolor2,foreground='white',
                         font=myfont1,command=self.checkData)

        #-------------- placements -----------------------------------------------
        self.hdlbl.pack()
        x1 = 180
        y1 = 150

        x_diff=150
        y_diff=50

        self.L1.place(x=x1,y=y1)
        self.t1.place(x=x1+x_diff,y=y1)

        y1+=y_diff
        self.L2.place(x=x1,y=y1)
        self.t2.place(x=x1+x_diff,y=y1)

        y1+=y_diff
        self.b1.place(x=x1+x_diff,y=y1,width=200,height=40)

        self.databaseConnection()
        self.clearPage()
        self.window.mainloop()

    def databaseConnection(self):
        try:
            self.conn = pymysql.connect(host="localhost",db="hotel_manager_db",user="root",password="")
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showinfo("Database Error","Database Connection Error : \n"+str(e),parent=self.window)


    def checkData(self):
        try:
            qry = "select * from usertable where username=%s and password=%s"
            rowcount = self.curr.execute(qry,(self.t1.get(),self.t2.get()))
            data = self.curr.fetchone()
            self.clearPage()
            if data:
                uname=data[0]
                utype=data[2]
                self.window.destroy()
                from homepage import Homepage
                Homepage(uname,utype)


            else:
                messagebox.showwarning("Empty", "Wrong username or password", parent=self.window)

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
        return True


if __name__ == '__main__':
    LoginClass()