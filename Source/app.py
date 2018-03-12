#Incase performance issues use tkraise
import tkMessageBox as box
import os
import pickle
import time
import Tix
import db
import os
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter
    #import Tkinter as tk
except ImportError:
    # for Python3
    from tkinter import *
    #import tkinter as tk

class InitialPage(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.parent = master
        self.parent.title("Initial Page")
        self.parent.configure(background="#2d3339")
        self.centerWindow()

        self.option_label=Label(master, text='CHOOSE TO SIGN-UP/LOGIN', font=('Lato',20), fg='#fff', background='#2d3339')
        self.option_label.place(x=110,y=120)

        self.openlogin_label = Button(master, text="Log In", font=("Lato", 18), borderwidth=0, command=self.openlogin, background='#c92d22', fg='#fff', height=1, width=10)
        self.openlogin_label.place(x= 140, y = 300)

        self.opensignup_label = Button(master, text="Sign Up", font=("Lato", 18), borderwidth=0, command=self.opensignup, background='#c92d22', fg='#fff', height=1, width=10)
        self.opensignup_label.place(x= 340, y =300)

        self.quit = Button(master, text="Quit", font=("Lato", 18), command=self.quit, borderwidth=0, background='#c92d22', fg='#fff', height=1, width=5)
        self.quit.place(x= 480, y = 425)

    def openlogin(self):
        self.parent.destroy()
        login = Tk()
        framelogin = frame_login(login)
        login.mainloop()
        login.destroy()

    def opensignup(self):
        self.parent.destroy()
        signup = Tk()
        framesignup = frame_signup(signup)
        signup.mainloop()
        signup.destroy()

    def centerWindow(self):
        w = self.parent.winfo_screenwidth()
        h = self.parent.winfo_screenheight()
        x = w/2 - 225
        y = h/2 - 225

        self.parent.geometry("%dx%d+%d+%d" %(600,500,x,y))
        self.parent.resizable(0,0)
    def quit(self):
        self.parent.destroy()

    def database(self):
        ret = db.setup_check()
        if(ret != 1416):
            box.showerror('ERROR',"DATABASE CAN NOT BE SET UP OR ACCESSED")

class frame_login(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.parent = master
        self.parent.title("Login")
        self.parent.configure(background="#2d3339")
        #self.pack()
        self.centerWindow()

        self.login_label=Label(master, text='LOGIN SCREEN', font=('Lato',20), fg='#fff', background='#2d3339')
        self.login_label.place(x=180,y=120)

        self.user_label=Label(master, text="Enter your\nusername: ",  font=("Lato", 18), fg='#fff', background='#1EBBA6', width=20)
        self.user_label.place(x=0,y=190)

        self.pass_label=Label(master, text="Enter your\npassword: ",  font=("Lato", 18), fg='#fff', background='#16776A', width=20)
        self.pass_label.place(x=0,y=250)

        self.entry_user = Entry(master, width = 25, borderwidth=0, font=("Calibri Light", 35),background='#16776A',fg='#fff')
        self.entry_user.place(x=286, y=190)

        self.entry_pass = Entry(master,show="*",width = 25, borderwidth=0, font=("Calibri Light", 35),background='#1EBBA6',fg='#fff')
        self.entry_pass.place(x=286, y=250)

        self.login = Button(master, text="Log In", font=("Lato", 18), borderwidth=0, command=self.login, background='#c92d22', fg='#fff', height=1, width=10)
        self.login.place(x= 140, y = 339)

        self.back = Button(master, text="Back", font=("Lato", 18), borderwidth=0, command=self.back, background='#c92d22', fg='#fff', height=1, width=10)
        self.back.place(x= 300, y = 339)

    def back(self):
        self.parent.destroy()
        #InitialPage.__init__(self,master)
        intialpage = Tk()
        #InitialPage.__init__(self,master)
        intial_page = InitialPage(intialpage)
        intialpage.mainloop()
        intialpage.destroy()
    def centerWindow(self):
        w = self.parent.winfo_screenwidth()
        h = self.parent.winfo_screenheight()
        x = w/2 - 225
        y = h/2 - 225

        self.parent.geometry("%dx%d+%d+%d" %(600,500,x,y))
        self.parent.resizable(0,0)

    def clear(self):
        self.entry_user.delete(0,'end')
        self.entry_pass.delete(0,'end')


    def login(self):
        global a
        self.username=self.entry_user.get().lower()
        a=self.username
        self.password=self.entry_pass.get()
        obj = db.User(self.username,self.password)

        if(len(self.username) == 0):
            self.clear()
            box.showerror('ERROR',"Username cannot be empty")
        elif(len(self.password) == 0):
            self.clear()
            box.showerror('ERROR',"Password cannot be empty")
        else:
            fin = obj.check()
            print fin
            if(fin == 0):
                self.clear()
                box.showerror('ERROR',"Username doesn't exist")
            elif(fin == 1):
                fin = obj.check()
                if(fin == 0):
                    box.showerror('ERROR',"Username doesn't exist")
                elif(fin == 1):
                    os.system("say CORRECT PASSWORD")
                    if obj.uclass=="emp":
                        print "ayush"
                        self.parent.destroy()
                        employee=Tk()
                        emp=Employee(employee)
                        '''emp.att1=obj.name
                        emp.att2=obj.pwd
                        emp.att3=obj.email
                        emp.att4=obj.uclass'''
                        employee.mainloop()
                        employee.destroy()
                    elif obj.uclass=="mas":
                        self.parent.destroy()
                        master=Tk()
                        mas=Master(master)
                        master.mainloop()
                        master.destroy()





class frame_signup(Frame):
    def __init__(self, master=None):
        #def __init__(self,parent):
        #.__init__(self,parent)
        Frame.__init__(self,master)
        self.parent = master
        self.parent.title("Sign-up")
        self.parent.configure(background="#2d3339")
        self.centerWindow()

        self.signup_label=Label(master, text='SIGN-UP SCREEN', font=('Lato',20), fg='#fff', background='#2d3339')
        self.signup_label.place(x=180,y=120)

        self.user_label=Label(master, text="Choose your\nusername: ",  font=("Lato", 18), fg='#fff', background='#1EBBA6', width=20)
        self.user_label.place(x=0,y=190)

        self.pass_label=Label(master, text="Choose your\npassword: ",  font=("Lato", 18), fg='#fff', background='#16776A', width=20)
        self.pass_label.place(x=0,y=250)

        self.entry_user = Entry(master, width = 25, borderwidth=0, font=("Calibri Light", 35),background='#16776A',fg='#fff')
        self.entry_user.place(x=286, y=190)

        self.entry_pass = Entry(master,show="*",width = 25, borderwidth=0, font=("Calibri Light", 35),background='#1EBBA6',fg='#fff')
        self.entry_pass.place(x=286, y=250)

        self.email_label=Label(master, text="Add your\nEmail ID: ",  font=("Lato", 18), fg='#fff', background='#1EBBA6', width=20)
        self.email_label.place(x=0,y=310)

        self.class_label=Label(master, text="Add your\nClass: ",  font=("Lato", 18), fg='#fff', background='#16776A', width=20)
        self.class_label.place(x=0,y=370)

        self.entry_email = Entry(master, width = 25, borderwidth=0, font=("Calibri Light", 35),background='#16776A',fg='#fff')
        self.entry_email.place(x=286, y=310)

        self.entry_class = Entry(master, width = 25, borderwidth=0, font=("Calibri Light", 35),background='#1EBBA6',fg='#fff')
        self.entry_class.place(x=286, y=370)

        self.signup = Button(master, text="Sign Up", font=("Lato", 18), borderwidth=0, command=self.signup, background='#c92d22', fg='#fff', height=1, width=10)
        self.signup.place(x= 300, y =430)

        self.back = Button(master, text="Back", font=("Lato", 18), borderwidth=0, command=self.back, background='#c92d22', fg='#fff', height=1, width=10)
        self.back.place(x= 140, y = 430)

    def back(self):
        self.parent.destroy()
        #InitialPage.__init__(self,master)
        intialpage = Tk()
        #InitialPage.__init__(self,master)
        intial_page = InitialPage(intialpage)
        intialpage.mainloop()
    def centerWindow(self):
        w = self.parent.winfo_screenwidth()
        h = self.parent.winfo_screenheight()
        x = w/2 - 225
        y = h/2 - 225

        self.parent.geometry("%dx%d+%d+%d" %(600,500,x,y))
        self.parent.resizable(0,0)

    def signup(self):
        self.username=self.entry_user.get()
        self.password=self.entry_pass.get()
        self.email=self.entry_email.get()
        self.classtype=self.entry_class.get()

        obj = db.User(self.username,self.password,self.email,self.classtype)
        fin = obj.sign_proc()

        if(fin == -1):
            box.showerror('ERROR',"USERNAME NOT UNIQUE RETRY!")
            self.entry_user.delete(0,'end')
            self.entry_pass.delete(0,'end')
        elif(fin == -2):
            box.showerror('ERROR',"Email ID already in use")
            self.entry_email.delete(0,'end')
            self.entry_pass.delete(0,'end')
        elif(fin == 0):
            box.showinfo('SUCCESS',"SIGNUP SUCCESSFUL")
            self.parent.destroy()
            fram = Tk()
            init = frame_login(fram)
            fram.mainloop()
            fram.detroy()

class Employee(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        '''self.att1 = att1
        self.att2 = att2
        self.att3 = att3
        self.att4 = att4'''
        self.parent = master
        self.parent.title("Employee")
        self.parent.configure(background="#2d3339")
        #self.pack()
        self.centerWindow()

        self.login_label=Label(master, text='EMPLOYEE SCREEN', font=('Lato',20), fg='#fff', background='#2d3339')
        self.login_label.place(x=170,y=120)


        self.bill = Button(master, text='Bill Calculation', font=('Lato', 18), borderwidth=0, command=self.bill_calc, background='#c92d22', fg='#fff', height=1, width=20)
        self.bill.place(x= 170, y = 180)

        self.tax = Button(master, text='Tax Calculation', font=('Lato', 18), borderwidth=0, command=self.taxcalc, background='#c92d22', fg='#fff', height=1, width=20)
        self.tax.place(x= 170, y = 240)
        self.transdata = Button(master, text='Add Transaction data', font=('Lato', 18), borderwidth=0, command=self.addtrans, background='#c92d22', fg='#fff', height=1, width=20)
        self.transdata.place(x= 170, y = 300)

        self.logout = Button(master, text='Back', font=('Lato', 18), borderwidth=0, command=self.logout, background='#c92d22', fg='#fff', height=1, width=10)
        self.logout.place(x= 400, y = 360)

    def bill_calc(self):
        os.system("say Bill Calculation" )
    def taxcalc(self):
        os.system("say Tax Calculation" )
    def addtrans(self):
        os.system("say Add Transaction Data" )


    def logout(self):
        self.parent.destroy()
        #InitialPage.__init__(self,master)
        intialpage = Tk()
        #InitialPage.__init__(self,master)
        intial_page = InitialPage(intialpage)
        intialpage.mainloop()
        intialpage.destroy()
    def centerWindow(self):
        w = self.parent.winfo_screenwidth()
        h = self.parent.winfo_screenheight()
        x = w/2 - 225
        y = h/2 - 225

        self.parent.geometry("%dx%d+%d+%d" %(600,500,x,y))
        self.parent.resizable(0,0)

#----DRIVER SECTION OF APP----#
root = Tk()
root.iconbitmap(r"Users/ayush/Desktop/virtualenvs/sw-lab/git/SW-Lab/Images/image.png")
app = InitialPage(master=root)
app.database()
app.mainloop()
root.destroy()
#----DRIVER SECTION OF APP----#
