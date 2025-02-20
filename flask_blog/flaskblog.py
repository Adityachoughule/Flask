from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '871b93ec5a9f7e2db935b8ec367e2b0d'

posts = [
    {
        'author':'Corey Schafer',
        'title':'Blog Post 1',
        'content':'First Post content',
        'date_posted':'Feb 19, 2025'

    },
    {
        'author':'Hohn Doe',
        'title':'Blog Post 2',
        'content':'Second Post content',
        'date_posted':'Feb 20, 2025'

    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', post = posts)

@app.route("/about")
def about_page():
    return render_template('about.html', title="About")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    app.run(debug=True)

