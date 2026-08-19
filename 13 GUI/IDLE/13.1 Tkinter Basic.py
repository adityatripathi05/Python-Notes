############
# GUI: Graphical User Interface
'''
- A GUI is a system of interactive components such as
icons and other graphical objects that help a user
interact with computer software and other applications.
'''

############
# TCL(Tool Command Language) and Tk(Toolkit)
'''
- Tcl is a general purpose multi-paradigm system
programming language.
    - It is a scripting language that aims at providing
    the ability for applications to communicate with each other.
- Tk is a cross platform widget toolkit used for building
GUI in many languages.
'''

############
# GUI in Python:
'''
- In python, basic GUI application can be developed using
builtin module 'tkinter'.
- Other platform to develop GUI: PyQt, WxPython etc
'''

########
# Basic Interface Window:
'''
import tkinter as tk
win= tk.Tk()
'''

########
#Define Properties of Interface:
'''
import tkinter as tk
win= tk.Tk()
win.title('My GUI')
win.geometry('300x300')
win.configure(background='Red')
'''

#########
# Interface Size to Fullscreen:
'''
import tkinter as tk
win= tk.Tk()
win.title('My GUI')

width_screen=win.winfo_screenwidth()
print(width_screen)
height_screen=win.winfo_screenheight()
print(height_screen)
win.geometry(f'{width_screen}x{height_screen}')
'''

#########
# Define Interface Position w.r.t Screen
'''
import tkinter as tk
win= tk.Tk()
win.title('My GUI')
#win.geometry('300x300+0+0') # Topleft corner x=0,y=0
win.geometry('300x300+400+300')
'''

#########
# Restrict Resizing of Interface
'''
import tkinter as tk
win= tk.Tk()
win.title('My GUI')
win.geometry('300x300')
win.resizable(0,0) #win.resizable(height=False,width=False)
'''

##########
# Restrict maximum and minimum resizing of Interface
'''
import tkinter as tk
win= tk.Tk()
win.title('My GUI')
win.geometry('300x300')
win.minsize(100,100)
win.maxsize(500,500)
'''

################Add Widget to Interface##################

#########
# Add a Label Widget:
'''
import tkinter as tk
win= tk.Tk()
win.title('My GUI')
win.geometry('300x300')

label=tk.Label(win,text='Name')
label.grid(row=0, column=0) # grid() is layout manager
'''

# Customize Label:
'''
import tkinter as tk
win= tk.Tk()
win.title('My GUI')
win.geometry('300x300')

label=tk.Label(win,text='Name',bg='blue',fg='#33FFBE',
               font='Ariel 15 bold italic',
               bd=2,relief='solid',padx=10,pady=10)
label.grid(row=0, column=0)
'''

# Set Label text after declaration:
'''
import tkinter as tk
win = tk.Tk()  
win.title('My GUI') 
win.geometry("300x300")

# Using StringVar and textvariable inside Label
label1=tk.Label(win, bd=2,relief='solid')
label1.grid(row=0,column=0, pady=3)

var2=tk.StringVar()
label2=tk.Label(win, bd=2,relief='solid',
                textvariable=var2)
label2.grid(row=1,column=0, pady=3)

#Input text of Label later here 
label1['text']='Hi'
var2.set('Hi')
'''

# Add Multiple Label Widgets:
'''
import tkinter as tk
win= tk.Tk()
win.title('My GUI')
win.geometry('300x300')

labels=['Name','Age','Email','Gender','Country','Weight']
for i in range(len(labels)):
    label='label'+str(i)
    label=tk.Label(win,text=labels[i])
    label.grid(row=i, column=0)
'''

# Alignment of Widget in a column:
'''
import tkinter as tk
win= tk.Tk()
win.title('My GUI')
win.geometry('500x500')
win.configure(background='#33FFBE')

labels=['Name','Age','Email','Gender','Country','Weight']
for i in range(len(labels)):
    label='label'+str(i)
    label=tk.Label(win,text=labels[i])
    label.grid(row=i,column=0,sticky='E',pady=2) #'E'=tk.E
'''

###########
# Add a Entry Box:
'''
import tkinter as tk
import tkinter.ttk as ttk
win= tk.Tk()
win.title('My GUI')
win.geometry('300x300')

label=tk.Label(win,text='Name', font=('Ariel',10))
label.grid(row=0, column=0,padx=2)

var=tk.StringVar()
entry=tk.Entry(win,width=15,textvariable=var)
entry.grid(row=0,column=1,padx=2)
'''

