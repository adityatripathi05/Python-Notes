# Simple Quiz GUI app
# Create a question and multiple choice options of which one is correct
# When correct option is clicked a message displays that option is correct!

from tkinter import *

q = [
    "Q1. Capital of India?",
    "Q2. What are the symptoms of suffering from kidney disease?",
    "Q3.  If a person is put on dialysis, he is suffering from?",
    "Q4.  What is the shape of the kidney?",
    "Q5.  Secondary air pollutant is ?",
]

options = [
    ["Delhi", "Mumbai", "Kolkata", "Chennai"],
    ["High blood pressure", "Respiration problem", "Swelling on face, legs etc", "All of the above"],
    ["Heart disease", "Kidney disease", "Respiratory problem", "None of the above"],
    ["It is an oval shaped organ", "It is bean shaped organ", "It is rectangular in shape", "It has no fixed shape"],
    ["Ozone", "Carbon monoxide", "Nitrogen Dioxide", "Sulphur dioxide"],
]

a = [1, 4, 2, 2, 1]

class Quiz:
    def __init__(self, master):
        self.opt_selected = IntVar()
        self.qn = 0
        self.correct = 0
        self.ques = self.create_q(master, self.qn)
        self.opts = self.create_options(master, 4)
        self.display_q(self.qn)
        self.button = Button(master, text="Back", command=self.back_btn)
        self.button.pack(side=BOTTOM)
        self.button = Button(master, text="Next", command=self.next_btn)
        self.button.pack(side=BOTTOM)

    def create_q(self, master, qn):
        w = Label(master, text=q[qn])
        w.pack(side=TOP)
        return w

    def create_options(self, master, n):
        b_val = 0
        b = []
        while b_val < n:
            btn = Radiobutton(master, text="foo", variable=self.opt_selected, value=b_val+1)
            b.append(btn)
            btn.pack(side=TOP, anchor="w")
            b_val = b_val + 1
        return b

    def display_q(self, qn):
        b_val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q[qn]
        for op in options[qn]:
            self.opts[b_val]['text'] = op
            b_val = b_val + 1

    def check_q(self, qn):
        if self.opt_selected.get() == a[qn]:
            return True
        return False

    def print_results(self):
        print("Score: ", self.correct, "/", len(q))

    def back_btn(self):
        print("go back")

    def next_btn(self):
        if self.check_q(self.qn):
            print("Correct")
            self.correct += 1
        else:
            print("Wrong")
        self.qn = self.qn + 1
        if self.qn >= len(q):
            self.print_results()
            root.destroy()
        else:
            self.display_q(self.qn)

root = Tk()
root.geometry("500x300")
root.title("Simple Quiz App")
app = Quiz(root)
root.mainloop()

