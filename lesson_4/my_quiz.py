import sqlite3
from queries import *

conn = sqlite3.connect("questions.db")
cursor = conn.cursor()
cursor.execute(table_quiz)
cursor.execute(table_questions)
cursor.execute(table_quiz_content)
cursor.executemany('''INSERT INTO quiz (q_name) VALUES (?)''', quizes)
cursor.executemany('''INSERT INTO questions (question, answer, wrong1, wrong2, wrong3) VALUES (?,?,?,?,?)''', questions)
cursor.execute('''PRAGMA foreing_keys=on''')
cursor.executemany('''INSERT INTO quiz_content (quiz_id, question_id) VALUES (?,?)''', quiz_contents)
cursor.execute('''SELECT * FROM quiz_content''')
content = cursor.fetchall()
print(content)
conn.commit()

quiz = int(input())
quest = int(input())

def get_question_after(question_id = 0, quiz_id=1):
    global quest, content
    for k in content:
        if k[0] > question_id and k[1] == quiz_id:
            quest = k[0]
            cursor.execute('''SELECT * FROM questions WHERE id = (?)''', [k[2]])
            data = cursor.fetchall()
            return data
    return "Done"
        
print(get_question_after(quest, quiz))
cursor.execute('''DROP TABLE IF EXISTS quiz_content''')
cursor.execute('''DROP TABLE IF EXISTS questions''')
cursor.execute('''DROP TABLE IF EXISTS quiz''')
conn.commit()