
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the updated application!"

@app.route('/api/data', methods=['POST'])
def get_data():
    data = request.json
    response = {
        "message": "Data received successfully!",
        "received_data": data
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
