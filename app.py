from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Leo Santana v1.0"