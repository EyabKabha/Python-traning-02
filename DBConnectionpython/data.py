import mysql.connector
import pandas as pd

cnx = mysql.connector.connect(user='root', password='1234',
                              host='localhost',
                              database='buscal')

cursor = cnx.cursor()

cursor.execute("SELECT * FROM employees")
rowData = cursor.fetchall()

num_fields = len(cursor.description)
field_names = [i[0] for i in cursor.description]
table = cursor.execute("Show tables;")

df = pd.DataFrame(rowData)

print('=============================================================')
print('--------------------  Get Data from MySQL -------------------')
print('--------------------  Table name employees ------------------')
print('=============================================================')

path = input('Please Enter a location to where save the excel file ')

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter(f'{path}\\data.xlsx', engine='xlsxwriter')

if(path==''):
    writer = pd.ExcelWriter(f'Data.xlsx', engine='xlsxwriter')
else:
    writer = pd.ExcelWriter(f'{path}\\Data.xlsx', engine='xlsxwriter')



# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Data', index=False, header=field_names)

# Close the Pandas Excel writer and output the Excel file.
writer.save()

print('-------- The file extracted successfully from the DB --------')
input()