# Add multiple Entry box:
'''
import tkinter as tk
win= tk.Tk()
win.title('My GUI')
win.geometry('300x300')

labels=['Name','Age','Email','Gender','Country','Weight']
for i in range(len(labels)):
    label='label'+str(i)
    label=ttk.Label(win,text=labels[i])
    label.grid(row=i, column=0,sticky='E',padx=2,pady=2)

var={'var0':tk.StringVar(),
     'var1':tk.StringVar(),
     'var2':tk.StringVar()}
entry=['entry0','entry1','entry2']
for i in range(len(var)):
    entry[i]=tk.Entry(win,width=15,
                       textvariable=var['var'+str(i)])
    entry[i].grid(row=i,column=1,padx=2,pady=2)
entry[0].focus() #place cursor
'''

###########
# Add Radiobutton Widget:
'''
import tkinter as tk
win= tk.Tk()
win.title('My GUI')
win.geometry('300x300')

labels=['Name','Age','Email','Gender','Country','Weight']
for i in range(len(labels)):
    label='label'+str(i)
    label=ttk.Label(win,text=labels[i])
    label.grid(row=i, column=0,sticky='E',padx=2,pady=2)

var={'var0':tk.StringVar(),
     'var1':tk.StringVar(),
     'var2':tk.StringVar()}
entry=['entry0','entry1','entry2']
for i in range(len(var)):
    entry[i]=ttk.Entry(win,width=15,
                       textvariable=var['var'+str(i)])
    entry[i].grid(row=i,column=1,padx=2,pady=2)
entry[0].focus()

var3=tk.StringVar()
txt=['Male','Female','Other']
for i in range(3):
    rdbtn=f'rdbtn{i}'
    rdbtn=tk.Radiobutton(win,text=txt[i],value=txt[i],
                          variable=var3)
    rdbtn.grid(row=3,column=1+i, sticky='E')
var3.set(0)  # Any arbitrary value to disselect
'''

###########
# Add Combobox Widget:
'''
import tkinter as tk
import tkinter.ttk as ttk
win= tk.Tk()
win.title('My GUI')
win.geometry('300x300')

labels=['Name','Age','Email','Gender','Country','Weight']
for i in range(len(labels)):
    label='label'+str(i)
    label=ttk.Label(win,text=labels[i])
    label.grid(row=i, column=0,sticky='E',padx=2,pady=2)

var={'var0':tk.StringVar(),
     'var1':tk.StringVar(),
     'var2':tk.StringVar()}
entry=['entry0','entry1','entry2']
for i in range(len(var)):
    entry[i]=ttk.Entry(win,width=15,
                       textvariable=var['var'+str(i)])
    entry[i].grid(row=i,column=1,padx=2,pady=2)
entry[0].focus()

var3=tk.StringVar()
txt=['Male','Female','Other']
for i in range(3):
    rdbtn=f'rdbtn{i}'
    rdbtn=tk.Radiobutton(win,text=txt[i],value=txt[i],
                          variable=var3)
    rdbtn.grid(row=3,column=1+i, sticky='E')
var3.set(0)

var4=tk.StringVar()
cbbox=ttk.Combobox(win,width=13,textvariable=var4,
                   state='readonly')
cbbox['value']=['India','America','Canada','Brazil']
cbbox.current(0)
cbbox.grid(row=4,column=1)
'''

