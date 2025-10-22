from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Путь к папке с Unity build
UNITY_BUILD_PATH = os.path.join(os.path.dirname(__file__), 'unity_build')

@app.route('/')
def index():
    """Главная страница - index.html из Unity build"""
    return send_from_directory(UNITY_BUILD_PATH, 'index.html')

@app.route('/<path:filename>')
def serve_build_files(filename):
    """Обслуживание всех файлов Unity build"""
    return send_from_directory(UNITY_BUILD_PATH, filename)

@app.route('/health')
def health():
    """Health check endpoint для render.com"""
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)


