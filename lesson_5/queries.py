table_quiz = "CREATE TABLE IF NOT EXISTS quiz (id INTEGER PRIMARY KEY,q_name VARCHAR)"
table_questions = "CREATE TABLE IF NOT EXISTS questions (id INTEGER PRIMARY KEY,question VARCHAR,answer VARCHAR,wrong1 VARCHAR,wrong2 VARCHAR,wrong3 VARCHAR)"
table_quiz_content = "CREATE TABLE IF NOT EXISTS quiz_content (id INTEGER PRIMARY KEY,quiz_id INTEGER,question_id INTEGER,FOREIGN KEY (quiz_id) REFERENCES quiz (id),FOREIGN KEY (question_id) REFERENCES questions (id))"


quizes = [
        ('Своя игра', ),
        ('Кто хочет стать миллионером?', ),
        ('Самый умный', )]

questions = [
        ('Сколько месяцев в году имеют 28 дней?', 'Все', 'Один', 'Ни одного', 'Два'),
        ('Каким станет зеленый утес, если упадет в Красное море?', 'Мокрым', 'Красным', 'Не изменится', 'Фиолетовым'),
        ('Какой рукой лучше размешивать чай?', 'Ложкой', 'Правой', 'Левой', 'Любой'),
        ('Что не имеет длины, глубины, ширины, высоты, а можно измерить?', 'Время', 'Глупость', 'Море', 'Воздух'),
        ('Когда сетью можно вытянуть воду?', 'Когда вода замерзла', 'Когда нет рыбы', 'Когда уплыла золотая рыбка', 'Когда сеть порвалась'),
        ('Что больше слона и ничего не весит?', 'Тень слона', 'Воздушный шар', 'Парашют', 'Облако')]

quiz_contents = [(1, 1),
                 (2, 2),
                 (3, 3),
                 (1, 4),
                 (2, 5),
                 (3, 6),]