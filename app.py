from flask import Flask 
from flask import render_template 
from flask import request
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Ola<br>Mundo!</h1>"

@app.route("/aluno")
def aluno():
    return render_template('formulario.html')

@app.route("/envio", methods=['POST'])
def envioForms():
    nombre = request.form['nome']
    senha = request.form["senha"]

    if senha == '123':
        return render_template('aluno.html', n = nombre)
        
    else:
        
        return 'NÃO PASSARÃO'