###########
# Add Scale Widget:
'''
import tkinter as tk
import tkinter.ttk as ttk
win= tk.Tk()
win.title('My GUI')
win.geometry('300x300')

labels=['Name','Age','Email','Gender','Country','Weight']
for i in range(len(labels)):
    label='label'+str(i)
    label=ttk.Label(win,text=labels[i])
    label.grid(row=i, column=0,sticky='E',padx=2,pady=2)

var={'var0':tk.StringVar(),
     'var1':tk.StringVar(),
     'var2':tk.StringVar()}
entry=['entry0','entry1','entry2']
for i in range(len(var)):
    entry[i]=ttk.Entry(win,width=15,
                       textvariable=var['var'+str(i)])
    entry[i].grid(row=i,column=1,padx=2,pady=2)
entry[0].focus()

var3=tk.StringVar()
txt=['Male','Female','Other']
for i in range(3):
    rdbtn=f'rdbtn{i}'
    rdbtn=tk.Radiobutton(win,text=txt[i],value=txt[i], variable=var3)
    rdbtn.grid(row=3,column=1+i, sticky='E')
var3.set(0)

var4=tk.StringVar()
cbbox=ttk.Combobox(win,width=13,textvariable=var4, state='readonly')
cbbox['value']=['India','America','Canada','Brazil']
cbbox.current(0)
cbbox.grid(row=4,column=1)

var5=tk.DoubleVar()    
sc= tk.Scale(win,variable=var5,from_=40,to=60,orient=tk.HORIZONTAL)
sc.grid(row=5,column=1)
'''

# Add Checkbutton Widget:
'''
import tkinter as tk
import tkinter.ttk as ttk
win= tk.Tk()
win.title('My GUI')
win.geometry('300x300')

labels=['Name','Age','Email','Gender','Country','Weight']
for i in range(len(labels)):
    label='label'+str(i)
    label=tk.Label(win,text=labels[i])
    label.grid(row=i, column=0,sticky='E',padx=2,pady=2)

var={'var0':tk.StringVar(),
     'var1':tk.StringVar(),
     'var2':tk.StringVar()}
entry=['entry0','entry1','entry2']
for i in range(len(var)):
    entry[i]=tk.Entry(win,width=15,
                       textvariable=var['var'+str(i)])
    entry[i].grid(row=i,column=1,padx=2,pady=2)
entry[0].focus()

var3=tk.StringVar()
txt=['Male','Female','Other']
for i in range(3):
    rdbtn=f'rdbtn{i}'
    rdbtn=tk.Radiobutton(win,text=txt[i],value=txt[i], variable=var3)
    rdbtn.grid(row=3,column=1+i, sticky='E')
var3.set(0)

var4=tk.StringVar()
cbbox=ttk.Combobox(win,width=13,textvariable=var4, state='readonly')
cbbox['value']=['India','America','Canada','Brazil']
cbbox.current(0)
cbbox.grid(row=4,column=1)

var5=tk.DoubleVar()    
sc= tk.Scale(win,variable=var5,from_=40,to=60,orient=tk.HORIZONTAL)
sc.grid(row=5,column=1)

var6=tk.IntVar()
chkbtn1=tk.Checkbutton(win,text='Agree to all terms*',
                       variable=var6, state='disabled')
chkbtn1.select()
chkbtn1.grid(row=6,column=0,columnspan=3,sticky='W')

var7=tk.IntVar()
chkbtn2=tk.Checkbutton(win,text='Save details for future',
                       variable=var7)
chkbtn2.deselect()
chkbtn2.grid(row=7,column=0,columnspan=3,sticky='W')
'''

# Add a Button Widget:
'''
import tkinter as tk
win= tk.Tk()
win.title('My GUI')
win.geometry('300x300')

label=tk.Label(win,text='Enter an Integer')
label.grid(row=0, column=0,padx=2)

var=tk.StringVar()
entry=tk.Entry(win,width=5,textvariable=var)
entry.grid(row=0,column=1,padx=2)

var1=tk.StringVar()
label1=tk.Label(win,textvariable=var1)
label1.grid(row=0,column=2,padx=2)

def checkEvenOdd():
    num=var.get()
    if int(num)%2==0:
        var1.set('Even')
    else:
        var1.set('Odd')
        
btn = ttk.Button(win, text='Check', command= checkEvenOdd)
btn.grid(row=1, column=0)
'''

