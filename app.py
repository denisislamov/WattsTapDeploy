from flask import Flask, send_from_directory, make_response
import os
import mimetypes

app = Flask(__name__)

# Путь к папке с Unity build
UNITY_BUILD_PATH = os.path.join(os.path.dirname(__file__), 'unity_build')

# Настройка MIME типов для Unity WebGL
mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('application/wasm', '.wasm')
mimetypes.add_type('application/octet-stream', '.data')
mimetypes.add_type('application/octet-stream', '.symbols.json')

@app.route('/')
def index():
    """Главная страница - index.html из Unity build"""
    response = make_response(send_from_directory(UNITY_BUILD_PATH, 'index.html'))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response

@app.route('/<path:filename>')
def serve_build_files(filename):
    """Обслуживание всех файлов Unity build"""
    response = make_response(send_from_directory(UNITY_BUILD_PATH, filename))
    
    # Установка правильных заголовков для Unity файлов
    if filename.endswith('.js'):
        response.headers['Content-Type'] = 'application/javascript'
    elif filename.endswith('.wasm'):
        response.headers['Content-Type'] = 'application/wasm'
    elif filename.endswith('.data'):
        response.headers['Content-Type'] = 'application/octet-stream'
    
    # Разрешаем кэширование для статических ресурсов
    if filename.startswith('Build/') or filename.startswith('TemplateData/'):
        response.headers['Cache-Control'] = 'public, max-age=31536000'
    
    # CORS заголовки для Unity WebGL
    response.headers['Access-Control-Allow-Origin'] = '*'
    
    return response

@app.route('/health')
def health():
    """Health check endpoint для render.com"""
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)


