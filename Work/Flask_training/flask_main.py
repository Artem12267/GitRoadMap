
import re
import bcrypt
from DataBase import main_db
import random
from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_login import LoginManager, UserMixin, login_required ,logout_user ,login_user


# def hashed_password(plain_text_password):
#     #Мы добавляем "соль" к нашему пароль, чтобы сделать его декодирование невозможным
#     return bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt()) 

# def check_password(plain_text_password, hashed_password):
#     return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_password)

db_user = main_db.flask_user("DataBase\DataBaseFlask.db")

app = Flask(__name__)

# all_orders = []

app.config.update(
    SECRET_KEY='WOW SUCH SECRET'
)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


class User(UserMixin):
    def __init__(self, id):
        self.id = id


@login_manager.user_loader
def load_user(login):
    return User(login)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        for key in request.form:
            if request.form[key] == '':
                return render_template('registration.html', message='Все поля должны быть заполнены!')

        row = db_user.CheckRegistr(request.form['login'])
        if row:
            return render_template('registration.html', message='Такой пользователь уже существует!')
            
        if request.form['password'] != request.form['password_check']:
            return render_template('registration.html', message='Пороли не совпадают')
        data = dict(request.form)
        data.pop('password_check')
        login = data['login']
        password = data['password']
        email = data['email']
        phone_number = data['phone_number']
        db_user.AddUser(login, password, email, phone_number)
        return render_template('registration.html', message='Регистрация прошла успешно')
    return render_template('registration.html')


@app.route('/')
@login_required
def main_products():
    return render_template('main_products.html')



@app.route('/sneakers_main', methods=['GET', 'POST'])
def sneakers_main():
#     if request.method == 'POST':
#         item_id = request.form['item_id']
#         row = db.cart.get('item_id', item_id)
#         if not row:
#             data = {'item_id':item_id, 'amount':1}
#             db.cart.put(data)
#         else:
#             data = {'item_id':item_id, 'amount':row.amount+1}
#             db.cart.delete('item_id', item_id)
#             db.cart.put(data)

#     data = db.items.get_all()
#     for row in data:
#         res = db.cart.get('item_id', row.id)
#         if res:
#             row.amount = res.amount
#         else:
#             row.amount = 0
    return render_template('sneakers_main.html')#, data=data)

@app.route('/men', methods=['GET', 'POST'])
def men():
    DictItems = {
        "id" : [],
        "name" : [],
        "description" : [],
        "price" : [],
        "img" : []
        }

    DataFrom_Items = db_user.GettingData_Items()

    for data in DataFrom_Items:
        passing = []
        for item in data:
            item = str(item)
            passing.append(item)

            if len(passing) == 5:
                DictItems["id"].append(passing[0])
                DictItems["name"].append(passing[1])
                DictItems["description"].append(passing[2])
                DictItems["price"].append(passing[3])
                DictItems["img"].append(passing[4])
        
    return render_template('men.html')


# @app.route('/cart')
# @login_required
# def cart():
#     return render_template('cart.html')


# @app.route('/contacts')
# @login_required
# def contacts():
#     return render_template('contacts.html')


@app.route('/about_comp')
@login_required
def about_comp():
    return render_template('about_comp.html')


# @app.route('/product1')
# @login_required
# def product1():
#     end_date = datetime.now() + timedelta(days=7)
#     end_date = end_date.strftime('%d.%m.%Y')
#     return render_template('product1.html',
#                            action_name='Весенние скидки!',
#                            end_date=end_date,
#                            lucky_num=randint(1, 5))


# @app.route('/product2')
# @login_required
# def product2():
#     brands = ['Colla', 'Pepppssi', 'Orio', 'Macdak']
#     return render_template('product2.html', brands=brands)


# @app.route('/order', methods=['GET', 'POST'])
# @login_required
# def order():
#     if request.method == 'POST':
#         for key in request.form:
#             if request.form[key] == '':
#                 return render_template('order.html', error='Не все поля заполнены!')
#             if key == 'email':
#                 if not re.match('\w+@\w+\.(ru|com)', request.form[key]):
#                     return render_template('order.html', error='Неправильный формат почты')
#             if key == 'phone_number':
#                 if not re.match('\+7\d{9}', request.form[key]):
#                     return render_template('order.html', error='Неправильный формат номера телефона')
#             else:
#                 all_orders.append(request.form)
#     return render_template('order.html')


# @app.route('/api/orders')
# def api_orders():
#     return jsonify(all_orders)


# @app.route('/order_list')
# @login_required
# def order_list():
#     return render_template('order_list.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        row = db_user.CheckRegistr(request.form['login'])
        if not row:
            return render_template('login.html', error='Неправильный логин или пароль')

        if request.form['password'] == db_user.CheckRegistr(request.form['login'], verification=True):
            user = User(login)  # Создаем пользователя
            login_user(user)  # Логинем пользователя
            return redirect(url_for('main_products'))
        else:
            return render_template('login.html', error='Неправильный логин или пароль')
    return render_template('login.html')


# @app.route("/logout")
# @login_required
# def logout():
#     logout_user()
#     return 'Пока'


# @app.route('/lootbox')
# @login_required
# def lootbox():
#     num = randint(1, 100)
#     if num < 50:
#         chance = 50
#     elif 50 < num < 95:
#         chance = 45
#     elif 95 < num < 99:
#         chance = 4
#     else:
#         chance = 1
#     return render_template('lootbox.html', chance=chance)


if __name__ == "__main__":
    app.run()
