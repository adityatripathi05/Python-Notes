'''
- A GUI (graphical user interface) is a system of interactive
components such as icons and other graphical objects that
help a user interact with computer software and other
applications.
'''
# Tkinter:
'''
import tkinter as tk
windows = tk.Tk()
windows.mainloop()
'''
'''
mainloop() is an infinite loop used to run the application,
wait for an event to occur and process the event till the
window is not closed.
'''
######################################################
# Defining properties of Interface:
'''
import tkinter as tk
windows = tk.Tk()
windows.geometry("500x500")
#windows.resizable(width=False, height=False)
windows.minsize(300,300)
windows.maxsize(700,700)
windows.title("My GUI")
windows.mainloop()
'''
#########################################################
# Switching between Interfaces:
'''
import tkinter as tk
from tkinter import ttk
class Interface1:
    def __init__(self):
        windows = tk.Tk()
        windows.geometry("500x500")
        windows.resizable(width=False, height=False)
        windows.title("Sign-up")
        label0 = tk.Label(windows, text="Welcome to XXX Bank",
                          font=('Times',12,'bold'),
                          fg='red',bg='Blue')
        label0.grid(row=0, columnspan=3)
        def btn1_act():
            windows.destroy()
            Interface2()
        button1 = tk.Button(windows,text='Submit',
                            command=btn1_act)
        button1.grid(row=8, column=0)
        windows.mainloop()
        
class Interface2:
    def __init__(self):
        windows = tk.Tk()
        windows.geometry("500x500")
        windows.resizable(width=False, height=False)
        windows.title("Login")
        windows.mainloop()

Interface1()
'''
##############################################################################
# Add widgets:
'''
import tkinter as tk
from tkinter import ttk
class Interface1:
    def __init__(self):
        windows = tk.Tk()
        windows.geometry("500x500")
        windows.resizable(width=False, height=False)
        windows.title("Sign-up")
        label0 = tk.Label(windows, text="Welcome to XXX Bank",
                          font=('Times',12,'bold'),
                          fg='red',bg='Blue')
        label0.grid(row=0, columnspan=3)
        label1 = tk.Label(windows, text="Create Username",
                          font=('Times',12,'bold'),
                          fg='red')
        label1.grid(row=1, column=0, sticky=tk.W)
        text1 = tk.StringVar()
        entry1 = tk.Entry(windows,width=15,textvariable=text1)
        entry1.grid(row=1, column=1)
        entry1.focus()
        text2 = tk.StringVar()
        label2 = tk.Label(windows, text="Select Gender",
                          font=('Times',12,'bold'),
                          fg='red')
        label2.grid(row=2, column=0, sticky=tk.W)
        radio1 = ttk.Radiobutton(windows,text='Male',
                                value='Male',variable=text2)
        radio1.grid(row=2, column=1)
        radio2 = ttk.Radiobutton(windows,text='Female',
                                value='Female',variable=text2)
        radio2.grid(row=2, column=2)
        label3 = tk.Label(windows, text="Select State",
                          font=('Times',12,'bold'),
                          fg='red')
        label3.grid(row=3, column=0, sticky=tk.W)
        text3 = tk.StringVar()
        combo1 = ttk.Combobox(windows, width=15,
                              state='readonly',
                              textvariable=text3)
        combo1['value']=('---SELECT---','UP','Delhi','Haryana')
        combo1.current(0)
        combo1.grid(row=3, column=1)
        text4 = tk.IntVar()
        check1 = ttk.Checkbutton(windows,variable=text4,
                                 text='Agree with all terms*')
        check1.grid(row=4, column=0)
        def btn1_act():
            uname= text1.get()
            ugender = text2.get()
            ulocation = text3.get()
            ucheck = text4.get()
            print(f'{uname}:{ugender}:{ulocation}:{ucheck}')
            windows.destroy()
            Interface2()
        button1 = tk.Button(windows,text='Submit',
                            command=btn1_act)
        button1.grid(row=8, column=0)
        windows.mainloop()
        
class Interface2:
    def __init__(self):
        windows = tk.Tk()
        windows.geometry("500x500")
        windows.resizable(width=False, height=False)
        windows.title("Login")
        windows.mainloop()

Interface1()
'''
################################################################################
# Even-Odd on Interface:
'''
import tkinter as tk
class Interface1:
    def __init__(self):
        windows = tk.Tk()
        windows.geometry("500x500")
        windows.resizable(width=False, height=False)
        windows.title("Check Even-Odd")
        label1 = tk.Label(windows, text="Enter No.",
                          font=('Times',12,'bold'),
                          fg='red')
        label1.grid(row=1, column=0, sticky=tk.W)
        var1 = tk.IntVar()
        entry1 = tk.Entry(windows,width=15,textvariable=var1)
        entry1.grid(row=1, column=1)
        entry1.focus()
        
        def even_odd(n):
            if n%2==0:
                return 'Even'
            else:
                return 'Odd'
            
        def btn1_act():
            no = var1.get()
            result = even_odd(no)
            label2 = tk.Label(windows, text=f"No. is {result}",
                          font=('Times',12,'bold'),
                          fg='red')
            label2.grid(row=1, column=3)
            
        button1 = tk.Button(windows,text='Submit',
                            command=btn1_act)
        button1.grid(row=3, column=0)
        windows.mainloop()
Interface1()
'''
##########################################################
# Message Box:
'''
import tkinter as tk
from tkinter import messagebox
class Interface1:
    def __init__(self):
        windows = tk.Tk()
        windows.geometry("500x500")
        windows.resizable(width=False, height=False)
        windows.title("Check Even-Odd")
        label1 = tk.Label(windows, text="Enter No.",
                          font=('Times',12,'bold'),
                          fg='red')
        label1.grid(row=1, column=0, sticky=tk.W)
        var1 = tk.IntVar()
        entry1 = tk.Entry(windows,width=15,textvariable=var1)
        entry1.grid(row=1, column=1)
        entry1.focus()
        
        def even_odd(n):
            if n%2==0:
                return 'Even'
            else:
                return 'Odd'
            
        def btn1_act():
            no = var1.get()
            result = even_odd(no)
            messagebox.showinfo("Result",f"No. is {result}")
            
        button1 = tk.Button(windows,text='Submit',
                            command=btn1_act)
        button1.grid(row=3, column=0)
        windows.mainloop()
Interface1()
'''
############################################################
# With database:
'''
import tkinter as tk
import sqlite3
from tkinter import messagebox
class Interface1:
    def __init__(self):
        windows = tk.Tk()
        windows.geometry("500x500")
        windows.resizable(width=False, height=False)
        windows.title("Check Even-Odd")
        label1 = tk.Label(windows, text="Enter No.",
                          font=('Times',12,'bold'),
                          fg='red')
        label1.grid(row=1, column=0, sticky=tk.W)
        var1 = tk.IntVar()
        entry1 = tk.Entry(windows,width=15,textvariable=var1)
        entry1.grid(row=1, column=1)
        entry1.focus()
        
        def even_odd(n):
            if n%2==0:
                return 'Even'
            else:
                return 'Odd'
        def insert_db(n,re):
            tup = (n,re)
            conn = sqlite3.connect("EvenOdd.db")
            cur = conn.cursor()
            try:
                cur.execute('CREATE TABLE Even\
                            (Number INTEGER NOT NULL,\
                            Result CHAR(50) NOT NULL)')
            except:
                pass
            cur.execute('INSERT INTO Even(Number,Result)\
                        VALUES(?,?)',tup)
            conn.commit()
            conn.close()
        def btn1_act():
            no = var1.get()
            result = even_odd(no)
            insert_db(no,result)
            label2 = tk.Label(windows, text="Record Inserted",
                          font=('Times',12,'bold'),
                          fg='red')
            label2.grid(row=1, column=3)
        button1 = tk.Button(windows,text='Submit',
                            command=btn1_act)
        button1.grid(row=3, column=0)
        windows.mainloop()
Interface1()
'''
