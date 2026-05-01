from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form.get('num1', 0))
        num2 = float(request.form.get('num2', 0))
        op = request.form.get('operation')

        if op == 'add':
            result = num1 + num2
        elif op == 'sub':
            result = num1 - num2
        elif op == 'mul':
            result = num1 * num2
        elif op == 'div':
            if num2 == 0:
                result = "Cannot divide by zero"
            else:
                result = num1 / num2
        else:
            result = "Invalid operation"

    except Exception as e:
        result = "Invalid input"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)