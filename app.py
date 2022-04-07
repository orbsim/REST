from flask import Flask, jsonify, request

app = Flask(__name__)

langueges = ['Python', 'JavaScript', 'Java']




@app.route('/', methods=['GET'])
def get_langueges():
    #return jsonify(langueges)
    return {'langueges': langueges}


@app.route('/<int:index>', methods=['GET'])
def get_languege(index):
    try:
        return  {'languege': langueges[index]}, 200
    except IndexError:
        return {}, 404

    




@app.route('/', methods=['POST'])
def create_languege():
    arg = request.get_json()
    if arg.get('name'):
        langueges.append(arg['name'])
        return {}, 201
    return {}


@app.route('/<int:index>', methods=['PUT'])
def modify_languege(index):
    arg = request.get_json()
    if arg.get('name'):
        try:
            langueges[index] = arg['name']
            #204: request has not any response but if modify exists, it done
            return {}, 204 
        except IndexError:
            #404: page not found
            return {}, 404
    #400: bad request
    return {}, 400
        


@app.route('/<int:index>', methods=['DELETE'])
def delete_languege(index):
    try:
        del langueges[index]
        return {}, 204
    except IndexError:
        return {}, 404