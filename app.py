from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def first_req():
    return 'First request'

@app.route('/second-request', methods=['GET'])
def second_req():
    return 'Second request'

@app.route('/third-request', methods=['GET'])
def third_req():
    return 'Third request'

if __name__ == '__main__':
    app.run()
