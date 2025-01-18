from flask import Flask, redirect, url_for, render_template
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4

app = Flask(__name__)
app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)


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

        <h2>Меню</h2>

        <ol>

            <li><a href= '/lab1'> Лабораторная 1 </a></li>

            <li><a href= '/lab2'> Лабораторная 2 </a></li>

            <li><a href= '/lab3'> Лабораторная 3 </a></li>

            <li><a href= '/lab4'> Лабораторная 4 </a></li>

        </ol>

        </main>


        <footer> 
            &copy; Варюхин Иван, ФБИ-23, 3 курс, 2025
        </footer>
    </body>
</html>

"""