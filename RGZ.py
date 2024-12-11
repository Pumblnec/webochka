from flask import Blueprint, redirect, url_for, render_template, render_template_string, abort, request, make_response, session,  current_app, Flask, flash
from functools import wraps
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from os import path

RGZ = Blueprint('RGZ', __name__)

ADMIN_USER = 'Timur'

def db_connect():

    if current_app.config['DB_TYPE'] == 'postgres':
        conn = psycopg2.connect(dbname="WEB", 
        user="postgres", 
        password="Super0925!", 
        host="127.0.0.1"
        )
        cur = conn.cursor(cursor_factory = RealDictCursor)

    else:
        dir_path = path.dirname(path.realpath(__file__))
        db_path = path.join(dir_path, "database.db")
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

    return conn, cur

def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()

@RGZ.route('/RGZ/', methods=['GET'])
def books():
    # Проверка, авторизован ли пользователь
    if 'login' not in session:
        return redirect(url_for('RGZ.login'))

    # Получение параметров сортировки и поиска
    author = request.args.get('author', '')  # Получаем выбранного автора
    genre = request.args.get('genre', '')  # Получаем выбранный жанр
    pages_from = request.args.get('pages_from', '')  # Получаем минимальное количество страниц
    pages_to = request.args.get('pages_to', '')  # Получаем максимальное количество страниц
    page = int(request.args.get('page', 1))  # Текущая страница
    per_page = 20  # Количество книг на странице
    offset = (page - 1) * per_page  # Смещение для SQL-запроса

    conn, cur = db_connect()

    # Получение уникальных авторов и жанров для выпадающих списков
    cur.execute("SELECT DISTINCT author FROM books;")
    authors = [row['author'] for row in cur.fetchall()]

    cur.execute("SELECT DISTINCT genre FROM books;")
    genres = [row['genre'] for row in cur.fetchall()]

    # Подготовка условий для SQL-запроса
    conditions = []
    params = []

    if author:
        conditions.append("author = %s")
        params.append(author)

    if genre:
        conditions.append("genre = %s")
        params.append(genre)

    if pages_from:
        conditions.append("page_count >= %s")
        params.append(int(pages_from))  # Преобразуем в int

    if pages_to:
        conditions.append("page_count <= %s")
        params.append(int(pages_to))  # Преобразуем в int

    # Формируем SQL-запрос
    query = """
        SELECT cover_image, title, author, page_count AS pages, publisher, genre 
        FROM books 
        WHERE TRUE
    """
    
    if conditions:
        query += " AND " + " AND ".join(conditions)

    query += " ORDER BY title LIMIT %s OFFSET %s;"
    params.append(per_page)
    params.append(offset)

    cur.execute(query, params)
    books = cur.fetchall()

    # Получение общего количества книг для пагинации
    total_query = """
        SELECT COUNT(*) 
        FROM books 
        WHERE TRUE
    """
    
    total_conditions = []
    total_params = []

    if author:
        total_conditions.append("author = %s")
        total_params.append(author)

    if genre:
        total_conditions.append("genre = %s")
        total_params.append(genre)

    if pages_from:
        total_conditions.append("page_count >= %s")
        total_params.append(int(pages_from))

    if pages_to:
        total_conditions.append("page_count <= %s")
        total_params.append(int(pages_to))

    if total_conditions:
        total_query += " AND " + " AND ".join(total_conditions)

    cur.execute(total_query, total_params)
    total_books = cur.fetchone()['count']
    total_pages = (total_books + per_page - 1) // per_page  # Общее количество страниц

    db_close(conn, cur)

    is_admin = session.get('login') == ADMIN_USER

    return render_template('RGZ/RGZ.html', books=books, page=page, total_pages=total_pages, authors=authors, genres=genres, login=session.get('login'), is_admin=is_admin)

