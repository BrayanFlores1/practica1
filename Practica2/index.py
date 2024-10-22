from flask import Flask, render_template ,request

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/inscribir', methods=['POST'])
def inscribir():
    nombre = request.form['nombre']
    apellidos = request.form['apellidos']
    curso = request.form['curso']
    paralelo = request.form['paralelo']
    
    # Enviamos los datos a la página estudiantes.html
    return render_template('estudiantes.html', nombre=nombre, apellidos=apellidos, curso=curso, paralelo=paralelo)


@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html')  # Muestra el formulario de usuarios

@app.route('/enviar_usuario', methods=['POST'])
def enviar_usuario():
    # Recibimos los datos del formulario de usuarios
    nombre = request.form['nombre']  # Asegúrate de que esta línea esté presente
    apellido = request.form['apellido']
    correo = request.form['correo']
    contraseña = request.form['contraseña']
    
    # Enviamos los datos a la página grasias.html
    return render_template('gracias.html', nombre=nombre, apellido=apellido, correo=correo, contraseña=contraseña)


@app.route('/libros')
def libros():
    return render_template('libros.html')
@app.route('/enviar', methods=['POST'])
def enviar1():
    # Recibimos los datos del formulario
    titulo = request.form['titulo']
    autor = request.form['autor']
    resumen = request.form['resumen']
    medio = request.form.get('medio')

    # Los datos pueden ser enviados a la página libros1.html
    return render_template('libros1.html', titulo=titulo, autor=autor, resumen=resumen, medio=medio)

# Ruta para el formulario de productos
@app.route('/productos')
def productos():
    return render_template('productos.html')  # Muestra el formulario de productos

# Ruta para procesar el formulario de productos
@app.route('/enviar_producto', methods=['POST'])
def enviar_producto():
    producto = request.form['producto']
    categoria = request.form['categoria']
    existencia = request.form['existencia']
    precio = request.form['precio']
    
    # Enviamos los datos a la página productos1.html
    return render_template('productos1.html', producto=producto, categoria=categoria, existencia=existencia, precio=precio)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
