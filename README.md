# DirLocker

A lightweight Python-based directory encryption utility. It uses Bitwise NOT operations to quickly lock and unlock all files within a specified directory.

## 🛠 Features

- **Fast Encryption**: High-speed bitwise inversion to alter file data without complex keys.
- **Recursive Scanning**: Automatically detects and processes all files within subdirectories.
- **Safety Measures**: Appends a `.lock` extension to processed files to prevent accidental modification.
- **Colorized UI**: Integration with `colorama` for clear, color-coded terminal feedback.

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3 installed and the required dependency:

```
pip install colorama
```
Usage
1. Run the script:
```
python DirLocker.py
```

2. **Enter Directory**: Input the absolute or relative path of the target folder.
3. **Select Operation**:
   - Enter `0` to **Lock** (Encrypt and add `.lock` extension).
   - Enter `1` to **Unlock** (Decrypt and remove `.lock` extension).

## ⚙️ How it Works

1. **Bitwise Logic**: The core algorithm applies a bitwise NOT operation (`~b & 0xFF`) to every byte in a file. Running this operation twice returns the data to its original state.
2. **File Handling**: The script renames files to include a `.lock` suffix when encrypted to keep track of processed data.

## ⚠️ Disclaimer

- **Permission**: Ensure you have explicit consent from the computer owner before running this tool.
- **Liability**: This tool is for educational purposes. The developer is not responsible for any data loss or errors.
- **Best Practice**: Always perform a backup of important data before running batch encryption scripts.