# Button in Form
'''
import tkinter as tk
import tkinter.ttk as ttk
from csv import DictWriter
import os

win= tk.Tk()
win.title('My GUI')
win.geometry('300x300')

labels=['Name','Age','Email','Gender','Country','Weight']
for i in range(len(labels)):
    label='label'+str(i)
    label=tk.Label(win,text=labels[i])
    label.grid(row=i, column=0,sticky='E',padx=2,pady=2)

var={'var0':tk.StringVar(),
     'var1':tk.StringVar(),
     'var2':tk.StringVar()}
entry=['entry0','entry1','entry2']
for i in range(len(var)):
    entry[i]=tk.Entry(win,width=15,
                       textvariable=var['var'+str(i)])
    entry[i].grid(row=i,column=1,padx=2,pady=2)
entry[0].focus()

var3=tk.StringVar()
txt=['Male','Female','Other']
for i in range(3):
    rdbtn=f'rdbtn{i}'
    rdbtn=tk.Radiobutton(win,text=txt[i],value=txt[i], variable=var3)
    rdbtn.grid(row=3,column=1+i, sticky='E')
var3.set(0)

var4=tk.StringVar()
cbbox=ttk.Combobox(win,width=13,textvariable=var4, state='readonly')
cbbox['value']=['India','America','Canada','Brazil']
cbbox.current(0)
cbbox.grid(row=4,column=1)

var5=tk.DoubleVar()    
sc= tk.Scale(win,variable=var5,from_=40,to=60,orient=tk.HORIZONTAL)
sc.grid(row=5,column=1)

var6=tk.IntVar()
chkbtn1=tk.Checkbutton(win,text='Agree to all terms*',
                       variable=var6, state='disabled')
chkbtn1.select()
chkbtn1.grid(row=6,column=0,columnspan=3,sticky='W')

var7=tk.IntVar()
chkbtn2=tk.Checkbutton(win,text='Save details for future',
                       variable=var7)
chkbtn2.deselect()
chkbtn2.grid(row=7,column=0,columnspan=3,sticky='W')

def submit():
    name=var['var0'].get()
    age=var['var1'].get()
    email=var['var2'].get()
    country=var3.get()
    gender=var4.get()
    weight=var5.get()
    future=var7.get()
    with open('Detail.csv','a',newline='') as file:
        writer= DictWriter(file,fieldnames=['Name','Age',
                                            'Email',
                                            'Country',
                                            'Gender',
                                            'Weight',
                                            'Future'])
        if os.stat('Detail.csv').st_size==0:
            writer.writeheader()
        writer.writerow({'Name':name.title(),
                         'Age':age,
                         'Email':email.lower(),
                         'Country':country,
                         'Gender':gender,'Weight':weight,
                         'Future':future})             
    var['var0'].set('')
    var['var1'].set('')
    var['var2'].set('')
    var3.set(0)
    var4.set('')
    var5.set(40)
    var7.set(0)
btn= ttk.Button(win,text='Submit',command=submit)
btn.grid(row=8,column=1,pady=2)
    
win.mainloop()
'''

# mainloop()
'''
- It is an infinite loop used to run the application,
wait for an event to occur and process the event till the
window is not closed.
'''

##########
# Add Messagebox Widget:
'''
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
win= tk.Tk()
win.title('My GUI')
win.geometry('500x500')

def info():
    msgbox.showinfo('Info','This is information')
btn1=tk.Button(win,text='INFO',command=info)
btn1.grid(row=0,column=0,pady=4)

def error():
    msgbox.showerror('Error','This is Error')
btn2=tk.Button(win,text='ERROR',command=error)
btn2.grid(row=1,column=0,pady=4)

def warn():
    msgbox.showwarning('Warning','This is warning')
btn3=tk.Button(win,text='WARNING',command=warn)
btn3.grid(row=2,column=0,pady=4)
'''

