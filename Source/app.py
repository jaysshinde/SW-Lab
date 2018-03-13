#Incase performance issues use tkraise
#Dump object data on logout
import tkMessageBox as box
import os
import pickle
import time
import Tix
import db
import em
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

#pass user attributes to dependent classes
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


class verify(Frame):
    def __init__(self,master = None,num = 0):
        Frame.__init__(self,master)
        self.parent = master
        self.parent.title("Verification")
        self.num = num
        self.parent.configure(background="#2d3339")
        self.centerWindow()

        self.verify_label=Label(master,text='Enter your verification code here',font=('Lato',10),fg='#fff',background='#2d3339')
        self.verify_label.grid(row = 0,column = 0)

        self.entry_verify=Entry(master, width = 8, borderwidth=0, font=("Calibri Light", 10),background='#1EBBA6',fg='#fff')
        self.entry_verify.grid(row=2,column = 1)

        self.button_verify=Button(master, text="Verify", font=("Lato", 10), borderwidth=0, command=self.verific, background='#c92d22', fg='#fff', height=1, width=5)
        self.button_verify.grid(row = 4,column = 1)

    def verific(self):
        self.code = int(self.entry_verify.get())

        if(self.code == self.num):
            box.showinfo('SUCCESS',"Signup Successful")
            self.parent.destroy()
        else:
            box.showerror('ERROR',"Codes do not match retry")
            self.parent.destroy()

    def centerWindow(self):
        w = self.parent.winfo_screenwidth()
        h = self.parent.winfo_screenheight()
        x = w/2 - 225
        y = h/2 - 225


#pass user attributes to dependent classes
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

    def clear(self):
        self.entry_user.delete(0,'end')
        self.entry_pass.delete(0,'end')
        self.entry_class.delete(0,'end')
        self.entry_email.delete(0,'end')

    def signup(self):
        self.username=self.entry_user.get()
        self.password=self.entry_pass.get()
        self.emaill=self.entry_email.get()
        self.classtype=self.entry_class.get()

        obj = db.User(self.username,self.password,self.emaill,self.classtype)
        if(len(self.username) == 0):
            self.clear()
            box.showerror('ERROR',"Username cannot be empty")
        elif(len(self.password) == 0):
            self.clear()
            box.showerror('ERROR',"Password cannot be empty")
        elif(len(self.emaill) == 0):
            self.clear()
            box.showerror('ERROR',"Email ID cannot be empty")
        else:
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
                res = em.sendemail_verify(obj.email)
                if(res[0] == 1):
                    frame = Tk()
                    obj = verify(frame)
                    obj.num = res[1]
                    frame.mainloop()
                    frame.destroy()
                    self.parent.destroy()
                    fram = Tk()
                    init = frame_login(fram)
                    fram.mainloop()
                    fram.destroy()
                else:
                    box.showerror('ERROR',"Could not send email, Retry")

#pass user attributes to dependent classes
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


        self.bill = Button(master, text='Bill/Tax Calculation', font=('Lato', 18), borderwidth=0, command=self.bill_calc, background='#c92d22', fg='#fff', height=1, width=20)
        self.bill.place(x= 170, y = 180)

        self.tax = Button(master, text='Add a Field', font=('Lato', 18), borderwidth=0, command=self.taxcalc, background='#c92d22', fg='#fff', height=1, width=20)
        self.tax.place(x= 170, y = 240)
        self.transdata = Button(master, text='Add Transaction data', font=('Lato', 18), borderwidth=0, command=self.addtrans, background='#c92d22', fg='#fff', height=1, width=20)
        self.transdata.place(x= 170, y = 300)

        self.logout = Button(master, text='Logout', font=('Lato', 18), borderwidth=0, command=self.logout, background='#c92d22', fg='#fff', height=1, width=10)
        self.logout.place(x= 400, y = 360)

    def bill_calc(self):
        os.system("say Bill Calculation" )
        billframe=Tk()
        bf=bill_frame(billframe)
        billframe.mainloop()
        billframe.destroy()
    def taxcalc(self):
        os.system("say Tax Calculation" )

    def addtrans(self):
        os.system("say Add Transaction Data" )
        transframe=Tk()
        tf=transaction_frame(transframe)
        transframe.mainloop()
        transframe.destroy()


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



