from apis_app import apis_app

@apis_app.route('/', methods=['GET'])
def api_hello():
    return {'message': 'Hello, API!'}
