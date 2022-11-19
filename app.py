from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/hello', methods=['GET'])
def hello_world():
    name = 'Rekruto' if 'name' not in request.args else request.args['name']
    message = 'Давай дружить' if 'message' not in request.args else request.args['message']
    return f'{name}!{message}!'


if __name__ == '__main__':
    app.run()
