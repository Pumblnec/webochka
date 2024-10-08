from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

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
@app.route("/lab1")
def startuem():
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
            НГТУ ФБ Лабораторная работа 1
        </header>

        <h1> web-сервер на flask</h1>
        <main>
        Flask — фреймворк для создания веб-приложений на языке программирования Python,
        использующий набор инструментов Werkzeug, а также шаблонизатор Jinja2.
        Относится к категории так называемых микрофреймворков — минималистичных каркасов веб-приложений,
        сознательно предоставляющих лишь самые базовые возможности.
        <br>
        <div>
            <h2> <a href="http://127.0.0.1:5000/menu">Меню</a></h2>
            <ul> 
                <li>
                    <a href = "http://127.0.0.1:5000/lab1/student">Информация о студенте</a>
                </li>
                 <li>
                    <a href = "http://127.0.0.1:5000/lab1/oak">Мудрый дуб(18+)</a>
                </li>
                 <li>
                    <a href = "http://127.0.0.1:5000/lab1/python">Python</a>
                </li>
                 <li>
                    <a href = "http://127.0.0.1:5000/lab1/nri">Call of Cthulhu.НРИ.</a>
                </li>
            </ul>
        </dub>
        </main>
        <br>
        <footer> 
            &copy; Варюхин Иван, ФБИ-23, 2024
        </footer>
    </body>
</html>
"""

@app.route('/lab1/oak')
def dub():
    return '''
<!doctype html>
<html>
    <head>
        <title>Варюхин Иван Алексеевич.
        Лабораторная 1</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            НГТУ ФБ Лабораторная работа 1
        </header>

        <h1> web-сервер на flask</h1>
        <main>
            <div class="dub">
            <h2> 
                Дубище
            </h2>
            <img width = 500p src = "'''+ url_for('static', filename='oak.jpeg') +'''">
            </div>
        </main>
        <br>
        <footer> 
            &copy; Варюхин Иван, ФБИ-23, 2024
        </footer>
    </body>
</html>
'''
@app.route('/lab1/student')
def student():
    return '''
<!doctype html>
<html>
    <head>
        <title>Варюхин Иван Алексеевич.
        Лабораторная 1</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            НГТУ ФБ Лабораторная работа 1
        </header>

        <h1> web-сервер на flask</h1>
        <main>
            <div class="dub">
            <h2> 
                Варюхин Иван Алексеевич
            </h2>
            <img width = 250p src = "'''+ url_for('static', filename='fb.png') +'''">
            </div>
        </main>
        <br>
        <footer> 
           
        </footer>
    </body>
</html>
'''
@app.route('/lab1/python')
def py():
    return '''
<!doctype html>
<html>
    <head>
        <title>Варюхин Иван Алексеевич.
        Лабораторная 1</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            НГТУ ФБ Лабораторная работа 1
        </header>

        <h1> web-сервер на flask</h1>
        <main>
            <div class="dub">
            <h2> 
                Python
            </h2>
            <img width = 250p src = "'''+ url_for('static', filename='pyt.png') +'''">
            <br>
            Если вы хотите начать изучать Python, следуйте нашим рекомендациям:
            Начните с основ. Осваивайте Python постепенно.
            При изучении языка программирования важно понять основы, поэтому не спешите —
            посвятите достаточно времени изучению базовых конструкций.

            Практикуйтесь. После освоения основ Python начните практиковаться,
            решая задачи и создавая свои программы. Практика поможет закрепить знания, а также научиться применять их на практике.

            Изучайте библиотеки и фреймворки. Python имеет множество библиотек и фреймворков,
            которые позволяют быстро создавать программы различной сложности.

            Станьте частью сообщества. Вы можете обращаться за помощью к более опытным коллегам,
            а также делиться своими знаниями с другими. Присоединяйтесь к форумам, чатам и группам в социальных сетях, где обсуждаются темы, связанные с Python.

            Никогда не останавливайтесь на достигнутом. Python постоянно совершенствуется,
            поэтому не забывайте следить за новыми версиями языка, изучать новые библиотеки и фреймворки, принимать участие в проектах, связанных с Python.
            </div>
        </main>
        <br>
        <footer> 
           
        </footer>
    </body>
</html>
'''
@app.route('/lab1/nri')
def nri():
    return '''
<!doctype html>
<html>
    <head>
        <title>Варюхин Иван Алексеевич.
        Лабораторная 1</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            НГТУ ФБ Лабораторная работа 1
        </header>

        <h1> web-сервер на flask</h1>
        <main>
            <div class="dub">
            <h2> 
                Call of Cthulhu
            </h2>
            <img width = 500p src = "'''+ url_for('static', filename='cthul.jpg.webp') +'''">
            <br>
            Зов Ктулху (англ. «Call of Cthulhu», иногда употребляется в виде сокращения CoC, по первым буквам английского названия) —
            настольная ролевая игра по мотивам Мифов Ктулху, которые основаны на произведениях Говарда Филлипса Лавкрафта.
            Название игры является отсылкой к одному из самых знаменитых произведений Лавкрафта — «Зов Ктулху».
            Игра разрабатывается компанией Chaosium, первое издание было выпущено в 1981 году, к настоящему времени выпущена уже седьмая редакция игры.
            </div>
        </main>
        <br>
        <footer> 
           
        </footer>
    </body>
</html>
'''