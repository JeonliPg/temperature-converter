from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    temperature = float(request.form['temperature'])
    unit = request.form['unit']
    if unit == 'C':
        result = (temperature * 9/5) + 32
        converted_unit = 'Fahrenheit'
    else:
        result = (temperature - 32) * 5/9
        converted_unit = 'Celsius'
    return render_template('index.html', result=result, converted_unit=converted_unit, original_temp=temperature, original_unit=unit)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
