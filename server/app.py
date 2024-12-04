#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<hello>')
def user(hello):
    print('hello')
    return hello

@app.route('/count/<int:parameter>')
def count_parameter(parameter):
        count_str = ""
        for i in range(parameter):
             count_str += f"{i}\n"
        return count_str

@app.route('/math/<int:num1>/<op>/<int:num2>')
def math_parameter(num1, op, num2):
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == 'div' and num2 != 0:
        result = num1 / num2
    elif op == '%':
        result = num1 % num2
    else:
        return "Invalid operation or division by zero", 400

    return str(result)
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
