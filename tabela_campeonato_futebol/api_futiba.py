from flask import Flask, request, jsonify
import negocio


app = Flask(__name__)


@app.route("/partidas", methods=["POST"])
def cadastra_partida():
    dado = request.json
    print(dado)
    try:
        negocio.cadastra_partida(dado)    
        return dado, 201
    except:
        return {'title': 'erro no cadastra partida', "status": 402}, 402

@app.route("/times", methods=["GET"])
def recupera_times():
    try:
        dados = negocio.monta_tabela_classificacao()
        result = []
        for time in dados:
            d = {"nome": time[0], "pontos": time[1], "jogos": time[2], "vitorias": time[3], 
            "empates": time[4], "derrotas": time[5],
            "gols_contra": time[6], "gols_pro": time[7],
            "saldo": time[8], "aproveitamento": time[9]}
            
            result.append(d)
        return result, 200
    except:
        return {'title': 'erro na recuperacao', 'status': 401}, 401










app.run(debug=True)