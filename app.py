from flask import Flask, render_template, request, redirect, url_for
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Change to your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Query the database for the user
    user = User.query.filter_by(username=username, password=password).first()

    if user:
        return redirect(url_for('success'))
    else:
        return "Invalid username or password"

@app.route('/success')
def success():
    return "Login successful"

if __name__ == '__main__':
    app.run(debug=True)
