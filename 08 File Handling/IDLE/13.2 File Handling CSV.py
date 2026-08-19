# csv File Handling: comma seperated values
# It's a common format to store tabular data.
# Default delimiter for these types of file is , (comma)
'''
with open('tab1.csv','a') as file:
    file.write('Name,Corona Test')
    file.write('\n')
    file.write('Aditya,neg')
    file.write('\n')
    print('Written')
'''

# Define a function for writing on file.
'''
def write_file(name,test):
    with open('tab1.csv','a') as file:
        file.write(f'{name},{test}')
    print('Written')    

write_file('Neetu','neg')
'''

# csv file handling: csv module
# for write operation: writer() and DictWriter()
# writer()
'''
import csv
with open('tab2.csv','w',newline='') as file:
    #to avoid newline after every row, we can give
    #newline argument as empty string '' while opening file.
    writer_obj= csv.writer(file)
    # writer() return object type data which will store
    # in variable writer_obj
    writer_obj.writerow(['Name','Corona Test'])
    writer_obj.writerow(['Manish','pos'])
    # writerow() will write single row at a time.
    writer_obj.writerow(['Preeti','neg'])
    writer_obj.writerows([['Bhuwan','pos'],
                          ['Shiv','pos']])
    # writerows() will write multiple rows at a time.
    print('Written')
'''

# DictWriter():
'''
import csv
with open('tab3.csv','w',newline='') as file:
    writer_obj= csv.DictWriter(file,fieldnames=['Name',
                                           'Corona Test'])
    writer_obj.writeheader()
    writer_obj.writerow({'Name':'Manish',
                         'Corona Test':'pos'})
    writer_obj.writerow({'Corona Test':'neg',
                         'Name':'Preeti'})
    writer_obj.writerows([{'Name':'Bhuwan',
                           'Corona Test':'pos'},
                          {'Name':'Shiv',
                           'Corona Test':'pos'}])
    print("Written")
'''

# for read operation: reader() and DictReader()
# reader()
'''
import csv
with open('tab3.csv') as file:
    reader_obj= csv.reader(file)
    # reader() return iterator object type data.
    print(reader_obj)
    for i in reader_obj:
        print(i) # Each row as List
'''

# If we want to read only 'Name' column:
'''
import csv
with open('tab3.csv') as file:
    reader_obj= csv.reader(file)
    for i in reader_obj:
        print(i[0])
'''

# DictReader():
'''
import csv
with open('tab3.csv') as file:
    reader_obj= csv.DictReader(file)
    #reader_obj will be an instance of class which also
    #work as iterator
    for i in reader_obj:
        print(i) # Each row as Dictionary
'''

# If we want to read only 'Name' column:
'''
import csv
with open('tab3.csv') as file:
    reader_obj= csv.DictReader(file)
    for i in reader_obj:
        print(i['Name'])
'''





