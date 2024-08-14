from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def serve_index():
    return "Hello from Flask!"

@app.route('/api/test')
def test_api():
    return jsonify(message="Hello from Flask API!")

if __name__ == '__main__':
    app.run(debug=True)