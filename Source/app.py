#Incase performance issues use tkraise
import tkMessageBox as box
import os
import pickle
import time
import Tix
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

    def opensignup(self):
        self.parent.destroy()
        signup = Tk()
        framesignup = frame_signup(signup)
        signup.mainloop()

    def centerWindow(self):
        w = self.parent.winfo_screenwidth()
        h = self.parent.winfo_screenheight()
        x = w/2 - 225
        y = h/2 - 225

        self.parent.geometry("%dx%d+%d+%d" %(600,500,x,y))
        self.parent.resizable(0,0)
    def quit(self):
        self.parent.destroy()

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

        self.entry_pass = Entry(master, width = 25, borderwidth=0, font=("Calibri Light", 35),background='#1EBBA6',fg='#fff')
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
    def centerWindow(self):
        w = self.parent.winfo_screenwidth()
        h = self.parent.winfo_screenheight()
        x = w/2 - 225
        y = h/2 - 225

        self.parent.geometry("%dx%d+%d+%d" %(600,500,x,y))
        self.parent.resizable(0,0)

    def login(self):
        global a
        self.username=self.entry_user.get().lower()
        a=self.username
        self.password=self.entry_pass.get()
        self.f=open('user.dat','rb')
        try:
            while True:
                self.a=pickle.load(self.f)
                self.usernames=self.a.keys()
                if len(self.usernames)==1:
                    self.entry_pass.delete(0,'end')
        except EOFError:
            pass
        if self.password=='':
            box.showerror('ERROR','Please enter a password before trying to login')
        else:
            if self.username.strip() not in self.usernames:
                box.showerror('ERROR',"That username wasn't found in our directory.\nPlease sign up first")
            if self.username.strip() in self.usernames:
                if self.password==self.a[self.username.strip()]:
                    self.parent.destroy()
                    self.file=open(a+'.txt','a').close()
                    self.mainscreen()
                    main_page = Tk()
                    mainframe = main_frame(main_page)
                    main_page.mainloop()
                else:
                    box.showerror('ERROR','Incorrect username/password entered.\nPlease enter valid credentials')
                    self.entry_pass.delete(0,'end')

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

        self.entry_pass = Entry(master, width = 25, borderwidth=0, font=("Calibri Light", 35),background='#1EBBA6',fg='#fff')
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
        global a
        self.username=self.entry_user.get().lower()
        a=self.username
        self.password=self.entry_pass.get()
        self.email=self.entry_email.get()
        self.classtype=self.entry_class.get().lower()
        self.f=open('user.dat','rb')
        try:
            while True:
                self.collection=pickle.load(self.f)
                self.usernames=self.collection.keys()
        except EOFError:
            pass
        self.f.close()
        if len(self.password.strip())==0:
                box.showerror('ERROR','Please enter a password')
        else:
            if self.username.strip() in self.usernames:
                box.showerror('ERROR','The entered username has already been taken.\nPlease enter another one')
                self.entry_pass.delete(0,'end')
                self.entry_user.delete(0,'end')
                self.entry_email.delete(0,'end')
                self.entry_class.delete(0,'end')
            else:
                self.collection[self.username.strip()]=self.password
                self.f=open('user.dat','wb')
                pickle.dump(self.collection,self.f)
                self.f.close()
                box.showinfo('Success','Your credentials have been saved.\nEnjoy using our app')
                self.userdata='Username: '+self.username.strip()+'\nPassword: '+self.password
                box.showinfo('Your credentials',self.userdata)
                self.parent.destroy()
                self.file=open(a+'.txt','a').close()
                self.mainscreen()




