from flask import Flask, request, jsonify
from flask_cors import CORS
import pyodbc

app = Flask(__name__)
CORS(app)  # <-- Enable CORS for all routes

# Azure SQL connection info
server = 'studentidvalidation.database.windows.net'
database = 'student_db'
username = 'studentadmin'
password = 'Student@1234'
driver = '{ODBC Driver 17 for SQL Server}'

def get_db_connection():
    try:
        conn = pyodbc.connect(
            f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        )
        return conn
    except Exception as e:
        print("Error connecting to Azure SQL:", e)
        return None

@app.route('/validate', methods=['POST'])
def validate_id():
    data = request.get_json()
    student_id = data.get('student_id')

    if not student_id:
        return jsonify({'message': 'Student ID is required ❌'}), 400

    conn = get_db_connection()
    if not conn:
        return jsonify({'message': 'Server could not connect to the database ❌'}), 500

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT name, department FROM Students WHERE student_id = ?", (student_id,))
        record = cursor.fetchone()
        conn.close()

        if record:
            return jsonify({
                'message': 'Access Granted ✅',
                'student_id': student_id,
                'name': record[0],
                'department': record[1]
            })
        else:
            return jsonify({'message': 'Access Denied ❌'})

    except Exception as e:
        print("Error querying database:", e)
        return jsonify({'message': 'Error querying database ❌'}), 500

if __name__ == '__main__':
    app.run(debug=True)
