import psycopg2
import csv
# import mssql
import pyodbc

driver = 'ODBC Driver 17 for SQL Server'
server = 'DESKTOP-NSHCQFO'
db1 = 'mvcDB'
tcon = 'yes'
# uname = 'DESKTOP-NSHCQFO/Brian Tran'
# pword = '**my-password**'
# conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="Phili467")

conn = pyodbc.connect(DRIVER=driver, 
					  SERVER=server,
					  DATABASE=db1)
					  # Trusted_Connection=tcon)
cur = conn.cursor()
targetCsv = 'C:/Users/Admin/Downloads/djangularDataScientist-master/customerStats/customer.csv'
# targetCsv
with open('customerGender1.csv', 'r') as f:
# Notice that we don't need the `csv` module.
	next(f) # Skip the header row.
	cur.copy_from(
		f, 
		'public.customers_customer', sep=',', 
		columns=['ID', 'Name', 'Age', 'Active']
		)
	conn.commit()