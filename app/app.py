from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='pwa')

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/manifest.json')
def serve_manifest():
    return send_from_directory(app.static_folder, 'manifest.json')

@app.route('/service-worker.js')
def serve_service_worker():
    return send_from_directory(app.static_folder, 'service-worker.js')

@app.route('/assets/<path:path>')
def serve_assets(path):
    return send_from_directory(f'{app.static_folder}/assets', path)

@app.route('/icons/<path:path>')
def serve_icons(path):
    return send_from_directory(f'{app.static_folder}/icons', path)

#@app.route('/api/analyze', methods=['POST']) ....

if __name__ == '__main__':
    app.run(debug=True)