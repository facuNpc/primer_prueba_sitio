import traceback
from datetime import datetime
from flask import Flask, request, jsonify, render_template, Response, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

#Crear el server Flask
app = Flask(__name__)

if __name__ == '__main__':

    #lanzar server
    app.run(host="127.0.0.1", port=5000)