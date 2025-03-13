from flask import Blueprint, request, jsonify, current_app, send_file
import os
from utils.whisper_utils import transcribe_file

upload_bp = Blueprint('upload', __name__)

@upload_bp.route('/', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    upload_folder = current_app.config['UPLOAD_FOLDER']
    file_path = os.path.join(upload_folder, file.filename)
    file.save(file_path)

    try:
        transcription = transcribe_file(file_path)
        os.remove(file_path)  # 處理完成後刪除上傳的文件

        # 將轉換結果保存為文字文件
        download_folder = current_app.config['DOWNLOAD_FOLDER']
        os.makedirs(download_folder, exist_ok=True)
        text_file_path = os.path.join(download_folder, f"{os.path.splitext(file.filename)[0]}.txt")
        with open(text_file_path, 'w', encoding='utf-8') as text_file:
            text_file.write(transcription)

        # 返回轉換結果和下載 URL
        return jsonify({
            "transcription": transcription,
            "download_url": f"/download/{os.path.basename(text_file_path)}"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500