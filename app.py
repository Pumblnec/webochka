from flask import Flask 
app = Flask(__name__)

@app.route("/")
def start():
    return """

<!doctype html>
<html>
    <head>
        <title>Варюхин Иван Алексеевич.
        Лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ ФБ Лабораторная работа 1
        </header>

        <h1> web-сервер на flask</h1>

        <footer> 
            &copy; Варюхин Иван, ФБИ-23, 2024
        </footer>
    </body>
</html>

"""

