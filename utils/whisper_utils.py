import whisper

# 加載 Whisper 模型
model = whisper.load_model("base")

def transcribe_file(file_path):
    """轉換 MP3 文件為文字"""
    result = model.transcribe(file_path)
    return result['text']