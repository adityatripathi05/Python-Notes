# How you can extract tables in PDF
'''
- Using camelot library in Python.
- Camelot is a Python library and a command-line tool that makes it easy for
anyone to extract data tables trapped inside PDF files.
- Install required dependencies: Tkinter and ghostscript
- Install library: pip3 install camelot-py[cv]
'''
import camelot

# PDF file to extract tables from
file = "sales_funnel.pdf"

# extract all the tables in the PDF file
# read_pdf() function extracts all tables in a PDF file
tables = camelot.read_pdf(file)

# number of tables extracted
print("Total tables extracted:", tables.n)

# print the first table as Pandas DataFrame
print(tables.df)

# export the table to a CSV file
# export individually
tables[0].to_csv("sales1.csv")

# or export all in a zip
#tables.export("sales2.csv", f="csv", compress=True)

'''
- f parameter indicates the file format, in this case "csv".
- We can export to other formats such as 'html', 'JSON' and 'Excel'
- By setting compress parameter equals to True, this will create a ZIP
file that contains all the tables in CSV format.
'''








