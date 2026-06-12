◽️[中文](#資料加密器)    ◽️[English](#dir-locker)

# ***資料加密器***

## **📜目錄**
- [專案概述](#專案概述)
- [重點特色](#重點特色)
- [使用說明](#使用說明)
- [開發須知](#開發須知)
- [使用技術](#使用技術)
- [專案結構](#專案結構)
- [備註](#備註)


## **✏️專案概述**
一款以位元反轉對檔案進行加密與解密的命令列工具，支援對整個目錄批次處理。


## **✨重點特色**
- 快速對整個目錄的加密與解密
- 加密後自動附加 `.lock` 副檔名，解密後自動還原


## **✅️使用說明**
請先下載本倉庫內容並將其解壓縮
- 啟動：執行 主程式如`DirLocker_vX.X.py` 或對應的 `.exe` 檔案。
- 功能介紹：
1. **加密目錄（Lock）：**
    輸入目標目錄路徑後，選擇 `[0] Lock`，程式將遞迴掃描目錄內所有檔案並進行加密，加密後的檔案會附加 `.lock` 副檔名。
2. **解密目錄（Unlock）：**
    輸入目標目錄路徑後，選擇 `[1] Unlock`，程式將掃描目錄內所有 `.lock` 檔案並還原為原始內容與檔名。
- **範例**  
  *加密前:*
  ```
    📁 target_dir/
    ├── 📄 photo.jpg
    └── 📄 document.txt
  ```
  *加密後:*  
  ```
    📁 target_dir/
    ├── 🔒 photo.jpg.lock
    └── 🔒 document.txt.lock
  ```


## **💻開發須知**
1. 請先閱讀以下開發須知並遵守所用條款。
2. 請運行以下指令複製此倉庫至您的本地電腦：
   ```
   cd 目標目錄
   git clone https://github.com/294Ryan/DirLocker.git
   ```
3. 使用語言：
   - Python 3.14
4. 安裝必要工具：
   - Python 模組：請運行以下指令
     ```
     pip install colorama
     ```
5. 使用技術：請參見[使用技術](#使用技術)
6. 專案結構：請參見[專案結構](#專案結構)


## **🛠使用技術**
- **Bitwise NOT 加密**：對每個位元組執行 `~b & 0xFF`，達到可逆的簡易加密效果
- **os.walk 遞迴掃描**：遍歷目錄樹，取得所有子目錄與檔案路徑
- **colorama**：跨平台終端彩色輸出，提升操作回饋可讀性


## **🗂專案結構**
- 主程式為單一程式，如`DirLocker_vX.X.py`，為主要程式啟動點，包含加密、解密、目錄掃描與主流程控制


## **ℹ️備註**
- 維護者：294Ryan - [Github](https://github.com/294Ryan)
- 使用條款：`MIT License`
- 本專案係基於教育與學習之實驗用途，內含諸多不完備之處敬請指教。
- ⚠️本專案供教育研究使用，使用時請尊重所有版權與權利擁有者。
任何因不當使用造成的後果請自負。


---
# ***Dir Locker***

## **📜Table of Contents**
- [Overview](#overview)
- [Features](#features)
- [Usage](#usage)
- [Development](#development)
- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [Notes](#notes)


## **✏️Overview**
A command-line tool that encrypts and decrypts files using Bitwise NOT operations, supporting batch processing of entire directories.


## **✨Features**
- Encrypt or decrypt entire directories recursively
- Automatically appends `.lock` extension on encryption and restores original name on decryption


## **✅️Usage**
Download and extract the repository content.
- Launch: Run main py file like `DirLocker_vX.X.py` or the corresponding `.exe` file.
- Features:
1. **Lock (Encrypt):**
    Enter the target directory path and select `[0] Lock`. The program will recursively scan and encrypt all files, appending a `.lock` extension to each.
2. **Unlock (Decrypt):**
    Enter the target directory path and select `[1] Unlock`. The program will scan for all `.lock` files and restore them to their original content and filename.
- **Example**  
  *Before Lock:*
  ```
    📁 target_dir/
    ├── 📄 photo.jpg
    └── 📄 document.txt
  ```
  *After Lock:*
  ```
    📁 target_dir/
    ├── 🔒 photo.jpg.lock
    └── 🔒 document.txt.lock
  ```


## **💻Development**
1. Please read the following development guidelines and comply with the terms and conditions.
2. Clone this repository to your local machine:
   ```
   cd target-directory
   git clone https://github.com/294Ryan/DirLocker.git
   ```
3. Language used:
   - Python
4. Install dependencies:
   - Python modules:
     ```
     pip install colorama
     ```
5. Technologies: See [Technologies](#technologies)
6. Project Structure: See [Project Structure](#project-structure)


## **🛠Technologies**
- **Bitwise NOT Encryption**: Applies `~b & 0xFF` to each byte for simple reversible encryption
- **os.walk Recursive Scan**: Traverses directory trees to collect all file paths
- **colorama**: Cross-platform terminal color output for improved operation feedback


## **🗂Project Structure**
- `DirLocker_vX.X.py` Main entry point; contains encrypt, decrypt, directory scan, and main flow logic


## **ℹ️Notes**
- Maintainer: 294Ryan - [Github](https://github.com/294Ryan)
- License: `MIT License`
- This project is for educational and learning experimental purposes and contains many imperfections; your feedback is welcome.
- ⚠️This project is for educational and research purposes only. Please respect all copyrights and rights holders.
Any consequences arising from misuse are solely your responsibility.
