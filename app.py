from flask import Flask, jsonify, request

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

@app.before_request
def verify_token():
    if request.method == 'POST':
        if 'X-Auth-Token' not in request.headers:
            return jsonify({'status': 'false', 'message': 'Missing token'}), 401

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
    app.run(debug=True)
