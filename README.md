# intro-flask-api-rest

# Primeiros Passos 

Abra o Editor Replit e rode o codigo abaixo ! 

ˋˋˋ 
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello!"

if __name__ == '__main__':
    app.run(debug=True)
 ˋˋˋ

Codigo em execução - https://repl.it/@juanengml/Helloflask
