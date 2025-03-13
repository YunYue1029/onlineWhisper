from flask import Flask, render_template ,jsonify
from routes.upload import upload_bp
from routes.download import download_bp

# 初始化 Flask 應用
app = Flask(__name__)

# 指定上傳文件夾
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['DOWNLOAD_FOLDER'] = 'downloads'
# 註冊 Blueprint
app.register_blueprint(upload_bp, url_prefix='/upload')
app.register_blueprint(download_bp, url_prefix='/download')

@app.route('/')
def home():
    # 渲染 index.html 作為主頁
    return render_template('index.html')

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Page not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)


