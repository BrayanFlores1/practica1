from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Lista de inscritos simulada
inscritos = [
    {'id': 1, 'fecha': '2024-10-24', 'nombre': 'Sergio', 'apellidos': 'Pérez', 'turno': 'Mañana', 'seminarios': 'inteligencia artificial'},
    {'id': 2, 'fecha': '2024-10-25', 'nombre': 'Alanoca', 'apellidos': 'Gómez', 'turno': 'Tarde', 'seminarios': 'machine learning'}
]
# Página de inicio que redirige a la lista de inscritos
@app.route('/')
def index():
    return redirect(url_for('listainscritos'))
# Página que muestra la lista de inscritos
@app.route('/listainscritos')
def listainscritos():
    return render_template('listainscritos.html', inscritos=inscritos)

@app.route('/registros', methods=['GET', 'POST'])
def registros():
    if request.method == 'POST':
        # Obtener datos del formulario
        nuevo_id = len(inscritos) + 1
        fecha = request.form['fecha']
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        turno = request.form['turno']
        
        # Seminarios seleccionados (lista)
        seminarios = ', '.join(request.form.getlist('seminarios'))  # Concatenar la lista de seminarios seleccionados
        
        # Agregar nuevo inscrito a la lista
        inscritos.append({
            'id': nuevo_id,
            'fecha': fecha,
            'nombre': nombre,
            'apellidos': apellidos,
            'turno': turno,
            'seminarios': seminarios
        })
        
        return redirect(url_for('listainscritos'))
    
    return render_template('registros.html')


# Página para editar un inscrito existente
@app.route('/editar_inscrito/<int:id>', methods=['GET', 'POST'])
def editar_inscrito(id):
    inscrito = next((i for i in inscritos if i['id'] == id), None)
    
    if request.method == 'POST':
        # Actualizar los datos del inscrito
        inscrito['fecha'] = request.form['fecha']
        inscrito['nombre'] = request.form['nombre']
        inscrito['apellidos'] = request.form['apellidos']
        inscrito['turno'] = request.form['turno']
        inscrito['seminarios'] = request.form['seminarios']
        
        return redirect(url_for('listainscritos'))
    
    return render_template('editar.html', inscrito=inscrito)

# Eliminar un inscrito
@app.route('/eliminar_inscrito/<int:id>')
def eliminar_inscrito(id):
    global inscritos
    inscritos = [i for i in inscritos if i['id'] != id]
    return redirect(url_for('listainscritos'))

if __name__ == '__main__':
    app.run(debug=True)
