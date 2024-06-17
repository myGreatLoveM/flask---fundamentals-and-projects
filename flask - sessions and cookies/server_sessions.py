from flask import Flask, render_template, redirect, url_for, flash, session, request
from flask_session import Session
from forms import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'meeru'
app.config['SESSION_TYPE'] = 'filesystem'

Session(app)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if "user_name" in session:
        return redirect(url_for('home'))
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            print(form.username)
            session["user_name"] = form.username.data
            flash(f'Successfully logged in as {session["user_name"].title()}')
            next_url = request.args.get('next')
            return redirect(next_url or url_for('home'))
        else:
            flash(f'Invalid username')
    return render_template('login.html', title='Login', form=form)

@app.route('/about', methods=['GET'])
def about():
    if 'user_name' not in session:
        flash('Login Required!!!')
        return redirect(url_for('login', next=request.url))
    return render_template('about.html', title='About')

@app.route('/contact', methods=['GET'])
def contact():
    if 'user_name' not in session:
        flash('Login Required!!!')
        return redirect(url_for('login', next=request.url))
    return render_template('contact.html', title='Contact')


