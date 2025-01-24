from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        temperature = float(request.form['temperature'])
        
        # Conversión de Temperatura
        result_fahrenheit = (temperature * 9/5) + 32
        result_kelvin = temperature + 273.15
        result_rankine = (temperature + 273.15) * 9/5

        return render_template('index.html', 
                               original_temp=temperature, 
                               result_fahrenheit=result_fahrenheit, 
                               result_kelvin=result_kelvin, 
                               result_rankine=result_rankine)
    except ValueError:
        return "Por favor ingresa un valor válido para la temperatura."

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        expression = request.form['expression']
        result = eval(expression)
        return render_template('index.html', calculation_result=result, expression=expression)
    except Exception as e:
        return render_template('index.html', calculation_result="Error en la operación", expression=expression)

if __name__ == '__main__':
    app.run(debug=True)
