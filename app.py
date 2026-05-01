from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    op = request.form['operation']

    if op == 'add':
        result = num1 + num2
    elif op == 'sub':
        result = num1 - num2
    elif op == 'mul':
        result = num1 * num2
    elif op == 'div':
        result = num1 / num2
    else:
        result = "Error"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)