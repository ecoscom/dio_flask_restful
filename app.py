import json
from flask import Flask, jsonify, request

app = Flask(__name__)

deseenvolvedores = [
    {   'id': '0',
        'nome':'Evandro',
        'habilidades': ['Python', 'Django']
    },
    {   'id': '1',
        'nome':'Costa',
        'habilidades':['Python', 'Flask']
    }
]

@app.route('/dev/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = deseenvolvedores[id]
        except IndexError:
            response = {'status':'error', 'message':'Index ({}) not found'.format(id)}
        except Exception:
            response = { 'status':'error', 'message': 'Unknow error' }
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        deseenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        deseenvolvedores.pop(id)
        return jsonify({'status':'success', 'message':'Deleted'})

@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(deseenvolvedores)
        dados['id'] = posicao
        deseenvolvedores.append(dados)
        return jsonify({'status':'success', 'message':'Successful insert!'})
    elif request.method == 'GET':
        return jsonify(deseenvolvedores)




if __name__ == '__main__':
    app.run(debug=True)