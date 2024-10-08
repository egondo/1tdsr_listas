from flask import Flask, request, jsonify
import db 

app = Flask(__name__)

@app.route("/carros", methods=["GET"])
def recupera_todos_carros():
    return (db.carros, 200)


@app.route("/carros/<int:id>", methods=["GET"])
def recupera_id(id):
    for carro in db.carros:
        if carro['id'] == id:
            return (carro, 200)
    return ({"msg": "carro não existe", "status": 404}, 404)


@app.route("/carros", methods=["POST"])
def insere():
    
    carro = request.json

    for c in db.carros:
        if c['id'] == carro['id'] or c['placa'] == carro['placa']:
            return ({"msg": "Carro já cadastrado", "status": 406}, 406)
    
    db.carros.append(carro)
    return (carro, 201)

@app.route("/carros", methods=["PUT"])
def altera():
    carro = request.json
    for i in range(len(db.carros)):
        info = db.carros[i]
        if info['id'] == carro['id']:
            db.carros[i] = carro
            return jsonify(carro), 200
    
    info = {'msg': 'Carro não encontrado', "status": 404}
    return info, 404


app.run(debug=True)