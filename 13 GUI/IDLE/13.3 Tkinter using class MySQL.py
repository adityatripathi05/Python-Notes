import tkinter as tk
from tkinter import ttk
from pymysql import *

class Windows0:
    def __init__(self):
        try:
            con = connect(host='localhost', user='root', password='mysql', port=3306)
            cursor=con.cursor()
            cursor.execute("create database aditya")
            con.commit()
            con.close()
        except:
            pass
        try:
            con = connect(host='localhost', user='root', password='mysql', database= 'aditya', port=3306)
            cursor=con.cursor()
            cursor.execute("create table Account(Name varchar(10), Email varchar(10) primary key, Password varchar(10),\
                           Gender varchar(10), City varchar(10))")
            con.commit()
            con.close()
        except:
            pass
        
        self.window = tk.Tk()
        self.window.geometry("500x500")
        self.window.resizable(width=False, height=False)
        self.window.title('Welcome Window')
        
        self.label0 = ttk.Label(self.window, text = 'Welcome to the Institution', background= 'Red', font=('Times',12,'bold'))
        self.label0.grid(row=0, columnspan=3)
        
        def btn1_act():
            self.window.destroy()
            Windows3()
        self.button1 = ttk.Button(self.window, text='Login', command= btn1_act)
        self.button1.grid(row=1, column=0, sticky= tk.W)
        
        def btn2_act():
            self.window.destroy()
            Windows1()
        self.button2 = ttk.Button(self.window, text='Signup', command= btn2_act)
        self.button2.grid(row=1, column=2)
        
        def btn3_act():
            self.window.destroy()
        self.button3 = ttk.Button(self.window, text='Exit', command= btn3_act)
        self.button3.grid(row=1, column=4)
        
        self.window.mainloop()
        
class Windows1:
    def __init__(self):

        self.window = tk.Tk()
        self.window.geometry("500x500")
        self.window.resizable(width=False, height=False)
        self.window.title('Create Account Window')
        
        self.label0 = ttk.Label(self.window, text = 'ENTER DETAILS TO CREATE ACCOUNT', background= 'Red', font=('Times',12,'bold'))
        self.label0.grid(row=0, columnspan=3)
        
        self.text1 = tk.StringVar()
        self.entry1 = ttk.Entry(self.window, width= 15, textvariable= self.text1)
        self.entry1.grid(row=1, column=1, padx=2, pady=2)
        self.entry1.focus()
        
        self.label1 = ttk.Label(self.window, text = 'Enter Username', foreground='Blue', font=('ariel',10,'bold'))  
        self.label1.grid(row=1, column=0, sticky= tk.W, padx=2, pady=2)
        
        self.label2 = ttk.Label(self.window, text = 'Create Email-Id', foreground='Blue', font=('ariel',10,'bold'))
        self.label2.grid(row=2, column=0, sticky= tk.W, padx=2, pady=2)
        
        self.text2 = tk.StringVar()
        self.entry2 = ttk.Entry(self.window, width= 15, textvariable= self.text2)
        self.entry2.grid(row=2, column=1, padx=2, pady=2)
        
        self.label3 = ttk.Label(self.window, text = 'Create Password', foreground='Blue', font=('ariel',10,'bold'))
        self.label3.grid(row=3, column=0, sticky= tk.W)
        
        self.text3 = tk.StringVar()
        self.entry3 = ttk.Entry(self.window, width= 15, textvariable= self.text3)
        self.entry3.grid(row=3, column=1, padx=2, pady=2)
        
        self.label4 = ttk.Label(self.window, text = 'Enter Gender', foreground='Blue', font=('ariel',10,'bold'))
        self.label4.grid(row=4, column=0, sticky= tk.W, padx=2, pady=2)
        
        self.text4 = tk.StringVar()
        self.radio1 = ttk.Radiobutton(self.window, text='Male', value='Male', variable=self.text4)
        self.radio1.grid(row=4, column=1)
        self.radio2 = ttk.Radiobutton(self.window, text='Female', value='Female', variable=self.text4)
        self.radio2.grid(row=4, column=2)
        self.radio3 = ttk.Radiobutton(self.window, text='Other', value='Other', variable=self.text4)
        self.radio3.grid(row=4, column=3)
        
        self.label5 = ttk.Label(self.window, text = 'Enter State', foreground='Blue', font=('ariel',10,'bold'))
        self.label5.grid(row=5, column=0, sticky= tk.W, padx=2, pady=2)
        
        self.text5 = tk.StringVar()
        self.combo1 = ttk.Combobox(self.window, width= 13, state='readonly', textvariable= self.text5)
        self.combo1['value']= ('----SELECT----','UP','DELHI',"HARYANA",'PUNJAB','M.P','MUMBAI')
        self.combo1.current(0)
        self.combo1.grid(row=5, column=1)
        
        self.text6 = tk.IntVar()
        self.check1 = ttk.Checkbutton(self.window, text='Please check, if you agree to terms and conditions*',variable= self.text6)
        self.check1.grid(row=6, columnspan=3)
            
        def btn1_act():
            if (self.text6.get() == 1):
                uname = self.text1.get()
                email = self.text2.get()
                pwd = self.text3.get()
                gender = self.text4.get()
                state = self.text5.get()

                con = connect(host='localhost', user='root', password='mysql', database= 'aditya', port=3306)
                cursor=con.cursor()
                cursor.execute(f"insert into Account values('{uname}','{email}','{pwd}','{gender}','{state}')")
                con.commit()
                con.close()
                self.window.destroy()
                Windows2(uname)
            else:
                label6 = ttk.Label(self.window, text = 'Tick check button', foreground='Blue', font=('ariel',10,'bold'))
                label6.grid(row=7, column=0, sticky= tk.W, padx=2, pady=2)
            
        self.button1 = ttk.Button(self.window, text='Submit', command= btn1_act)
        self.button1.grid(row=8, column=0)

        def btn2_act():
            # set the value
            uname = self.text1.set("")
            email = self.text2.set("")
            pwd = self.text3.set("")
            gender = self.text4.set("")
            state = self.text5.set("")
            check = self.text6.set("")

        self.button2 = ttk.Button(self.window, text='Reset', command=btn2_act)
        self.button2.grid(row=8, column=2)
        
        def btn3_act():
            self.window.destroy()
            Windows0()
        self.button3 = ttk.Button(self.window, text='Back', command= btn3_act)
        self.button3.grid(row=0, column= 15, sticky= tk.E)
        
        def btn4_act():
            self.window.destroy()
        self.button4 = ttk.Button(self.window, text='Exit', command= btn4_act)
        self.button4.grid(row=8, column=4)
        
        self.window.mainloop()
        
