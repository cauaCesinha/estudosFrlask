from flask import Flask 

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Ola<br>Mundo!</h1>"

@app.route("/aluno/<name>")
def aluno(name):
    return f'<h1> {name}</h1>' 