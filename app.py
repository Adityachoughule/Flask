from flask import Flask,redirect,url_for,render_template,request


app = Flask(__name__)

@app.route('/')
def welcome():
    return "Practice Of flask from basic."

@app.route('/basic')
def basic():
    return "Practice Of flask from basic with start of python basic."

@app.route('/success/<int:score>')
def success_marks(score):
    res = "PASS"
    return render_template('result.html',result = res)

@app.route('/fail/<int:score>')
def fail_marks(score):
    # return "The person has fail and the marks is "+str(score)
    res = "FAIL"
    return render_template('result.html',result = res)

@app.route('/results/<int:marks>')
def results(marks):
    results = ""
    if marks < 50:
        results = "fail_marks"
    else:
        results = "success_marks"
    return redirect(url_for(results,score=marks))

@app.route('/jinja2/index1')
def index1():
    return render_template('index.html')

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score = 0
    if request.method == "POST":
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4
    res = ""
    if total_score >=50:
        res = "success_marks"
    else:
        res = "fail_marks"
    return redirect(url_for(res,score=total_score))

@app.errorhandler(404)
def not_found(e):
    return "Page not found!", 404



if __name__ == '__main__':
    app.run(debug=True)

