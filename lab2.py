from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2', __name__)


@lab2.route("/lab2/example")
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

@lab2.route("/lab2/")
def lab2():

    return  render_template ('lab2.html')

@lab2.route("/lab2/vector")
def vector():
    return render_template ('vector.html')
