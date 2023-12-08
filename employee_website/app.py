from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

DATABASE = 'employee_data.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM employees')
    data = cursor.fetchall()

    conn.close()

    return render_template('home.html', data=data)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)