@RGZ.route('/RGZ/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('RGZ/register.html')

    login = request.form.get('login')
    password = request.form.get('password')

    if not (login and password):
        return render_template('RGZ/register.html', error='Заполните все поля')

    conn, cur = db_connect()


    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT login FROM users WHERE login=%s;", (login,))
    else:
        cur.execute("SELECT login FROM users WHERE login=?;", (login,))

    if cur.fetchone():
        db_close(conn, cur)
        return render_template('RGZ/register.html', error="Такой пользователь уже существует")

    password_hash = generate_password_hash(password)


    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("INSERT INTO users (login, password) VALUES (%s, %s);", (login, password_hash))
    else:
        cur.execute("INSERT INTO users (login, password) VALUES (?, ?);", (login, password_hash))

    db_close(conn, cur)
    return render_template('RGZ/success.html', login=login)

@RGZ.route('/RGZ/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('RGZ/login.html')

    login = request.form.get('login')
    password = request.form.get('password')

    if not (login and password):
        flash("Заполните поля", "error")
        return render_template('RGZ/login.html')

    conn, cur = db_connect()

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT * FROM users WHERE login=%s;", (login,))
    else:
        cur.execute("SELECT * FROM users WHERE login=?;", (login,))
    user = cur.fetchone()

    if not user or not check_password_hash(user['password'], password):
        db_close(conn, cur)
        flash('Логин и/или пароль неверны', "error")
        return render_template('RGZ/login.html')

    # Установка сессии
    session['login'] = user['login']  # Сохраняем логин в сессии
    session['role'] = 'admin' if user['login'] == ADMIN_USER else 'user'  # Устанавливаем роль

    flash('Вы успешно вошли в систему!', "success")
    db_close(conn, cur)

    if session['role'] == 'admin':
        return redirect(url_for('RGZ.manage_books'))  # Перенаправление на админскую страницу
    else:
        return redirect(url_for('RGZ.books'))

@RGZ.route('/RGZ/logout')
def logout():
    session.pop('login', None)
    return redirect(url_for('RGZ.login'))

@RGZ.route('/admin/manage_books', methods=['GET', 'POST'])
def manage_books():
    if 'login' not in session or session['login'] != ADMIN_USER:
        return redirect(url_for('RGZ.login'))

    conn, cur = db_connect()

    if request.method == 'POST':
        # Добавление новой книги
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        page_count = request.form['page_count']
        publisher = request.form['publisher']
        cover_image = request.form['cover_image']

        cur.execute("INSERT INTO books (title, author, genre, page_count, publisher, cover_image) VALUES (%s, %s, %s, %s, %s, %s)",
                    (title, author, genre, page_count, publisher, cover_image))
        conn.commit()
        flash('Книга добавлена успешно!')

    # Получение параметров фильтрации
    author = request.args.get('author', '')
    genre = request.args.get('genre', '')
    page_count = request.args.get('page_count', '')

    # Формирование условия для SQL-запроса
    conditions = []
    params = []
    if author:
        conditions.append("author LIKE %s")
        params.append(f"%{author}%")

    if genre:
        conditions.append("genre LIKE %s")
        params.append(f"%{genre}%")

    if page_count:
        conditions.append("page_count = %s")
        params.append(page_count)

    # Получение всех книг для отображения с учетом фильтрации
    if conditions:
        query = "SELECT * FROM books WHERE " + " AND ".join(conditions)
        cur.execute(query, params)
    else:
        cur.execute("SELECT * FROM books")

    books = cur.fetchall()

    db_close(conn, cur)

    return render_template('RGZ/admin/manage_books.html', books=books, author=author, genre=genre, page_count=page_count)

@RGZ.route('/admin/edit_book/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    if 'login' not in session or session['login'] != ADMIN_USER:
        return redirect(url_for('login'))

    conn, cur = db_connect()

    if request.method == 'POST':
        # Обновление книги
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        page_count = request.form['page_count']
        publisher = request.form['publisher']
        cover_image = request.form['cover_image']

        cur.execute("UPDATE books SET title=%s, author=%s, genre=%s, page_count=%s, publisher=%s, cover_image=%s WHERE id=%s",
                    (title, author, genre, page_count, publisher, cover_image, book_id))
        conn.commit()
        flash('Книга обновлена успешно!')
        return redirect(url_for('RGZ.manage_books'))

    # Получение данных книги для редактирования
    cur.execute("SELECT * FROM books WHERE id=%s;", (book_id,))
    book = cur.fetchone()

    db_close(conn, cur)

    return render_template('RGZ/admin/edit_book.html', book=book)

@RGZ.route('/admin/delete_book/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    if 'login' not in session or session['login'] != ADMIN_USER:
        return redirect(url_for('login'))

    conn, cur = db_connect()
    cur.execute("DELETE FROM books WHERE id=%s;", (book_id,))
    conn.commit()
    db_close(conn, cur)

    flash('Книга удалена успешно!')
    return redirect(url_for('RGZ.manage_books'))