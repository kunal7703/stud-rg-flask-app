from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)  # ✅ this line must be present before any @app.route

# Database config
db_config = {
    'host': 'db',
    'user': 'root',
    'password': 'password',
    'database': 'studentsdb'
}

@app.route('/', methods=['GET'])
def home():
    return render_template('register.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    course = request.form['course']
    address = request.form['address']

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO students (name, email, phone, course, address) VALUES (%s, %s, %s, %s, %s)',
        (name, email, phone, course, address)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return 'Student Registered Successfully!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

 