class Application(Frame):

    def __init__(self, master=None):
        #def __init__(self,parent):
        #fra.__init__(self,parent)
 	Frame.__init__(self,master)
        self.parent = master
        self.parent.title("Login")
        self.parent.configure(background="#2d3339")
        #self.pack()
        self.centerWindow()

        self.login_label=Label(master, text='LOGIN SCREEN', font=('Lato',20), fg='#fff', background='#2d3339')
        self.login_label.place(x=180,y=120)

        self.user_label=Label(master, text="Enter/Choose your\nusername: ",  font=("Lato", 18), fg='#fff', background='#1EBBA6', width=20)
        self.user_label.place(x=0,y=190)

        self.pass_label=Label(master, text="Enter/Choose your\npassword: ",  font=("Lato", 18), fg='#fff', background='#16776A', width=20)
        self.pass_label.place(x=0,y=250)

        self.entry_user = Entry(master, width = 25, borderwidth=0, font=("Calibri Light", 35),background='#16776A',fg='#fff')
        self.entry_user.place(x=286, y=190)

        self.entry_pass = Entry(master, width = 25, borderwidth=0, font=("Calibri Light", 35),background='#1EBBA6',fg='#fff')
        self.entry_pass.place(x=286, y=250)

        self.login = Button(master, text="Log In", font=("Lato", 18), borderwidth=0, command=self.login, background='#c92d22', fg='#fff', height=1, width=10)
        self.login.place(x= 140, y = 339)

        self.signup = Button(master, text="Sign Up", font=("Lato", 18), borderwidth=0, command=self.signup, background='#c92d22', fg='#fff', height=1, width=10)
        self.signup.place(x= 300, y =340)

        self.quit = Button(master, text="Quit", font=("Lato", 18), command=self.quit, borderwidth=0, background='#c92d22', fg='#fff', height=1, width=5)
        self.quit.place(x= 480, y = 425)

    def centerWindow(self):
        w = self.parent.winfo_screenwidth()
        h = self.parent.winfo_screenheight()
        x = w/2 - 225
        y = h/2 - 225

        self.parent.geometry("%dx%d+%d+%d" %(600,500,x,y))
        self.parent.resizable(0,0)

    def login(self):
        global a
        self.username=self.entry_user.get().lower()
        a=self.username
        self.password=self.entry_pass.get()
        self.f=open('user.dat','rb')
        try:
            while True:
                self.a=pickle.load(self.f)
                self.usernames=self.a.keys()
                if len(self.usernames)==1:
                    self.entry_pass.delete(0,'end')
        except EOFError:
            pass
        if self.password=='':
            box.showerror('ERROR','Please enter a password before trying to login')
        else:
            if self.username.strip() not in self.usernames:
                box.showerror('ERROR',"That username wasn't found in our directory.\nPlease sign up first")
        if self.username.strip() in self.usernames:
            if self.password==self.a[self.username.strip()]:
                self.parent.destroy()
                self.file=open(a+'.txt','a').close()
                self.mainframe()
                main_screen = Tk()
                mainframe = main_frame(main_screen)
                main_screen.mainloop()
            else:
                box.showerror('ERROR','Incorrect username/password entered.\nPlease enter valid credentials')
                self.entry_pass.delete(0,'end')

    def signup(self):
        global a
        self.username=self.entry_user.get().lower()
        a=self.username
        self.password=self.entry_pass.get()
        self.f=open('user.dat','rb')
        try:
            while True:
                self.collection=pickle.load(self.f)
                self.usernames=self.collection.keys()
        except EOFError:
            pass
        self.f.close()
        if len(self.password.strip())==0:
                box.showerror('ERROR','Please enter a password')
        else:
            if self.username.strip() in self.usernames:
                box.showerror('ERROR','The entered username has already been taken.\nPlease enter another one')
                self.entry_pass.delete(0,'end')
                self.entry_user.delete(0,'end')
            else:
                self.collection[self.username.strip()]=self.password
                self.f=open('user.dat','wb')
                pickle.dump(self.collection,self.f)
                self.f.close()
                box.showinfo('Success','Your credentials have been saved.\nEnjoy using our app')
                self.userdata='Username: '+self.username.strip()+'\nPassword: '+self.password
                box.showinfo('Your credentials',self.userdata)
                self.parent.destroy()
                self.file=open(a+'.txt','a').close()
                self.mainscreen()

    def mainscreen(self):
        main_screen = Tk()
        mainframe = main_frame(main_screen)
        main_screen.mainloop()

    def quit(self):
        self.parent.destroy()
    #self.createWidgets()
    #self.createLabels()

