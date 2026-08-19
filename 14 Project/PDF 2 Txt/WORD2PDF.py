'''pip install docx2pdf'''


import sys
import os
from docx2pdf import convert
import tkinter as tk
from pathlib import Path
import tkinter.messagebox as msgbox
from tkinter import filedialog


def Word_to_pdf():   
    def word_to_pdf(input_file,output_file):
        in_file =str(input_file)
        out_file = str(output_file)+'.pdf'
        in_file =  in_file.replace('/','\\')
        convert(in_file,out_file)
        print(".DOCX to PDF conversion sucessful and Saved")


    def validate_inputs(src_file, dest_dir, out_file):
        errors = False
        error_msgs = []
        
        # Check for a doc file
        if Path(src_file).suffix.upper() != ".DOCX":
            errors = True
            entry1.delete(0,tk.END)
            error_msgs.append("Please select a .DOC or .DOCX   input file")
        
        # Check for a directory
        if not(Path(dest_dir)).exists():
            errors = True
            error_msgs.append("Please Select a valid output directory")

        # Check for a file name
        if len(out_file) < 1:
            errors = True
            error_msgs.append("Please enter a file name")
           
        return(errors, error_msgs)

    def press():
        src_file = word_path.get()
        dest_dir = pdf_path.get()
        out_file = pdf_name.get()
        errors, error_msg = validate_inputs(src_file, dest_dir, out_file)
        if errors:
            msgbox.showerror('Error',"\n".join(error_msg))
        else:
            word_to_pdf(src_file,Path(dest_dir,out_file))
    
    def quit():
        app.destroy()
        
    def browse_to_word(self):
        wfile_path = filedialog.askopenfilename()
        entry1.insert(tk.END, wfile_path)
        
    def browse_to_pdf(self):
        pfolder_path = filedialog.askdirectory()
        entry2.insert(tk.END, pfolder_path)

    app=tk.Tk()
    app.title('Word to PDF Converter')
    app.geometry("600x100")
    app.resizable(0,0)

    # Add the interactive components
    label1 = tk.Label(app,text="Choose Source Word File to convert")
    label1.grid(row=0,column=0)
    
    word_path=tk.StringVar()
    entry1 = tk.Entry(app,width=65,textvariable=word_path)
    entry1.bind("<Enter>", browse_to_word)
    entry1.grid(row=0,column=1)

    label2 = tk.Label(app,text="Select Output Directory")
    label2.grid(row=1,column=0)
    
    pdf_path=tk.StringVar()
    entry2 = tk.Entry(app,width=65,textvariable=pdf_path)
    entry2.bind("<Enter>", browse_to_pdf)
    entry2.grid(row=1,column=1)

    label3 = tk.Label(app,text="Output file name")
    label3.grid(row=2,column=0)
    pdf_name=tk.StringVar()
    entry3 = tk.Entry(app,width=65,textvariable=pdf_name)
    entry3.grid(row=2,column=1)

    btn1 = tk.Button(app,text="Process",command=press)
    btn1.grid(row=3,column=0)
    
    btn2 = tk.Button(app,text="Quit",command=quit)
    btn2.grid(row=3,column=1)
    app.mainloop()
Word_to_pdf()