class Windows2:
    def __init__(self,u):
        self.window=tk.Tk()
        self.window.geometry('500x500')
        self.window.resizable(width=False, height=False)
        self.window.title('Successful')
        
        self.label1= ttk.Label(self.window, text=f'Hello {u}, your account created successfully')
        self.label1.grid(row=0, columnspan=4)
        
        def btn1_act():
            self.window.destroy()
            Windows3()  
        self.button1= ttk.Button(self.window,text='Login', command= btn1_act)
        self.button1.grid(row=1, column=0)
        
        def btn2_act():
            self.window.destroy()
            Windows1()
        self.button2= ttk.Button(self.window,text='Back', command= btn2_act)
        self.button2.grid(row=1, column=3)
        
        def btn3_act():
            self.window.destroy()
        self.button3 = ttk.Button(self.window, text='Exit', command= btn3_act)
        self.button3.grid(row=1, column=5)
        
        self.window.mainloop()
        
class Windows3:
    def __init__(self):
        self.window=tk.Tk()
        self.window.geometry('500x500')
        self.window.resizable(width=False, height=False)
        self.window.title('Login Window')
        
        self.label0 = ttk.Label(self.window, text = 'ENTER DETAILS TO LOGIN', background= 'Red', font=('Times',12,'bold'))
        self.label0.grid(row=0, columnspan=4)
        
        self.label1 = ttk.Label(self.window, text = 'Enter Email-Id', foreground='Blue', font=('ariel',10,'bold'))
        self.label1.grid(row=1, column=0, sticky= tk.W, padx=2, pady=2)
        
        self.text1 = tk.StringVar()
        self.entry1 = ttk.Entry(self.window, width= 15, textvariable= self.text1)
        self.entry1.grid(row=1, column=1, padx=2, pady=2)
        
        self.label2 = ttk.Label(self.window, text = 'Enter Password', foreground='Blue', font=('ariel',10,'bold'))
        self.label2.grid(row=2, column=0, sticky= tk.W)
        
        self.text2 = tk.StringVar()
        self.entry2 = ttk.Entry(self.window, width= 15, textvariable= self.text2)
        self.entry2.grid(row=2, column=1, padx=2, pady=2)
        
        def btn1_act():
            email = self.text1.get()
            pwd = self.text2.get()
            con = connect(host='localhost', user='root', password='mysql', database= 'aditya', port=3306)
            cursor=con.cursor()
            if (cursor.execute(f"select * from Account where Email='{email}'")):
                if (cursor.execute(f"select * from Account where Password='{pwd}'")):
                    self.window.destroy()
                    Windows4(email)
                else:
                    label4 = ttk.Label(self.window, text = 'Wrong Password', foreground='Blue', font=('ariel',10,'bold'))
                    label4.grid(row=3, column=0, sticky= tk.W)
                
            else:
                label3 = ttk.Label(self.window, text = 'Unknown user', foreground='Blue', font=('ariel',10,'bold'))
                label3.grid(row=3, column=0, sticky= tk.W)
                
        self.button1= ttk.Button(self.window,text='Login', command= btn1_act)
        self.button1.grid(row=4, column=0)
        
        def btn2_act():
            self.window.destroy()
            Windows5()
            
        self.button2= ttk.Button(self.window,text='Forget Password', command= btn2_act)
        self.button2.grid(row=4, column=1)
        
        def btn3_act():
            self.window.destroy()
            Windows0()
        self.button3 = ttk.Button(self.window, text='Back', command= btn3_act)
        self.button3.grid(row=0, column= 15, sticky= tk.E)
        
        def btn4_act():
            self.window.destroy()
        self.button4 = ttk.Button(self.window, text='Exit', command= btn4_act)
        self.button4.grid(row=4, column=5)
        
        self.window.mainloop()