# Use in form:
'''
import tkinter as tk
import tkinter.ttk as ttk
from csv import DictWriter
import os

win= tk.Tk()
win.title('My GUI')
win.geometry('300x300')

labels=['Name','Age','Email','Gender','Country','Weight']
for i in range(len(labels)):
    label='label'+str(i)
    label=tk.Label(win,text=labels[i])
    label.grid(row=i, column=0,sticky='E',padx=2,pady=2)

var={'var0':tk.StringVar(),
     'var1':tk.StringVar(),
     'var2':tk.StringVar()}
entry=['entry0','entry1','entry2']
for i in range(len(var)):
    entry[i]=tk.Entry(win,width=15,
                       textvariable=var['var'+str(i)])
    entry[i].grid(row=i,column=1,padx=2,pady=2)
entry[0].focus()

var3=tk.StringVar()
txt=['Male','Female','Other']
for i in range(3):
    rdbtn=f'rdbtn{i}'
    rdbtn=tk.Radiobutton(win,text=txt[i],value=txt[i], variable=var3)
    rdbtn.grid(row=3,column=1+i, sticky='E')
var3.set(0)

var4=tk.StringVar()
cbbox=ttk.Combobox(win,width=13,textvariable=var4, state='readonly')
cbbox['value']=['India','America','Canada','Brazil']
cbbox.current(0)
cbbox.grid(row=4,column=1)

var5=tk.DoubleVar()    
sc= tk.Scale(win,variable=var5,from_=40,to=60,orient=tk.HORIZONTAL)
sc.grid(row=5,column=1)

var6=tk.IntVar()
chkbtn1=tk.Checkbutton(win,text='Agree to all terms*',
                       variable=var6, state='disabled')
chkbtn1.select()
chkbtn1.grid(row=6,column=0,columnspan=3,sticky='W')

var7=tk.IntVar()
chkbtn2=tk.Checkbutton(win,text='Save details for future',
                       variable=var7)
chkbtn2.deselect()
chkbtn2.grid(row=7,column=0,columnspan=3,sticky='W')

def submit():
    name=var['var0'].get()
    age=var['var1'].get()
    email=var['var2'].get()
    country=var3.get()
    gender=var4.get()
    weight=var5.get()
    future=var7.get()
    
    if name=='' or age=='' or email=='':
        msgbox.showinfo('Missing Fields',
                     'Name,Age,Email can\'t be left empty')
    elif age:
        try:
            age=int(age)
        except ValueError:
            msgbox.showerror('Wrong Fields Value',
                     'Age should be numeric')
        else:
            with open('Detail.csv','a',newline='') as file:
                writer= DictWriter(file,fieldnames=['Name','Age',
                                                    'Email',
                                                    'Country',
                                                    'Gender',
                                                    'Weight',
                                                    'Future'])
                if os.stat('Detail.csv').st_size==0:
                    writer.writeheader()
                writer.writerow({'Name':name.title(),
                                 'Age':age,
                                 'Email':email.lower(),
                                 'Country':country,
                                 'Gender':gender,'Weight':weight,
                                 'Future':future})             
            var['var0'].set('')
            var['var1'].set('')
            var['var2'].set('')
            var3.set(0)
            var4.set('')
            var5.set(40)
            var7.set(0)
    
btn= ttk.Button(win,text='Submit',command=submit)
btn.grid(row=8,column=1,pady=2)
    
win.mainloop()
'''

#############
# Add Menubar Widget:
'''
import tkinter as tk
win= tk.Tk()
win.title('My GUI')
win.geometry('300x300')

def new():
    win2= tk.Tk()
    win2.title('My GUI')
    win2.geometry('500x500')
    
def openExisting():
    print('Open Existing')

def end():
    win.quit()
    win.destroy()
    exit()

def about():
    print('About the App')
    
mbar= tk.Menu(win)
win.config(menu=mbar) #place menubar
  
fileMenu=tk.Menu(mbar,tearoff=0)
fileMenu.add_command(label='New',command=new)
fileMenu.add_command(label='Open',command=openExisting)
fileMenu.add_separator()
fileMenu.add_command(label='Exit',command=end)
mbar.add_cascade(label='File',menu=fileMenu)

helpMenu=tk.Menu(mbar,tearoff=0)
helpMenu.add_command(label='About',command=about)
mbar.add_cascade(label='Help',menu=helpMenu)

win.mainloop()
'''

