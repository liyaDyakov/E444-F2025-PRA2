from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = StringField('What is your UofT email address?', validators=[DataRequired()])
    submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hehehe'
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        old_email = session.get('email')

        submitted_name = form.name.data
        submitted_email = form.email.data

        if 'utoronto' in submitted_email.lower():
            if old_name is not None and old_name != form.name.data:
                flash('Looks like you have changed your name!')
            name = submitted_name
            email = submitted_email
            session['name'] = name
            session['email'] = email
        elif '@' in submitted_email:
            flash('Please use your UofT email')
            form.email.data = ''  # clear the email field
            session['email'] = None
        else:
            flash('Enter a valid email address')
            form.email.data = ''  # clear the email field
            session['email'] = None

    return render_template('index.html',
        form = form, name = session.get('name'), email = session.get('email'))

# @app.route('/user/<name>')
# def user(name):
#     return render_template(
#         'user.html',
#         name=name,
#         current_time=datetime.utcnow()
#     )

# Custom error handlers
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404

# @app.errorhandler(500)
# def internal_server_error(e):
#     return render_template('500.html'), 500