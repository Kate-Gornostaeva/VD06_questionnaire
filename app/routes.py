from flask import render_template, request, redirect, url_for
from app import app

users = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']
        age = request.form['age']
        hobby = request.form['hobby']
        if name and city and age and hobby:
            user = {'name': name, 'city': city, 'age': age, 'hobby': hobby}
            users.append(user)
            return redirect(url_for('index'))

    return render_template('questionnaire.html', users=users)