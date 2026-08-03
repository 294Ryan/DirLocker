■[中文](#目錄加密器)　　■[English](#dirlocker)

# ***目錄加密器***

## **目錄**
- [專案概述](#專案概述)
- [重點特色](#重點特色)
- [使用說明](#使用說明)
- [開發須知](#開發須知)
- [使用技術](#使用技術)
- [專案結構](#專案結構)
- [備註](#備註)


## **專案概述**
DirLocker 是一款輕量級 CLI 工具，可對指定目錄下的所有檔案進行**位元反轉加密/解密**，並透過附加 `.lock` 副檔名來標示加密狀態。適合用於快速混淆敏感檔案內容，防止未經授權的直接讀取。


## **重點特色**
- **一鍵加密整個目錄**：遞迴掃描並加密目錄內所有檔案
- **對稱式解密**：相同演算法執行兩次即可還原，無需額外金鑰
- **狀態標示清晰**：加密檔案自動附加 `.lock`，解密後自動移除
- **防重複處理**：已加密的檔案會被自動略過，避免二次損壞
- **彩色終端輸出**：操作結果以顏色區分，狀態一目了然


## **使用說明**

前往 [Releases](https://github.com/294Ryan/DirLocker/releases) 下載最新版本並解壓縮。

- **啟動**：執行 `DirLocker_v1.0.1.exe`
- **功能介紹**：
1. **加密目錄（Lock）**：
   輸入目標目錄路徑後，選擇 `[0] Lock`，工具會遞迴掃描並加密目錄內所有檔案，加密後的檔案將附加 `.lock` 副檔名。
2. **解密目錄（Unlock）**：
   輸入目標目錄路徑後，選擇 `[1] Unlock`，工具會對所有 `.lock` 檔案執行解密還原，並移除 `.lock` 副檔名。


## **開發須知**
1. 請先閱讀以下開發須知並遵守 [MIT License](./LICENSE) 條款。
2. 複製此倉庫至本地：
```
git clone https://github.com/294Ryan/DirLocker.git
```
3. 使用語言：
   - Python 3.x
4. 安裝必要套件：
```
pip install colorama
```
5. 使用技術：請參見[使用技術](#使用技術)
6. 專案結構：請參見[專案結構](#專案結構)


## **使用技術**
- **位元反轉加密（Bitwise NOT）**：對每個位元組執行 `~b & 0xFF`，運算具對稱性，加密與解密使用相同邏輯
- **遞迴目錄遍歷**：使用 `os.walk()` 掃描所有子目錄與檔案
- **副檔名狀態管理**：以 `.lock` 作為加密狀態旗標，搭配 `os.rename()` 進行重命名
- **PyInstaller 打包**：透過 `.spec` 設定檔將程式打包為單一 Windows 執行檔


## **專案結構**
```
DirLocker/
├── .gitignore          # Git 忽略清單
├── icon.ico            # 應用程式圖示
├── LICENSE             # MIT 授權條款
├── main.py             # 主程式
├── main.spec           # PyInstaller 打包設定
└── README.md           # 專案說明文件
```


## **備註**
- 維護者：294Ryan - [GitHub](https://github.com/294Ryan)
- 使用條款：MIT License
- [!] 本專案供教育研究使用，請確保在電腦所有人同意的情況下進行操作。任何因不當使用造成的資料損失或後果請自負。

---

# ***DirLocker***

## **Table of Contents**
- [Overview](#overview)
- [Key Features](#key-features)
- [Usage](#usage)
- [Development](#development)
- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [Notes](#notes)


## **Overview**
DirLocker is a lightweight CLI tool that performs **bitwise NOT encryption/decryption** on all files within a specified directory, marking encrypted files with a `.lock` extension. Designed for quickly obfuscating sensitive file contents to prevent unauthorized direct access.


## **Key Features**
- **Encrypt an entire directory at once**: Recursively scans and encrypts all files within a directory
- **Symmetric decryption**: Running the same algorithm twice restores the original — no key required
- **Clear state labeling**: Encrypted files are automatically appended with `.lock`; decrypted files have it removed
- **Duplicate processing prevention**: Already-encrypted files are automatically skipped to avoid corruption
- **Color-coded terminal output**: Operation results are color-differentiated for at-a-glance status


## **Usage**

Download the latest release from [Releases](https://github.com/294Ryan/DirLocker/releases) and extract it.

- **Launch**: Run `DirLocker_v1.0.1.exe`
- **Features**:
1. **Lock Directory**:
   Enter the target directory path, then select `[0] Lock`. The tool will recursively scan and encrypt all files, appending `.lock` to each encrypted file.
2. **Unlock Directory**:
   Enter the target directory path, then select `[1] Unlock`. The tool will decrypt all `.lock` files and restore their original extensions.


## **Development**
1. Read the following notes and comply with the [MIT License](./LICENSE) terms.
2. Clone this repository:
```
git clone https://github.com/294Ryan/DirLocker.git
```
3. Language:
   - Python 3.x
4. Install required packages:
```
pip install colorama
```
5. Technologies: See [Technologies](#technologies)
6. Project Structure: See [Project Structure](#project-structure)


## **Technologies**
- **Bitwise NOT Encryption**: Applies `~b & 0xFF` to each byte — symmetric by nature, so the same logic handles both encryption and decryption
- **Recursive Directory Traversal**: Uses `os.walk()` to scan all subdirectories and files
- **Extension-based State Management**: Uses `.lock` as an encryption state flag, with `os.rename()` handling renaming
- **PyInstaller Packaging**: Packaged into a single Windows executable via a `.spec` configuration file


## **Project Structure**
```
DirLocker/
├── .gitignore          # Git ignore rules
├── icon.ico            # Application icon
├── LICENSE             # MIT License
├── main.py             # Main program
├── main.spec           # PyInstaller packaging config
└── README.md           # Project documentation
```


## **Notes**
- Maintainer: 294Ryan - [GitHub](https://github.com/294Ryan)
- License: MIT License
- [!] This project is intended for educational and research purposes. Ensure you have the computer owner's consent before use. Any data loss or consequences resulting from misuse are solely your responsibility.
