from flask import Flask,render_template,request
from empdata import Employee

app=Flask(__name__)

getemployee=Employee()

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/employee')
def emp():
    return render_template('employee.html',employeelist=getemployee)

if(__name__=='__main__'):
    app.run(debug=True) 