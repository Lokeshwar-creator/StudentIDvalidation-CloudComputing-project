import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=studentidvalidation.database.windows.net;DATABASE=student_db;UID=studentadmin;PWD=Student@1234'
)
cursor = conn.cursor()
cursor.execute("SELECT TOP 1 * FROM Students")
print(cursor.fetchone())
conn.close()
