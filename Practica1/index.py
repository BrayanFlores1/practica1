from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/quienessomos')
def quienessomos():
    
    return render_template('quienessomos.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')


@app.route('/noticias')
def noticias():
    
    return render_template('noticias.html')



@app.route('/contacto')
def contacto():
    
    return render_template('contacto.html')



@app.route('/enviar', methods=['POST'])
def enviar():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    correo = request.form['correo']
    mensaje = request.form['mensaje']
    
    # Aquí puedes procesar los datos (por ejemplo, enviarlos por correo)
    print(f"Nombre: {nombre}, Apellido: {apellido}, Correo: {correo}, Mensaje: {mensaje}")

    # Redirigir a la página gracias.html
    return render_template('gracias.html')




if __name__ == '__main__':
    app.run(debug=True)

