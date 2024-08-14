from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/play', methods=['POST'])
def play():
    # Implement play functionality
    return jsonify({"status": "playing"})

@app.route('/api/pause', methods=['POST'])
def pause():
    # Implement pause functionality
    return jsonify({"status": "paused"})

@app.route('/api/load', methods=['POST'])
def load():
    # Implement load functionality
    return jsonify({"status": "loaded"})

if __name__ == '__main__':
    app.run(debug=True)