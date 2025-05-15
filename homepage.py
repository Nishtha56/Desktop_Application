from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from booking import BookingClass
from bookingreport import Report1Class
from roomdetails import RoomClass
from report2 import  Report2Class
from ManageUser import UserClass
from PIL import Image,ImageTk
from ChangePassword import  ChangePasswordClass


class Homepage:
    def __init__(self,uname,utype):

        self.uname=uname
        self.utype=utype

        self.window=Tk()
        self.window.title('Hotel Manager')
        self.window.config(background='#c1d1f8')

        mycolor2='#032881'
        mycolor='#1449cb'
        myfont1='latin'

       # -----setting-----------
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        self.window.geometry("%dx%d+%d+%d" % (w, h, 0, 0))

        from PIL import Image, ImageTk

        self.b = Image.open("images//hotel3.jpg")

        self.bk = ImageTk.PhotoImage(self.b)
        self.blbl = Label(self.window, image=self.bk)
        self.blbl.place(x=0, y=0, width=w, height=h)

        #---------------------topic--------
        self.hd = Label(self.window, text='   HOTEL MANAGEMENT   ', background='blue', font=('georgia', 40, 'bold'),
                           relief='ridge', borderwidth=10, foreground='#b6cbfe')
        self.hd.config(background=mycolor)



        #--------buttons----------------------

        self.btn_img1 = Image.open('images//booking.png').resize((20, 30))
        self.btn_pimg1 = ImageTk.PhotoImage(self.btn_img1)

        self.b1 = Button(self.window, text='BOOKING', background=mycolor2, foreground='#b6cbfe',
                         font=myfont1,relief='groove',borderwidth=15,width=30,
                         command=lambda : BookingClass(self.window),image=self.btn_pimg1,compound=LEFT)

        self.btn_img2 = Image.open('images//room.jpg').resize((20, 30))
        self.btn_pimg2 = ImageTk.PhotoImage(self.btn_img2)

        self.b2 = Button(self.window, text='ROOM DETAILS', background=mycolor2, foreground='#b6cbfe',
                         font=myfont1,relief='groove',borderwidth=15,width=30,command=lambda : RoomClass(self.window),
                         image=self.btn_pimg2,compound=LEFT)


        self.btn_img4 = Image.open('images//user2.jpg').resize((20, 30))
        self.btn_pimg4 = ImageTk.PhotoImage(self.btn_img4)

        self.b4 = Button(self.window, text='CHANGE PASSWORD', background=mycolor2, foreground='#b6cbfe',
                         font=myfont1,relief='groove',borderwidth=15,width=30,command=lambda : ChangePasswordClass(self.window,self.uname),
                         image=self.btn_pimg4,compound=LEFT)

        self.btn_img5 = Image.open('images//logo.png').resize((20, 30))
        self.btn_pimg5 = ImageTk.PhotoImage(self.btn_img5)

        self.b5 = Button(self.window, text='BOOKING REPORT', background=mycolor2, foreground='#b6cbfe',
                         font=myfont1, relief='groove', borderwidth=15, width=30,command=lambda : Report2Class(self.window),
                         image=self.btn_pimg5,compound=LEFT)

        self.btn_img6 = Image.open('images//logo.png').resize((20, 30))
        self.btn_pimg6 = ImageTk.PhotoImage(self.btn_img6)

        self.b6 = Button(self.window, text='BOOKING DATE REPORT', background=mycolor2, foreground='#b6cbfe',
                         font=myfont1, relief='groove', borderwidth=15,
                         width=30,command=lambda : Report1Class(self.window),image=self.btn_pimg6,compound=LEFT)

        self.btn_img7 = Image.open('images//user.jpg').resize((30, 30))
        self.btn_pimg7 = ImageTk.PhotoImage(self.btn_img7 )

        self.b7 = Button(self.window, text='USER', background=mycolor2, foreground='#b6cbfe',
                         font=myfont1, relief='groove', borderwidth=15, width=30,command=lambda : UserClass(self.window),
                         image=self.btn_pimg7,compound=LEFT)


        self.btn_img8=Image.open('images//primary-logout.png').resize((20,30))
        self.btn_pimg8=ImageTk.PhotoImage(self.btn_img8)


        self.b8 = Button(self.window, text='LOG OUT', background=mycolor2, foreground='#b6cbfe',
                         font=myfont1, relief='groove', borderwidth=15,width=30, image=self.btn_pimg8,compound=LEFT,command=self.quitter)


        if self.utype=="Employee":
            self.b4.config(state='disabled')
            self.b7.config(state='disabled')




        #------------------------PLACEMENT=-------------------------

        self.hd.pack()
        self.b1.place(x=270,y=150,width=310,height=80)
        self.b2.place(x=270,y=300,width=310,height=80)
        self.b7.place(x=270,y=450,width=310,height=80)
       # self.b3.place(x=270,y=450,width=310,height=80)
        self.b5.place(x=790, y=150,width=310,height=80)
        self.b6.place(x=790, y=300,width=310,height=80)
        self.b4.place(x=790, y=450,width=310,height=80)
        self.b8.place(x=500, y=600,width=310,height=80)

        self.window.mainloop()

    def quitter(self):
        ans = messagebox.askquestion("Confirmation", "Are you to Logout?", parent=self.window)
        if ans == 'yes':
            self.window.destroy()
            from Loginpage import LoginClass
            LoginClass()

