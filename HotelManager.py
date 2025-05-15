from tkinter import *
from tkinter import messagebox
import pymysql
class MainClass:
    def __init__(self):
        self.databaseConnection()
        try:
            qry = "select * from usertable"
            rowcount = self.curr.execute(qry)
            data = self.curr.fetchone()
            if data:
                from Loginpage import LoginClass
                LoginClass()
            else:
                from ManageUser import CreateUserClass
                CreateUserClass()

        except Exception as e:
            messagebox.showerror("Query Error", "Query Error : \n" + str(e))


    def databaseConnection(self):
        try:
            self.conn = pymysql.connect(host="localhost",db="hotel_manager_db",user="root",password="")
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showinfo("Database Error","Database Connection Error : \n"+str(e))


if __name__ == '__main__':
    MainClass()

