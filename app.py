from flask import Flask, render_template,abort
import json

with open('books.json') as file:
    libros=json.load(file)

app = Flask(__name__)

@app.route('/')
def inicio():
    print(libros)
    return render_template("Inicio.html",datos=libros)


app.run(debug=True)