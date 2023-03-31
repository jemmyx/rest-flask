from flask import Flask, jsonify

app = Flask(__name__)

# test data
bands = [
    {
        'id': 1,
        'name': 'Metallica',
        'origin': 'US'
    },
    {
        'id': 2,
        'name': 'Slipknot',
        'origin': 'US'
    },
    {
        'id': 3,
        'name': 'Pantera',
        'origin': 'US'
    },
    {
        'id': 4,
        'name': 'Markdu',
        'origin': 'Sweden'
    }
]

@app.route('/', methods=['GET'])
def first_req():
    data = {'status': 'true','message': 'first request'}
    return jsonify(data)

@app.route('/second-request', methods=['GET'])
def second_req():
    data = {'status': 'true','message': 'second request'}
    return jsonify(data)

@app.route('/third-request', methods=['GET'])
def third_req():
    data = {'status': 'true','message': 'third request'}
    return jsonify(data)

@app.route('/bands', methods=['GET'])
def get_bands():
    data = bands
    return jsonify(data)

if __name__ == '__main__':
    app.run()
