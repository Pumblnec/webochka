from flask import Flask, redirect, url_for, render_template
from lab1 import lab1

app = Flask(__name__)
app.register_blueprint(lab1)

@app.route("/")
@app.route("/index")
def start():
    return redirect ('/menu', code=302)

@app.route("/lab2/example")
def example():
    namee = 'Варюхин Иван'
    course = '3'
    group = 'ФБИ-23'
    labnum = '2'
    fruits = [
        {'name': 'Яблоки', 'price': 180},
        {'name': 'Киви', 'price': 210},
        {'name': 'Апельсины', 'price': 150},
        {'name': 'Капуста?', 'price': 80},
        {'name': 'Манго', 'price': 270}
        
    ]
    books = [
        {'name': 'Зов Ктулху. Тень над Исмунтом', 'author': 'Лавкрафт Г.', 'genre': 'Ужасы, мистика', 'pages': 336},
        {'name': 'Ночной дозор', 'author': 'Лукьяненко С.', 'genre': 'Роман, фантастика, ужасы', 'pages': 410},
        {'name': 'Легкий способ бросить курить', 'author': 'Карр А.', 'genre': 'Методики, психология', 'pages': 224},
        {'name': 'Билли Саммерс', 'author': 'Кинг С.', 'genre': 'Детектив, триллер', 'pages': 550},
        {'name': 'Зеленая миля', 'author': 'Кинг С.', 'genre': 'Психологический триллер', 'pages': 384},
        {'name': 'ТЕКСТ', 'author': 'Глуховский Д.', 'genre': 'Криминальная драма, психологический триллер', 'pages': 330},
        {'name': 'Снеговик', 'author': 'Несбё Ю.', 'genre': 'Криминальная драма, детектив', 'pages': 460},
        {'name': 'Нетопырь', 'author': 'Несбё Ю.', 'genre': 'Криминальная драма, детектив', 'pages': 330},
        {'name': 'Ядовитый воздух свободы', 'author': 'Блейк А.', 'genre': 'Психологические детективы', 'pages': 473},
        {'name': 'Я прихожу после смерти. История уборщика мест преступлений', 'author': 'Кундт Т., Багджи Т.', 'genre': 'Трукрайм', 'pages': 170}
    ]
    return render_template ('example.html', namee=namee, course=course, group=group, labnum=labnum, fruits = fruits, books=books)

@app.route("/lab2/")
def lab2():

    return  render_template ('lab2.html')

@app.route("/lab2/vector")
def vector():
    return render_template ('vector.html')

@app.route("/menu")
def mn():
    return """

<!doctype html>
<html>
    <head>
        <title>Варюхин Иван Алексеевич.
        Лабораторная 1</title>
        <link rel="stylesheet" href='""" + url_for('static', filename='lab1.css') + """'>
    </head>
    <body>
        <header>
            НГТУ ФБ WEB-программирование, часть 2. Список лабораторных
        </header>

        
        <h1> web-сервер на flask</h1>
        <main> 

        <h2>Меню</h2>

        <ol>

            <li><a href= 'http://127.0.0.1:5000/lab1'> Лабораторная 1 </a></li>

            <li><a href= 'http://127.0.0.1:5000/lab2'> Лабораторная 2 </a></li>

        </ol>

        </main>


        <footer> 
            &copy; Варюхин Иван, ФБИ-23, 3 курс, 2024
        </footer>
    </body>
</html>

"""