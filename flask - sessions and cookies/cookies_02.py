from flask import Flask, render_template, redirect, url_for, flash, request, make_response
from forms import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'meeru'


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    user_name = request.cookies.get('user_name')
    if user_name:
        return redirect(url_for('home'))
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user_name = form.username.data
            resp = make_response('')
            resp.set_cookie('user_name', user_name)
            flash(f'Successfully logged in as {user_name.title()}')
            next_url = request.args.get('next') or url_for('home')
            resp.headers["Location"] = next_url
            resp.status_code = 302
            return resp
        else:
            flash(f'Invalid username')
    return render_template('login.html', title='Login', form=form)

@app.route('/about', methods=['GET'])
def about():
    user_name = request.cookies.get('user_name')
    if user_name is None:
        flash('Login Required!!!')
        return redirect(url_for('login', next=request.url))
    return render_template('about.html', title='About')

@app.route('/contact', methods=['GET'])
def contact():
    user_name = request.cookies.get('user_name')
    if user_name is None:
        flash('Login Required!!!')
        return redirect(url_for('login', next=request.url))
    return render_template('contact.html', title='Contact')


if __name__ == '__main__':
    app.run(debug=True)