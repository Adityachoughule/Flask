from flask import Flask, render_template, url_for
app = Flask(__name__)

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



if __name__ == '__main__':
    app.run(debug=True)

