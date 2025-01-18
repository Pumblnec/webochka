from flask import Blueprint, redirect, url_for, render_template, request, make_response, session
lab4 = Blueprint('lab4', __name__)

@lab4.route('/lab4/')
def lab():
    return render_template ('lab4/lab4.html')


@lab4.route('/lab4/div-form')
def div_form():
    return render_template ('lab4/div-form.html')


@lab4.route('/lab4/div', methods = ['POST'])
def div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/div.html', error='Оба поля должны быть заполнены!')
    if x2 == '0':
        return render_template('lab4/div.html', error='на ноль делить нельзя!') 
    x1 = int(x1)
    x2 = int(x2)
    result = x1/x2
    return render_template('lab4/div.html', x1=x1, x2=x2, result=result)




@lab4.route('/lab4/sum-form')
def sum_form():
    return render_template('lab4/sum-form.html')

@lab4.route('/lab4/sum', methods = ['POST'])
def sum():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '':
        x1 = '0'
    if x2 == '':
        x2 = '0'
    x1 = int(x1)
    x2 = int(x2)
    result = x1 + x2
    return render_template('lab4/sum.html', x1=x1, x2=x2, result=result)



@lab4.route('/lab4/mul-form')
def mul_form():
    return render_template('lab4/mul-form.html')

@lab4.route('/lab4/mul', methods = ['POST'])
def mul():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '':
        x1 = '1'
    if x2 == '':
        x2 = '1'
    x1 = int(x1)
    x2 = int(x2)
    result = x1 * x2
    return render_template('lab4/mul.html', x1=x1, x2=x2, result=result)



@lab4.route('/lab4/ex-form')
def ex_form():
    return render_template('lab4/ex-form.html')

@lab4.route('/lab4/ex', methods = ['POST'])
def ex():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/ex.html', error='Оба поля должны быть заполнены!')
    x1 = int(x1)
    x2 = int(x2)
    result = x1 - x2
    return render_template('lab4/ex.html', x1=x1, x2=x2, result=result)



@lab4.route('/lab4/vz-form')
def vz_form():
    return render_template('lab4/vz-form.html')

@lab4.route('/lab4/vz', methods = ['POST'])
def vozv():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/vz.html', error='Оба поля должны быть заполнены!')
    if x1 == '0' and x2 == '0':
        return render_template('lab4/vz.html', error='не должно быть 0!')
    
    x1 = int(x1)
    x2 = int(x2)
    result = x1 ** x2
    return render_template('lab4/vz.html', x1=x1, x2=x2, result=result)


tree_count = 0

@lab4.route('/lab4/tree', methods = ['GET', 'POST'])
def tree():
    global tree_count
    if request.method == 'GET':
        return render_template('lab4/tree.html', tree_count=tree_count)
    operation = request.form.get('operation')

    if operation == 'cut':
        if tree_count > 0:
            tree_count -= 1
    elif operation == 'plant':
        if tree_count < 10:
            tree_count += 1
    
    return redirect('/lab4/tree')


users = [
    {'login': 'alex', 'password': '123', 'name': 'Алексей Алексеич', 'gender': 'мужчина'},
    {'login': 'dimasik', 'password': '555', 'name': 'Дим Димыч', 'gender': 'мужчина'},
    {'login': 'Vanya228', 'password': '228', 'name': 'Ваня Крут', 'gender': 'мужчина'},
    {'login': 'Artemi', 'password': 'ara322', 'name': 'Артемий Артемович', 'gender': 'мужчина'},
]


@lab4.route('/lab4/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'login' in session:
            authorized = True
            login = session['login']
            for user in users:
                if user['login'] == login:
                    name = user['name'] 
                    return render_template('/lab4/login.html', authorized=authorized, login=login, name=name)
        else:
            authorized = False
            login = ''
        return render_template('/lab4/login.html', authorized=authorized, login=login)
    

    login = request.form.get('login')
    password = request.form.get('password')

    if not login:
        error = 'Не введён логин'
        return render_template('/lab4/login.html', error=error, authorized=False, login=login)
    if not password:
        error = 'Не введён пароль'
        return render_template('/lab4/login.html', error=error, authorized=False, login=login)

    for user in users:
        if login == user['login'] and password == user['password']:
            session['login'] = login
            return redirect('/lab4/login')
    
    error = 'Неверный логин и/или пароль'
    return render_template('/lab4/login.html', error=error, authorized=False, login=login)


@lab4.route('/lab4/fridge', methods=['GET', 'POST'])
def fridge():
    error = None
    temperature = None
    snowflakes = None

    if request.method == "POST":
        temperature = float(request.form["temperature"])
        if temperature is None:
            error = "Ошибка: не задана температура"
        elif temperature < -12:
            error = "Не удалось установить температуру — слишком низкое значение"
        elif temperature > -1:
            error = "Не удалось установить температуру — слишком высокое значение"
        else:
            if -12 <= temperature <= -9:
                snowflakes = 3
            elif -8 <= temperature <= -5:
                snowflakes = 2
            elif -4 <= temperature <= -1:
                snowflakes = 1

    return render_template('/lab4/fridge.html', error=error, temperature=temperature, snowflakes=snowflakes)


prices = {
    "ячмень": 12345,
    "овёс": 8522,
    "пшеница": 8722,
    "рожь": 14111
}

@lab4.route('/lab4/order_grain', methods=['GET', 'POST'])
def order_grain():
    if request.method == 'POST':
        grain_type = request.form.get('grain_type')
        weight = request.form.get('weight')

        if not weight:
            return render_template('/lab4/order_grain.html', error="Ошибка! Не указан вес заказа.", grain_types=prices.keys())
        try:
            weight = float(weight)
        except ValueError:
            return render_template('/lab4/order_grain.html', error="Ошибка! Некорректный формат веса.", grain_types=prices.keys())

        if weight <= 0:
            return render_template('/lab4/order_grain.html', error="Ошибка! Вес заказа должен быть больше 0.", grain_types=prices.keys())

        price_per_ton = prices.get(grain_type, 0)
        total_cost = price_per_ton * weight

        discount = 0
        if weight > 50:
            discount = total_cost * 0.1
            total_cost -= discount

        if weight > 500:
            return render_template('/lab4/order_grain.html', error="К сожалению, такого объёма зерна сейчас нет в наличии.", grain_types=prices.keys())

        return render_template('/lab4/order_grain.html', grain_type=grain_type, weight=weight, total_cost=total_cost, discount=discount, grain_types=prices.keys())
 
    return render_template('/lab4/order_grain.html', grain_types=prices.keys())