#pass user attributes to dependent classes
class bill_frame(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.parent = master
        self.parent.title("Bill/Tax Calculation")
        self.parent.configure(background="#2d3339")
        self.centerWindow()
        #self.add_item = Button(master, text='Add New Item', font=('Lato', 15), borderwidth=0, command=self.additem, background='#c92d22', fg='#fff', height=1, width=10)
        #self.add_item.place(x= 600, y = 50)

        self.bill_label=Label(master, text='Add Billing/Tax Information', font=('Lato',20), fg='#fff', background='#2d3339')
        self.bill_label.place(x=50,y=50)
        self.done_item = Button(master, text='Done', font=('Lato', 15), borderwidth=0, command=self.done, background='#c92d22', fg='#fff', height=1, width=10)
        self.done_item.place(x= 400, y = 50)
        self.tid_label=Label(master, text="Add Transaction ID: ",  font=("Lato", 15), fg='#fff', background='#2d3339', width=15)
        self.tid_label.place(x=50,y=100)

        self.entry_tid = Entry(master, width = 25, borderwidth=0, font=("Calibri Light", 15),background='#16776A',fg='#fff')
        self.entry_tid.place(x=300, y=100)

        self.count=0
    def done(self):
        os.system("say Done")

    '''def additem(self):
        master=self.parent
        self.itemid_label=Label(master, text="Item ID: ",  font=("Lato", 15), fg='#fff', background='#1EBBA6', width=15)
        self.itemid_label.place(x=50,y=100+125*self.count)

        self.itemname_label=Label(master, text="Item Name: ",  font=("Lato", 15), fg='#fff', background='#16776A', width=15)
        self.itemname_label.place(x=50,y=125+125*self.count)

        self.entry_id = Entry(master, width = 25, borderwidth=0, font=("Calibri Light", 15),background='#16776A',fg='#fff')
        self.entry_id.place(x=150, y=100+125*self.count)

        self.entry_name = Entry(master,width = 25, borderwidth=0, font=("Calibri Light", 15),background='#1EBBA6',fg='#fff')
        self.entry_name.place(x=150, y=125+125*self.count)

        self.quan_label=Label(master, text="Quantity: ",  font=("Lato", 15), fg='#fff', background='#1EBBA6', width=15)
        self.quan_label.place(x=50,y=150+125*self.count)

        self.price_label=Label(master, text="Price: ",  font=("Lato", 15), fg='#fff', background='#16776A', width=15)
        self.price_label.place(x=50,y=175+125*self.count)

        self.entry_quan = Entry(master, width = 25, borderwidth=0, font=("Calibri Light", 15),background='#16776A',fg='#fff')
        self.entry_quan.place(x=150, y=150+125*self.count)

        self.entry_price = Entry(master, width = 25, borderwidth=0, font=("Calibri Light", 15),background='#1EBBA6',fg='#fff')
        self.entry_price.place(x=150, y=175+125*self.count)

        self.count+=1'''
    def centerWindow(self):
        w = self.parent.winfo_screenwidth()
        h = self.parent.winfo_screenheight()
        x = w/2 - 225
        y = h/2 - 225

        self.parent.geometry("%dx%d+%d+%d" %(800,600,x,y))
        self.parent.resizable(1,1)

#pass user attributes to dependent classes
class transaction_frame(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.parent = master
        self.parent.title("Transaction Data")
        self.parent.configure(background="#2d3339")
        self.centerWindow()
        self.add_item = Button(master, text='Add New Item', font=('Lato', 15), borderwidth=0, command=self.additem, background='#c92d22', fg='#fff', height=1, width=10)
        self.add_item.place(x= 600, y = 50)

        self.trans_label=Label(master, text='Add Transaction Record', font=('Lato',20), fg='#fff', background='#2d3339')
        self.trans_label.place(x=50,y=50)
        self.done_item = Button(master, text='Done', font=('Lato', 15), borderwidth=0, command=self.done, background='#c92d22', fg='#fff', height=1, width=10)
        self.done_item.place(x= 400, y = 50)

        self.type_label=Label(master, text="Sales/Purchase: ",  font=("Lato", 15), fg='#fff', background='#2d3339', width=15)
        self.type_label.place(x=50,y=100)

        self.entry_type = Entry(master, width = 25, borderwidth=0, font=("Calibri Light", 15),background='#16776A',fg='#fff')
        self.entry_type.place(x=300, y=100)

        self.count=0
    def done(self):
        os.system("say Done")

    def additem(self):
        master=self.parent
        self.itemid_label=Label(master, text="Item ID: ",  font=("Lato", 15), fg='#fff', background='#1EBBA6', width=10)
        self.itemid_label.place(x=50,y=200+125*self.count)

        self.itemname_label=Label(master, text="Item Name: ",  font=("Lato", 15), fg='#fff', background='#16776A', width=10)
        self.itemname_label.place(x=50,y=225+125*self.count)

        self.entry_id = Entry(master, width = 25, borderwidth=0, font=("Calibri Light", 15),background='#16776A',fg='#fff')
        self.entry_id.place(x=150, y=200+125*self.count)

        self.entry_name = Entry(master,width = 25, borderwidth=0, font=("Calibri Light", 15),background='#1EBBA6',fg='#fff')
        self.entry_name.place(x=150, y=225+125*self.count)

        self.quan_label=Label(master, text="Quantity: ",  font=("Lato", 15), fg='#fff', background='#1EBBA6', width=10)
        self.quan_label.place(x=50,y=250+125*self.count)

        self.price_label=Label(master, text="Price: ",  font=("Lato", 15), fg='#fff', background='#16776A', width=10)
        self.price_label.place(x=50,y=275+125*self.count)

        self.entry_quan = Entry(master, width = 25, borderwidth=0, font=("Calibri Light", 15),background='#16776A',fg='#fff')
        self.entry_quan.place(x=150, y=250+125*self.count)

        self.entry_price = Entry(master, width = 25, borderwidth=0, font=("Calibri Light", 15),background='#1EBBA6',fg='#fff')
        self.entry_price.place(x=150, y=275+125*self.count)


        self.count+=1
    def centerWindow(self):
        w = self.parent.winfo_screenwidth()
        h = self.parent.winfo_screenheight()
        x = w/2 - 225
        y = h/2 - 225

        self.parent.geometry("%dx%d+%d+%d" %(800,600,x,y))
        self.parent.resizable(1,1)

class Master(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        '''self.att1 = att1
        self.att2 = att2
        self.att3 = att3
        self.att4 = att4'''
        self.parent = master
        self.parent.title("Master")
        self.parent.configure(background="#2d3339")
        #self.pack()
        self.centerWindow()

        self.login_label=Label(master, text='MASTER SCREEN', font=('Lato',20), fg='#fff', background='#2d3339')
        self.login_label.place(x=170,y=50)


        self.umanage = Button(master, text='User Management', font=('Lato', 18), borderwidth=0,command=self.user_manage,background='#c92d22', fg='#fff', height=1, width=20)
        self.umanage.place(x= 170, y = 100)

        self.breports = Button(master, text='Business Reports', font=('Lato', 18), command=self.b_reports,borderwidth=0,background='#c92d22', fg='#fff', height=1, width=20)
        self.breports.place(x= 170, y = 150)
        self.spredict = Button(master, text='Stock Prediction', font=('Lato', 18), borderwidth=0,command=self.stock_pred, background='#c92d22', fg='#fff', height=1, width=20)
        self.spredict.place(x= 170, y = 200)

        self.btcal = Button(master, text='Bill/Tax Calculation', font=('Lato', 18),borderwidth=0,command=self.bill_calc,background='#c92d22', fg='#fff', height=1, width=20)
        self.btcal.place(x= 170, y = 250)

        self.ran = Button(master, text='Add a New Field', font=('Lato', 18), borderwidth=0,background='#c92d22', fg='#fff', height=1, width=20)
        self.ran.place(x= 170, y = 300)
        self.add_trans = Button(master, text='Add Transaction Data', font=('Lato', 18), borderwidth=0,command=self.addtrans, background='#c92d22', fg='#fff', height=1, width=20)
        self.add_trans.place(x= 170, y = 350)

        self.logout = Button(master, text='Logout', font=('Lato', 18), borderwidth=0, command=self.logout, background='#c92d22', fg='#fff', height=1, width=10)
        self.logout.place(x= 400, y = 450)

    def b_reports(self):
    	self.parent.destroy()
    	brframe=Tk()
        brf=business_reports(brframe)
        brframe.mainloop()
        brframe.destroy()

    def stock_pred(self):
    	self.parent.destroy()
   	spframe=Tk()
        spf=stocks_prediction(spframe)
        spframe.mainloop()
        spframe.destroy()

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
    def bill_calc(self):
        os.system("say Bill Calculation" )
        billframe=Tk()
        bf=bill_frame(billframe)
        billframe.mainloop()
        billframe.destroy()

    def addtrans(self):
        os.system("say Add Transaction Data" )
        transframe=Tk()
        tf=transaction_frame(transframe)
        transframe.mainloop()
        transframe.destroy()
    def user_manage(self):
        self.parent.destroy()
        um=Tk()
        umanage=UserManage(um)
        um.mainloop()
        um.destroy()
class UserManage(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.parent = master
        self.parent.title("Employee Management")
        self.parent.configure(background="#2d3339")
        self.centerWindow()

        self.title_label=Label(master, text='Users', font=('Lato',20), fg='#fff', background='#2d3339')
        self.title_label.place(x=50,y=50)
        self.uid_label=Label(master, text='User ID', font=('Lato',15), fg='#fff', background='#2d3339')
        self.uid_label.place(x=50,y=100)
        self.uname_label=Label(master, text='Username', font=('Lato',15), fg='#fff', background='#2d3339')
        self.uname_label.place(x=150,y=100)
        self.email_label=Label(master, text='Email', font=('Lato',15), fg='#fff', background='#2d3339')
        self.email_label.place(x=250,y=100)


        self.umanage = Button(master, text='User Management', font=('Lato', 18), borderwidth=0,commmand=self.user_manage,background='#c92d22', fg='#fff', height=1, width=20)
        self.umanage.place(x= 170, y = 180)
    def centerWindow(self):
        w = self.parent.winfo_screenwidth()
        h = self.parent.winfo_screenheight()
        x = w/2 - 225
        y = h/2 - 225

        self.parent.geometry("%dx%d+%d+%d" %(600,500,x,y))
        self.parent.resizable(0,0)

class business_reports(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.parent = master
        self.parent.title("Business Reports")
        self.parent.configure(background="#2d3339")
        self.centerWindow()


        self.title_label=Label(master, text='Business Reports', font=('Lato',20), fg='#fff', background='#2d3339')
        self.title_label.place(x=50,y=50)
        self.done_item = Button(master, text='Done', font=('Lato', 15), borderwidth=0, command=self.done, background='#c92d22', fg='#fff', height=1, width=10)
        self.done_item.place(x= 400, y = 50)
        #self.tid_label=Label(master, text="Add Transaction ID: ",  font=("Lato", 15), fg='#fff', background='#2d3339', width=15)
        #self.tid_label.place(x=50,y=100)
    def centerWindow(self):
        w = self.parent.winfo_screenwidth()
        h = self.parent.winfo_screenheight()
        x = w/2 - 225
        y = h/2 - 225
        self.parent.geometry("%dx%d+%d+%d" %(600,500,x,y))
        self.parent.resizable(0,0)
    def done(self):
        self.parent.destroy()
        master=Tk()
        mas=Master(master)
        master.mainloop()
        master.destroy()


class stocks_prediction(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.parent = master
        self.parent.title("Stock Prediction")
        self.parent.configure(background="#2d3339")
        self.centerWindow()


        self.title_label=Label(master, text='Predictions', font=('Lato',20), fg='#fff', background='#2d3339')
        self.title_label.place(x=50,y=50)
        self.done_item = Button(master, text='Done', font=('Lato', 15), borderwidth=0, command=self.done, background='#c92d22', fg='#fff', height=1, width=10)
        self.done_item.place(x= 400, y = 50)
        #self.tid_label=Label(master, text="Add Transaction ID: ",  font=("Lato", 15), fg='#fff', background='#2d3339', width=15)
        #self.tid_label.place(x=50,y=100)
    def centerWindow(self):
        w = self.parent.winfo_screenwidth()
        h = self.parent.winfo_screenheight()
        x = w/2 - 225
        y = h/2 - 225
        self.parent.geometry("%dx%d+%d+%d" %(600,500,x,y))
        self.parent.resizable(0,0)
    def done(self):
        self.parent.destroy()
        master=Tk()
        mas=Master(master)
        master.mainloop()
        master.destroy()

#----DRIVER SECTION OF APP----#
root = Tk()
#root.iconbitmap(r"Users/ayush/Desktop/virtualenvs/sw-lab/git/SW-Lab/Images/image.png")
#img = PhotoImage(file='/home/gian/Documents/SW-Lab-master/device-computer-icon.png')
#root.tk.call('wm', 'iconphoto', root._w, img)
app = InitialPage(master=root)
app.database()
app.mainloop()
root.destroy()
#----DRIVER SECTION OF APP----#
