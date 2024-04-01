from flask import Flask, render_template, request

app = Flask(__name__)

# Список блюд
menu_items = [
    {'id': 1, 'name': 'Паста с томатным соусом'},
    {'id': 2, 'name': 'Салат Цезарь'},
    {'id': 3, 'name': 'Стейк из говядины'},
    {'id': 4, 'name': 'Рыбный суп'},
    {'id': 5, 'name': 'Фруктовый салат'}
]

# Главная страница с формой выбора блюд
@app.route('/')
def index():
    return render_template('index.html', menu_items=menu_items)

# Обработка формы
@app.route('/choose', methods=['POST'])
def choose():
    selected_items = []
    for item in menu_items:
        item_id = str(item['id'])
        if request.form.get(item_id):
            selected_items.append(item['name'])
    return render_template('selected.html', selected_items=selected_items)

if __name__ == '__main__':
    app.run(debug=True)