#----MAKING THE USERNAME/PASSWORD FILE-----#
f=open('user.dat','ab').close()
f=open('user.dat','rb')
a=dict()
try:
    while True:
        a=pickle.load(f)
except EOFError:
    pass
if type(a)==dict:
    pass
else:
    a=dict()
try:
    if len(a)!=0 and a['###']=='###':
        pass
    else:
        x={'###':'###'}
        a.update(x)
except TypeError:
    f.close()
    os.remove('user.dat')
    pass
f.close()
f=open('user.dat','wb')
pickle.dump(a,f)
f.close()
#----MAKING THE USERNAME/PASSWORD FILE-----#

#----MAIN WINDOW OF APP----#
class main_frame(Frame):

    def __init__(self,parent):
        #frame_title.__init__(self,parent)
        Frame.__init__(self,parent)
        self.parent=parent
        self.parent.title("Multi-Functional Accounting Software")
        self.parent.configure(bg="#2d3339")
        self.centerWindow()

        self.welcometext=Label(parent, text='Welcome '+a,font=("Lato", 20), fg='#fff', background='#2d3339')
        self.welcometext.place(x=10,y=80)

        self.label1=Label(parent, text='What would you like to do today?', font=('Lato', 20), fg='#fff', background='#2d3339')
        self.label1.place(x=75, y=155)

        self.encryption = Button(parent, text="Encryption", font=("Lato", 18), command=self.encry, borderwidth=0, background='#1EBBA6', fg='#fff', height=2, width=20)
        self.encryption.place(x= 140, y = 230)

        self.decryption = Button(parent, text="Decryption", font=("Lato", 18), command=self.decry, borderwidth=0, background='#16776A', fg='#fff', height=2, width=20)
        self.decryption.place(x= 140, y = 330)

        self.quit = Button(parent, text="Quit", font=("Lato", 18), command=self.quit, borderwidth=0, background='#c92d22', fg='#fff', height=1, width=5)
        self.quit.place(x= 460, y = 485)

        self.logout = Button(parent, text="Log Out", font=("Lato", 18), command=self.logout, borderwidth=0, background='#c92d22', fg='#fff', height=1, width=7)
        self.logout.place(x= 330, y = 485)

        self.history = Button(parent, text="View History", font=("Lato", 18), command=self.history, borderwidth=0, background='#c92d22', fg='#fff', height=1, width=10)
        self.history.place(x= 10, y = 485)

    def centerWindow(self):
        w = self.parent.winfo_screenwidth()
        h = self.parent.winfo_screenheight()
        x = w/2 - 275
        y = h/2 - 275
        self.parent.geometry("%dx%d+%d+%d" % (550,550,x,y))
        self.parent.resizable(0,0)

    def encry(self):  #Encryption Frame
        self.parent.destroy()
        encrypt = Tk()
        frameencrypt = frame_encrypt(encrypt)
        encrypt.mainloop()

    def decry(self): #Decryption Frame
        self.parent.destroy()
        decrypt = Tk()
        framedecrypt = frame_decrypt(decrypt)
        decrypt.mainloop()

    def history(self): #History Frame
        self.parent.destroy()
        viewhistory=Tk()
        historyframe=frame_history(viewhistory)
        viewhistory.mainloop()

    def quit(self):
        self.parent.destroy()

    def logout(self):
        self.parent.destroy()
        logout = Tk()
        loginframe = login_frame(logout)
        logout.mainloop()
#----MAIN WINDOW OF APP----#

#----DRIVER SECTION OF APP----#
root = Tk()
app = InitialPage(master=root)
app.mainloop()
root.destroy()
#----DRIVER SECTION OF APP----#
