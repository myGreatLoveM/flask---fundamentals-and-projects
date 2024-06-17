from flask import Flask, render_template, request, redirect, url_for, flash
from forms import RegisterForm, LoginForm

app = Flask(__name__)

app.secret_key = 'meeru'

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            print(request.form.to_dict())
            print(form.cleaned_data['email'])
            email = form.email.data
            if email == "a@b.com":
                flash('Login successful')
                return redirect(url_for('home'))
            else:
                flash('Incorrect email address')
    return render_template('login.html', title='Login', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            print(request.form.to_dict())
            flash(f'Successfully logged in {form.username.data}')
            return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)



if __name__ == '__main__':
    app.run(debug=True)