########
# Add Frame Widget:
'''
import tkinter as tk
win= tk.Tk()
win.title('My GUI')
win.geometry('300x300')

frame1= tk.Frame(win, bd=3, relief='solid')

labels=['Name','Age','Email']
for i in range(len(labels)):
    label='label'+str(i)
    label=tk.Label(frame1,text=labels[i])
    label.grid(row=i, column=0,sticky='E')

var={'var0':tk.StringVar(),
     'var1':tk.StringVar(),
     'var2':tk.StringVar()}
entry=['entry0','entry1','entry2']
for i in range(len(var)):
    entry[i]=tk.Entry(frame1,width=15,
                       textvariable=var['var'+str(i)])
    entry[i].grid(row=i,column=1)
entry[0].focus()

frame2= tk.Frame(win, bd=3, relief='solid')

var3=tk.StringVar()
label=tk.Label(frame2,text='Gender')
label.grid(row=0, column=0,sticky='E')

txt=['Male','Female','Other']
for i in range(3):
    rdbtn=f'rdbtn{i}'
    rdbtn=tk.Radiobutton(frame2,text=txt[i],value=txt[i], variable=var3)
    rdbtn.grid(row=0,column=1+i)
var3.set(0)

frame3= tk.Frame(win, bd=3, relief='solid')

labels=['Country','Weight']
for i in range(len(labels)):
    label='label'+str(i)
    label=tk.Label(frame3,text=labels[i])
    label.grid(row=i, column=0,sticky='E')
    
var4=tk.StringVar()
cbbox=ttk.Combobox(frame3,width=13,textvariable=var4, state='readonly')
cbbox['value']=['India','America','Canada','Brazil']
cbbox.current(0)
cbbox.grid(row=0,column=1)

var5=tk.DoubleVar()    
sc= tk.Scale(frame3,variable=var5,from_=40,to=60,orient=tk.HORIZONTAL)
sc.grid(row=1,column=1)

frame4=tk.Frame(win, bd=3, relief='solid')

var6=tk.IntVar()
chkbtn1=tk.Checkbutton(frame4,text='Agree to all terms*',
                       variable=var6, state='disabled')
chkbtn1.select()
chkbtn1.grid(row=0,column=0,columnspan=3,sticky='W')

var7=tk.IntVar()
chkbtn2=tk.Checkbutton(frame4,text='Save details for future',
                       variable=var7)
chkbtn2.deselect()
chkbtn2.grid(row=1,column=0,columnspan=3,sticky='W')

def submit():
    name=var['var0'].get()
    age=var['var1'].get()
    email=var['var2'].get()
    country=var3.get()
    gender=var4.get()
    weight=var5.get()
    future=var7.get()
    
    if name=='' or age=='' or email=='':
        msgbox.showinfo('Missing Fields',
                     'Name,Age,Email can\'t be left empty')
    elif age:
        try:
            age=int(age)
        except ValueError:
            msgbox.showerror('Wrong Fields Value',
                     'Age should be numeric')
        else:
            with open('File2Save/Detail.csv','a',newline='') as file:
                writer= DictWriter(file,fieldnames=['Name','Age',
                                                    'Email',
                                                    'Country',
                                                    'Gender',
                                                    'Weight',
                                                    'Future'])
                if os.stat('File2Save/Detail.csv').st_size==0:
                    writer.writeheader()
                writer.writerow({'Name':name.title(),
                                 'Age':age,
                                 'Email':email.lower(),
                                 'Country':country,
                                 'Gender':gender,'Weight':weight,
                                 'Future':future})             
            var['var0'].set('')
            var['var1'].set('')
            var['var2'].set('')
            var3.set(0)
            var4.set('')
            var5.set(40)
            var7.set(0)
    
btn= ttk.Button(frame4,text='Submit',command=submit)
btn.grid(row=2,column=0)

frame1.grid(row=0,column=0,pady=2)
frame2.grid(row=1,column=0,pady=2)
frame3.grid(row=2,column=0,pady=2)
frame4.grid(row=3,column=0,pady=2)

frames=[frame1,frame2,frame3,frame4]
for frame in frames:
    for child in frame.winfo_children():
        child.grid_configure(padx=4,pady=2)

win.mainloop()
'''

