# intro-flask-api-rest

# Primeiros Passos em 5 passos

Abra o Editor Replit e rode o codigo abaixo ! 

~~~python 

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello!"

if __name__ == '__main__':
    app.run(debug=True)

~~~


Codigo em execução - https://repl.it/@juanengml/Helloflask

# Como Montando Rotas

~~~python from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello!</h1>"

@app.route("/mask")
def mask():
    return "<h1>Mask Detect!</h1>"

@app.route("/about")
def about():
    return "<h1>Sobre o Projeto !</h1>"

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080,debug=True)

~~~

Codigo: https://repl.it/@juanengml/rotasFlask

# Adicionando Templates

* Cria uma pasta templates
* Dentro da templates, crie um arquivo chamado index.html 

## Depois vamos direcionar nosso index.html para renderizar o template



~~~python 
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080,debug=True)

~~~

codigo fonte: https://repl.it/@juanengml/rotasFlask
