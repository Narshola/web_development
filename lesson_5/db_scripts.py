import sqlite3
from queries import *

db_name = 'quiz.sqlite'
conn = None
cursor = None

def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

def close():
    cursor.close()
    conn.close()

def do(query):
    cursor.execute(query)
    conn.commit()

def clear_db():
    ''' удаляет все таблицы '''
    open()
    query = '''DROP TABLE IF EXISTS quiz_content'''
    do(query)
    query = '''DROP TABLE IF EXISTS questions'''
    do(query)
    query = '''DROP TABLE IF EXISTS quiz'''
    do(query)
    close()

    

def fill_tables():
    open()
    do('''PRAGMA foreing_keys=on''')
    cursor.executemany('''INSERT INTO quiz (q_name) VALUES (?)''', quizes)
    cursor.executemany('''INSERT INTO questions (question, answer, wrong1, wrong2, wrong3) VALUES (?,?,?,?,?)''', questions)
    cursor.executemany('''INSERT INTO quiz_content (quiz_id, question_id) VALUES (?,?)''', quiz_contents)
    conn.commit()
    # close()

def create():
    open()
    do(table_quiz)
    do(table_questions)
    do(table_quiz_content)
    fill_tables()
    close()

def get_question_after(question_id = 0, quiz_id = 1):
    open()
    query = '''
    SELECT quiz_content.id, questions.question, questions.answer, questions.wrong1, questions.wrong2, questions.wrong3
    FROM questions, quiz_content
    WHERE quiz_content.question_id = questions.id
    AND quiz_content.id > ? AND quiz_content.quiz_id == ?
    ORDER BY quiz_content.id'''
    cursor.execute(query, [question_id, quiz_id])
    result = cursor.fetchone()
    close()
    return result

def show(table):
    query = 'SELECT * FROM ' + table
    open()
    cursor.execute(query)
    print(cursor.fetchall())
    close()

def show_tables():
    show('questions')
    show('quiz')
    show('quiz_content')

def main():
    clear_db()
    create()
    show_tables()

if __name__ == "__main__":
    main()
