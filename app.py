from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/hello', methods=['GET'])
def hello_world():
    name = '' if 'name' not in request.args else request.args['name']
    message = '' if 'message' not in request.args else request.args['message']
    return render_template('hello.html', name=name, message=message)


if __name__ == '__main__':
    app.run()