########
# Add LabelFrame Widget:
'''
import tkinter as tk
win= tk.Tk()
win.title('My GUI')
win.geometry('300x400')

frame1= tk.LabelFrame(win, text='Basic Info.',bd=3, relief='solid')

labels=['Name','Age','Email']
for i in range(len(labels)):
    label='label'+str(i)
    label=tk.Label(frame1,text=labels[i])
    label.grid(row=i, column=0,sticky='E')

var={'var0':tk.StringVar(),
     'var1':tk.StringVar(),
     'var2':tk.StringVar()}
entry=['entry0','entry1','entry2']
for i in range(len(var)):
    entry[i]=tk.Entry(frame1,width=15,
                       textvariable=var['var'+str(i)])
    entry[i].grid(row=i,column=1)
entry[0].focus()

frame2= tk.LabelFrame(win, text='Personal Info.',bd=3, relief='solid')

var3=tk.StringVar()
label=tk.Label(frame2,text='Gender')
label.grid(row=0, column=0,sticky='E')

txt=['Male','Female','Other']
for i in range(3):
    rdbtn=f'rdbtn{i}'
    rdbtn=tk.Radiobutton(frame2,text=txt[i],value=txt[i], variable=var3)
    rdbtn.grid(row=0,column=1+i)
var3.set(0)

frame3= tk.LabelFrame(win, text='General Info.', bd=3, relief='solid')

labels=['Country','Weight']
for i in range(len(labels)):
    label='label'+str(i)
    label=tk.Label(frame3,text=labels[i])
    label.grid(row=i, column=0,sticky='E')
    
var4=tk.StringVar()
cbbox=ttk.Combobox(frame3,width=13,textvariable=var4, state='readonly')
cbbox['value']=['India','America','Canada','Brazil']
cbbox.current(0)
cbbox.grid(row=0,column=1)

var5=tk.DoubleVar()    
sc= tk.Scale(frame3,variable=var5,from_=40,to=60,orient=tk.HORIZONTAL)
sc.grid(row=1,column=1)

frame4=tk.LabelFrame(win, text='Submit Info.',bd=3, relief='solid')

var6=tk.IntVar()
chkbtn1=tk.Checkbutton(frame4,text='Agree to all terms*',
                       variable=var6, state='disabled')
chkbtn1.select()
chkbtn1.grid(row=0,column=0,columnspan=3,sticky='W')

var7=tk.IntVar()
chkbtn2=tk.Checkbutton(frame4,text='Save details for future',
                       variable=var7)
chkbtn2.deselect()
chkbtn2.grid(row=1,column=0,columnspan=3,sticky='W')

def submit():
    name=var['var0'].get()
    age=var['var1'].get()
    email=var['var2'].get()
    country=var3.get()
    gender=var4.get()
    weight=var5.get()
    future=var7.get()
    
    if name=='' or age=='' or email=='':
        msgbox.showinfo('Missing Fields',
                     'Name,Age,Email can\'t be left empty')
    elif age:
        try:
            age=int(age)
        except ValueError:
            msgbox.showerror('Wrong Fields Value',
                     'Age should be numeric')
        else:
            with open('File2Save/Detail.csv','a',newline='') as file:
                writer= DictWriter(file,fieldnames=['Name','Age',
                                                    'Email',
                                                    'Country',
                                                    'Gender',
                                                    'Weight',
                                                    'Future'])
                if os.stat('File2Save/Detail.csv').st_size==0:
                    writer.writeheader()
                writer.writerow({'Name':name.title(),
                                 'Age':age,
                                 'Email':email.lower(),
                                 'Country':country,
                                 'Gender':gender,'Weight':weight,
                                 'Future':future})             
            var['var0'].set('')
            var['var1'].set('')
            var['var2'].set('')
            var3.set(0)
            var4.set('')
            var5.set(40)
            var7.set(0)
    
btn= tk.Button(frame4,text='Submit',command=submit)
btn.grid(row=2,column=0)

frame1.grid(row=0,column=0,pady=2)
frame2.grid(row=1,column=0,pady=2)
frame3.grid(row=2,column=0,pady=2)
frame4.grid(row=3,column=0,pady=2)

frames=[frame1,frame2,frame3,frame4]
for frame in frames:
    for child in frame.winfo_children():
        child.grid_configure(padx=4,pady=2)

win.mainloop()
'''

########
# Add Tabbed Widget:
'''
import tkinter as tk
import tkinter.ttk as ttk
win= tk.Tk()
win.title('My GUI')
win.geometry('300x300')

nb=ttk.Notebook(win)
nb.grid(row=0,column=0)

tab1=tk.Frame(nb)
nb.add(tab1,text='Personal Detail')

tab2=ttk.Frame(nb)
nb.add(tab2,text='Objective')

win.mainloop()
'''