class Windows4:
    def __init__(self,email):
        self.window=tk.Tk()
        self.window.geometry('500x500')
        self.window.resizable(width=False, height=False)
        self.window.title('Detail Window')
        
        con = connect(host='localhost', user='root', password='mysql', database= 'aditya', port=3306)
        cursor=con.cursor()
        cursor.execute(f"select * from Account where Email='{email}'")
        detail = cursor.fetchone()
        
        self.label0 = ttk.Label(self.window, text = 'Your details are', foreground= 'Red', font=('Times',12,'bold'))
        self.label0.grid(row=0, columnspan=2, sticky= tk.W)
        
        self.label1 = ttk.Label(self.window, text = f'Name: {detail[0].lower().capitalize()}', foreground= 'Red', font=('Times',12,'bold'))
        self.label1.grid(row=1, column=0, sticky= tk.W)
        
        self.label2 = ttk.Label(self.window, text = f'Gender: {detail[3].lower().capitalize()}', foreground= 'Red', font=('Times',12,'bold'))
        self.label2.grid(row=2, column=0, sticky= tk.W)
        
        self.label3 = ttk.Label(self.window, text = f'City: {detail[4].lower().capitalize()}', foreground= 'Red', font=('Times',12,'bold'))
        self.label3.grid(row=3, column=0, sticky= tk.W)
        
        def btn4_act():
            self.window.destroy()
        self.button4 = ttk.Button(self.window, text='Exit', command= btn4_act)
        self.button4.grid(row=4, column=0)
        
        self.window.mainloop()
    
class Windows5:
    def __init__(self):
        self.window=tk.Tk()
        self.window.geometry('500x500')
        self.window.resizable(width=False, height=False)
        self.window.title('Password Window')
        
        self.label0 = ttk.Label(self.window, text = 'Enter Email-ID', foreground= 'Red', font=('Times',12,'bold'))
        self.label0.grid(row=1, column=0)
        self.text0 = tk.StringVar()
        self.entry0 = ttk.Entry(self.window, width= 15, textvariable= self.text0)
        self.entry0.grid(row=1, column=1, sticky= tk.W, padx=2, pady=2)
        self.entry0.focus()
        
        self.label1 = ttk.Label(self.window, text = 'Create New Password', foreground= 'Red', font=('Times',12,'bold'))
        self.label1.grid(row=2, column=0)
        self.text1 = tk.StringVar()
        self.entry1 = ttk.Entry(self.window, width= 15, textvariable= self.text1)
        self.entry1.grid(row=2, column=1, sticky= tk.W, padx=2, pady=2)
        self.entry1.focus()
        
        def btn1_act():
            email = self.text0.get()
            pwd = self.text1.get()
            con = connect(host='localhost', user='root', password='mysql', database= 'aditya', port=3306)
            cursor=con.cursor()
            if (cursor.execute(f"select * from Account where Email='{email}'")):
                cursor.execute(f"update Account set Password='{pwd}' where Email='{email}'")
                con.commit()
                con.close()
                self.window.destroy()
                Windows3()
                
            else:
                label3 = ttk.Label(self.window, text = 'Unknown user', foreground='Blue', font=('ariel',10,'bold'))
                label3.grid(row=3, column=0, sticky= tk.W)
                
        self.button1= ttk.Button(self.window,text='Submit', command= btn1_act)
        self.button1.grid(row=4, column=0)
        
        self.window.mainloop()
        
Windows0()
