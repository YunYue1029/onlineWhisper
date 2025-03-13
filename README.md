# ourWhisper

## 概述
本專案是一個基於 **Flask** 的檔案上傳與下載伺服器，提供簡單的 API 來讓使用者上傳與下載文件，上傳的mp3檔案經由whisper來轉換成txt，提供語音為本的轉換。

## 功能
- **首頁渲染**：`index.html`
- **文件上傳**：透過 `/upload` 路由上傳檔案
- **文件下載**：透過 `/download` 路由下載檔案
- **whisper語音轉換**：透過`whisper`的功能來提供語音轉換
- **錯誤處理**：提供 404 頁面錯誤回應

## 安裝與運行
### **1. 安裝 Python 依賴**
請確保已安裝 **Python 3**，然後執行以下指令：
```sh
pip install flask
```

### **2. 啟動 Flask 伺服器**
```sh
python app.py
```