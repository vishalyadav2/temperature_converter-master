from flask import Flask, render_template, redirect, url_for, session
from flask_bs4 import Bootstrap
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField


app = Flask(__name__)
app.config['SECRET_KEY'] = '...'
bs4 = Bootstrap(app)


class ConvertForm(FlaskForm):
    fahrenheit = IntegerField('Fahrenheit:')
    submit = SubmitField('Submit')


@app.route('/')
def index():
    return '<h1>Hello World</h1>'


@app.route('/convert', methods=['GET', 'POST'])
def convert():
    """formula C = 5/9 * (F -32) Fahrenheit to Celsius"""
    table = []
    for f in range(30, 101, 2):
        c = 5 / 9 * (f -32) 
        c = round(c, 1)
        table.append((f, c))

    form = ConvertForm()

    if form.validate_on_submit():
        f = form.fahrenheit.data
        c = 5 / 9 * (f -32)
        c = round(c, 1)
        session['fa'] = f
        session['celsius'] = c
        form.fahrenheit.data = ''
        return redirect(url_for('convert'))

    return render_template('convert.html', table=table, form=form, 
        f = session.get('fa', ''), 
        c=session.get('celsius', ''))
