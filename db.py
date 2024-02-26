from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

conn=mysql.connector.connect(
    host='localhost',
    username='root',
    password='root',
    database='barbar'
)
@app.route('/')
def home():
    return render_template('login.html')
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    cursor = conn.cursor()

    insert_query = "INSERT INTO users (username, password) VALUES ('kishore', 8903)"
    user_data = (username, password)
    cursor.execute(insert_query, user_data)
    conn.commit()
    
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

