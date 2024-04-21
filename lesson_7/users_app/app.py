from flask import Flask, render_template

users_list = [("Ivan", 39), ("Natalia", 21), ("Porfiriy", 62), ("Oleg", 37), ("Rodion", 26)]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/users")
def users():
    return render_template('users.html', header = "Users", users_list = users_list)

app.run(debug=True)