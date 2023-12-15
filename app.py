import traceback
from datetime import datetime
from flask import Flask, request, jsonify, render_template, Response, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

#Crear el server Flask
app = Flask(__name__)

#Renderiza Index.html 
@app.route("/")
def index():
    try:
        return render_template('index.html')
    except:
        return jsonify({'trace': traceback.format_exc()})
    
    
if __name__ == '__main__':
    #Lanzar server
    app.run(host="127.0.0.1", port=5000, debug= True)