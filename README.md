 Python RPA 影像辨識自動化腳本 (Image-based Automation Tool)

本專案是一個輕量級的 RPA (Robotic Process Automation) 工具，利用 Python 結合 OpenCV 影像辨識技術，自動執行 GUI 介面上的點擊操作。

目前主要應用於自動處理特定的錯誤流程（如代號 E1030），透過預先截取的按鈕圖檔，程式能自動偵測螢幕畫面並依序模擬滑鼠點擊，實現無人值守的自動化修復或操作。

 🚀 功能特色 (Features)
影像識別定位：使用 OpenCV (`cv2.matchTemplate`) 進行模板比對，精準定位螢幕上的按鈕位置。
順序執行邏輯：依照資料夾中的檔案編號（如 `1.jpg`, `2.jpg`...）依序偵測並執行點擊。
智慧等待機制：若畫面上尚未出現目標按鈕，程式會自動等待並持續偵測，直到目標出現才進行點擊。
真實滑鼠模擬：使用 `mouse` 函式庫模擬真實的滑鼠移動與點擊行為。

 🛠️ 技術堆疊 (Tech Stack)
 程式語言：Python
 核心函式庫：
     `opencv-python` (OpenCV)：用於影像處理與模板比對。
     `numpy`：處理影像矩陣運算。
     `pyautogui`：用於快速擷取螢幕畫面。
     `mouse`：用於控制滑鼠移動與點擊。

 📂 專案架構 (Project Structure)
為了讓腳本正確執行，請確保檔案目錄結構如下：
```text
Project/
├── main.py            主程式碼 (包含 error_handler 與 rpa_ws 類別)
├── RPA/
│   └── E1030/         存放樣板圖片的資料夾
│       ├── 1.jpg      步驟 1 要點擊的按鈕截圖
│       ├── 2.jpg      步驟 2 要點擊的按鈕截圖
│       └── ...        依此類推
└── README.md

