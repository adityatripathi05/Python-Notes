import tkinter as tk
import random as rd
class Game(tk.Tk):
    def __init__(self):
        super(Game,self).__init__()
        self.title('Color Game')
        self.score=0
        self.attempt=1
        self.color_optn=['black','red','blue','yellow','green']
        self.frame1=tk.Frame(self)
        self.frame1.pack()
        tk.Label(self.frame1,
                 text='Welcome to Color Game').pack()
        tk.Label(self.frame1,
                 text='Identify the color').pack()
        self.frame2=tk.Frame(self)
        self.frame2.pack()
        self.label_txt()
        self.frame3=tk.Frame(self)
        self.frame3.pack()
        self.ip=tk.Entry(self.frame3,
                         textvariable=self.color_optn)
        self.ip.focus()
        self.ip.bind("<Return>", self.evaluate)
        self.ip.pack()
        self.frame4=tk.Frame(self)
        self.frame4.pack()
        self.label_score()

    def label_txt(self):
        self.fnt_color=rd.choice(self.color_optn)
        self.txt=tk.Label(self.frame2,
                 text=rd.choice(self.color_optn),
                 fg=self.fnt_color)
        self.txt.pack()

    def label_score(self):
        self.sc=tk.Label(self.frame4,text=f'Score {self.score}')
        self.sc.pack()

    def evaluate(self,event):
        self.attempt+=1
        myentry=self.ip.get()
        self.ip.delete(0,tk.END)
        if myentry.lower()== self.fnt_color:
            self.score+=1
            self.sc.destroy()
            self.label_score()
            self.txt.destroy()
            self.label_txt()
        if self.attempt==5:
            self.ip.config(state='disabled')
      
if __name__=='__main__':
    win=Game()
    win.mainloop()
