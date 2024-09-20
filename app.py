from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect ('/menu', code=302)

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
            <ul> 
                <li>
                    <a href= 'http://127.0.0.1:5000/lab1'> Меню </a>
                </li>
            </ul>
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
        <main class = dub>
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