# Add Widgets to tabs
# Add Scrolltext Widget:
'''
import tkinter as tk
import tkinter.ttk as ttk
from csv import DictWriter
import os
import tkinter.scrolledtext as scroll

win= tk.Tk()
win.title('My GUI')
win.geometry('450x450')

topframe=tk.Frame(win, width=300, height=100, bd=3,relief='solid')
topframe.pack(fill='x')

label=tk.Label(topframe,text='GATE Exam',font='Times 20 bold')
label.pack()

nb=ttk.Notebook(win)
nb.pack(fill='both')

tab1=tk.Frame(nb)
nb.add(tab1,text='Personal Detail')

frame1= tk.Frame(tab1, bd=3, relief='solid')

labels=['Name','Age','Email']
for i in range(len(labels)):
    label='label'+str(i)
    label=tk.Label(frame1,text=labels[i])
    label.grid(row=i, column=0,sticky='E')

var={'var0':tk.StringVar(),
     'var1':tk.StringVar(),
     'var2':tk.StringVar()}
entry=['entry0','entry1','entry2']
for i in range(len(var)):
    entry[i]=tk.Entry(frame1,width=15,
                       textvariable=var['var'+str(i)])
    entry[i].grid(row=i,column=1)
entry[0].focus()

frame2= tk.Frame(tab1, bd=3, relief='solid')

var3=tk.StringVar()
label=tk.Label(frame2,text='Gender')
label.grid(row=0, column=0,sticky='E')

txt=['Male','Female','Other']
for i in range(3):
    rdbtn=f'rdbtn{i}'
    rdbtn=tk.Radiobutton(frame2,text=txt[i],value=txt[i], variable=var3)
    rdbtn.grid(row=0,column=1+i)
var3.set(0)

frame3= tk.Frame(tab1, bd=3, relief='solid')

labels=['Country','Weight']
for i in range(len(labels)):
    label='label'+str(i)
    label=tk.Label(frame3,text=labels[i])
    label.grid(row=i, column=0,sticky='E')
    
var4=tk.StringVar()
cbbox=ttk.Combobox(frame3,width=13,textvariable=var4, state='readonly')
cbbox['value']=['India','America','Canada','Brazil']
cbbox.current(0)
cbbox.grid(row=0,column=1)

var5=tk.DoubleVar()    
sc= tk.Scale(frame3,variable=var5,from_=40,to=60,orient=tk.HORIZONTAL)
sc.grid(row=1,column=1)

frame4=tk.Frame(tab1, bd=3, relief='solid')

var6=tk.IntVar()
chkbtn1=tk.Checkbutton(frame4,text='Agree to all terms*',
                       variable=var6, state='disabled')
chkbtn1.select()
chkbtn1.grid(row=0,column=0,columnspan=3,sticky='W')

var7=tk.IntVar()
chkbtn2=tk.Checkbutton(frame4,text='Save details for future',
                       variable=var7)
chkbtn2.deselect()
chkbtn2.grid(row=1,column=0,columnspan=3,sticky='W')

def submit():
    name=var['var0'].get()
    age=var['var1'].get()
    email=var['var2'].get()
    country=var3.get()
    gender=var4.get()
    weight=var5.get()
    future=var7.get()
    
    if name=='' or age=='' or email=='':
        msgbox.showinfo('Missing Fields',
                     'Name,Age,Email can\'t be left empty')
    elif age:
        try:
            age=int(age)
        except ValueError:
            msgbox.showerror('Wrong Fields Value',
                     'Age should be numeric')
        else:
            with open('File2Save/Detail.csv','a',newline='') as file:
                writer= DictWriter(file,fieldnames=['Name','Age',
                                                    'Email',
                                                    'Country',
                                                    'Gender',
                                                    'Weight',
                                                    'Future'])
                if os.stat('File2Save/Detail.csv').st_size==0:
                    writer.writeheader()
                writer.writerow({'Name':name.title(),
                                 'Age':age,
                                 'Email':email.lower(),
                                 'Country':country,
                                 'Gender':gender,'Weight':weight,
                                 'Future':future})             
            var['var0'].set('')
            var['var1'].set('')
            var['var2'].set('')
            var3.set(0)
            var4.set('')
            var5.set(40)
            var7.set(0)
    
btn= ttk.Button(frame4,text='Submit',command=submit)
btn.grid(row=2,column=0)

frame1.grid(row=0,column=0,pady=2)
frame2.grid(row=1,column=0,pady=2)
frame3.grid(row=2,column=0,pady=2)
frame4.grid(row=3,column=0,pady=2)

frames=[frame1,frame2,frame3,frame4]
for frame in frames:
    for child in frame.winfo_children():
        child.grid_configure(padx=4,pady=2)

tab2=tk.Frame(nb)
nb.add(tab2,text='Objective')

scr=scroll.ScrolledText(tab2,width=35,height=5,wrap=tk.WORD)
scr.grid(column=0)

win.mainloop()
'''
