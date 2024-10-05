from flask import Flask, jsonify, request

app = Flask(__name__)

#Aqui colocaremos nossas funcoes
@app.route("/hello", methods=["GET"])
def hello():
    return "Ola mundo!"

@app.route("/echo/<msg>", methods=["GET"])
def echo(msg):
    return msg.upper()



app.run(debug=True)