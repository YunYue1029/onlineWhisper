from flask import Blueprint, current_app, jsonify, send_file
import os

download_bp = Blueprint('download', __name__)

@download_bp.route('/<filename>', methods=['GET'])
def download_file(filename):
    try:
        download_folder = current_app.config['DOWNLOAD_FOLDER']
        file_path = os.path.join(download_folder, filename)

        # 確認文件是否存在
        if not os.path.exists(file_path):
            return jsonify({"error": "File not found"}), 404

        # 提供文件下載
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500