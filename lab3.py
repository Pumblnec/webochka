from flask import Blueprint, redirect, url_for, render_template, request, make_response
lab3 = Blueprint('lab3', __name__)

@lab3.route('/lab3/')
def labiche():
    name = request.cookies.get('name')
    name_color = request.cookies.get('name_color')
    return render_template ('lab3/lab3.html', name=name,  name_color=name_color)


@lab3.route('/lab3/cookie')
def luv():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name','Alex', max_age=5)
    resp.set_cookie('age','21')
    resp.set_cookie('name_color','DarkSlateBlue')
    return resp


@lab3.route('/lab3/del_cookie')
def delete():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp


@lab3.route('/lab3/form1')
def form():
    errors = {}
    user = request.args.get('user')
   
    if user == '':
        errors['user'] = '* заполните поле!'
    
    age = request.args.get('age')
    if age == '':
        errors['age'] = '* заполните поле!'
    sex = request.args.get('sex')
    return render_template('/lab3/form1.html', user = user, sex=sex, age=age, errors = errors)


@lab3.route('/lab3/order')
def order():
    return render_template('lab3/order.html')

@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'coffe':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10

    return render_template('lab3/pay.html', price=price)

@lab3.route('/lab3/success')
def success():
    price = request.args.get('price', 0)
    return render_template('lab3/success.html', price=price)

