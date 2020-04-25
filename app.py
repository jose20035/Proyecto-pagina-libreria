from flask import Flask, render_template,abort
import json

with open('books.json') as file:
    libros=json.load(file)

prueba=["hola","bueno","dias"]

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("Inicio.html",datos=libros,hola=prueba)


app.run(debug=True)