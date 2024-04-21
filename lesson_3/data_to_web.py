from flask import Flask, url_for, redirect
import os
import sqlite3

year = int(input())

folder = os.getcwd()
app = Flask(__name__, static_folder=folder)

@app.route("/")
def index():
    global year
    conn = sqlite3.connect("Artistc.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM artists WHERE "Birth Year" = (?)', [year])
    data = cursor.fetchall()
    names = []
    for k in data:
        names.append(k[1])
    if len(data) > 1:
        return  f'<p>{names}</p>'
    if len(data) == 1:
        return f'<p>{names[0]}</p>'
    return '<p>По Вашему запросу ничего не найдено</p>'

if __name__ == '__main__':
    app.run()