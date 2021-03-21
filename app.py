from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    var_1 = request.form.get("var_1", type=int)
    
    operation = request.form.get("operation")
    if(operation == 'Fahrenheit'):
        result = (var_1 * 9/5) + 32
     elif(operation == 'Celcius'):
        result = (var_1 – 32) * 5/9
    else:
        result = 'INVALID CHOICE'
    entry = result
    return render_template('result.html', entry=entry)

if __name__ == "__main__":
    app.run(debug=True)

