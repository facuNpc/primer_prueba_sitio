import traceback
from datetime import datetime
from flask import Flask, request, jsonify, render_template, Response, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

#Crear el server Flask
app = Flask(__name__)

#Renderizar Index.html 
@app.route("/")
def index():
    try:
        return render_template('index.html')
    except:
        return jsonify({'trace': traceback.format_exc()})

#Funcion que recibe la categoria
@app.route("/agregar_categoria", method='POST')
def agregar_categoria():
    try:
        if request.method == "POST":
            categoria = str(request.form.get('categoria')).lower()
        return redirect(url_for('template_gasto', categoria=categoria))
    except:
        Exception

#Template de productos y gastos
@app.route("/template_gasto", method="POST")
def template_gasto(categoria):
    try:
        return render_template("formulario_gastos", categoria = categoria)
    except:
        pass

#Funcion que recibe los gastos
@app.route("/agregar_gasto", method="POST")
def agregar_gasto(categoria):
    try:
        if request.method == "POST":
            pass
    except:
        return jsonify({'trace': traceback.format_exc()})
    
if __name__ == '__main__':
    #Lanzar server
    app.run(host="127.0.0.1", port=5000, debug= True)