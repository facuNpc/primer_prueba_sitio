import traceback
from datetime import datetime
from flask import Flask, request, jsonify, render_template, Response, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

#Crear el server Flask
app = Flask(__name__)

# Base de datos
from flask_sqlalchemy import SQLAlchemy

# Indicar al sistema (app) de donde leer la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///gastos.db"

# Asociar controlador de la base de datos con la aplicacion
db = SQLAlchemy()
db.init_app(app)

# ------------ Tablas de la DB ----------------- #
class Gastos(db.Model):
    __tablename__ = "Gastos"
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime)
    producto = db.Column(db.String)
    categoria = db.Column(db.String)
    gasto = db.Column(db.Integer)
    
    def __repr__(self):
        return f"Producto {self.producto} valor: {self.gasto}"

# ------------ Rutas o endpoints ----------------- #
#Renderizar Index.html 
@app.route("/")
def index():
    try:
        return render_template('index.html')
    except:
        return jsonify({'trace': traceback.format_exc()})
    
    
#Funcion que recibe los gastos
@app.route("/gastos", methods=['GET', 'POST'])
def gastos():
    if request.method == 'GET':
        # Si entré por "GET" es porque acabo de cargar la página
        try:
            return render_template("formulario_gastos", categoria = categoria)
        except:
            return jsonify({'trace': traceback.format_exc()})
        
    if request.method == "POST":
        try:
            producto = str(request.form.get('producto')).lower()
            gasto = str(request.form.get('gasto')).lower()
            categoria = str(request.form.get('categoria')).lower()

            if(producto is None or gasto is None or gasto.isdigit() is False):
                # Datos ingresados incorrectos
                return Response(status=400)
            
            # Obtener la fecha y hora actual
            fecha = datetime.now()

            # Crear un nuevo registro de gastos
            gastos = Gastos(fecha=fecha, producto=producto, gasto=int(gasto), categoria=categoria)

            # Agregar el registro de gastos a la DB
            db.session.add(gastos)
            db.session.commit()

            #Redirigir a template que muestre las tablas
            return redirect(url_for('datos'))
        except:
            return jsonify({'trace': traceback.format_exc()})


def datos():
    try:
        # Obtener todos los gastos:
        query = db.session.query(Gastos)     

        # Ordenamos por fecha para obtener primero el ultimo registro
        query = query.order_by(Gastos.fecha.desc())     

        # Obtener el reporte
        data = []

        for paciente in query:
            json_result = {}
            json_result['fecha'] = paciente.fecha.strftime("%Y-%m-%d %H:%M:%S.%f")
            json_result['nombre'] = paciente.nombre
            json_result['pulso'] = paciente.valor
            data.append(json_result)

        return render_template('index.html', data=data)
    except:
        return jsonify({'trace': traceback.format_exc()})

# Crear la base de datos
with app.app_context():

    db.create_all()
    print("Base de datos generada")


if __name__ == '__main__':
    #Lanzar server
    app.run(host="127.0.0.1", port=5000, debug= True)