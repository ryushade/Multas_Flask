from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = '123'

# Ruta para el formulario de ingreso de placas
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        placa = request.form['placa']
        return redirect(url_for('resultado', placa=placa))
    return render_template('index.html')

# Ruta que muestra los resultados de la búsqueda
@app.route('/resultado/<placa>')
def resultado(placa):
    datos_vehiculo = obtener_datos_placa(placa)
    if datos_vehiculo:
        return render_template('resultado.html', vehiculo=datos_vehiculo, placa=placa)
    else:
        flash('Vehículo no encontrado')
        return redirect(url_for('index'))

def obtener_datos_placa(placa):
    # Simulación de la búsqueda en la base de hechos
    base_hechos_placas = {
        'M4Y202': {'Modelo': 'TOYOTA YARIS - GRIS OSCURO METALICO', 'Serie': 'MR2B19FOK1052881'},
        'M4A015': {'Modelo': 'CHEVROLET SPARK LITE - BLANCO', 'Serie': 'KL1MJ6A48FC332771'},
        'AC4494': {'Modelo': 'DATSUN NL-510 - BEIGE', 'Serie': 'KD510001699'},
        'BMO882': {'Modelo': 'RAM 1500 BIG HORN - NEGRO', 'Serie': '1C6RRFFG7MN771625'},
    }
    return base_hechos_placas.get(placa.upper())

if __name__ == '__main__':
    app.run(debug=True)
