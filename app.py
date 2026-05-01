    from flask import Flask, request
    
    app = Flask(__name__)
    
    @app.route('/')
    def home():
        return '''
        <h2>Simple Calculator</h2>
        <form action="/calculate" method="post">
            Number 1: <input type="text" name="num1"><br><br>
            Number 2: <input type="text" name="num2"><br><br>
            Operation:
            <select name="operation">
                <option value="add">Add</option>
                <option value="sub">Subtract</option>
                <option value="mul">Multiply</option>
                <option value="div">Divide</option>
            </select><br><br>
            <input type="submit" value="Calculate">
        </form>
        '''
    
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
            result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
    
        return f"<h3>Result: {result}</h3><br><a href='/'>Go Back</a>"
    
    if __name__ == "__main__":
        app.run()