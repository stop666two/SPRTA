# 🚀 SPRTA - Stop666 Python Rename Tool for Android  
**File Renaming Powerhouse | Android Terminal Batch Processing Tool | Source: [GitHub](https://github.com/stop666two/SPRTA/tree/f7fee9a7eca66fc10f6c9fe2ceda3997be59690b)**  

**Languages**: [🇺🇸 English](README.md) | [🇨🇳 简体中文](https://github.com/stop666two/SPRTA/blob/332a82837d57791498e611b9db2e1dd1c9940c2e/Introduce/Chinese.md)

---

## 🔥 **Core Highlights**  
| 🌟 Feature | 📌 Description |  
|-----------|----------------|  
| **Smart Renaming** | Modify/append prefixes/suffixes while preserving file structures (e.g., `file.txt` → `new_file.666.txt`) |  
| **Text Injection** | Batch insert multi-line headers into files |  
| **Safety System** | Auto-backup + detailed logs (timestamps, operation records, parameters) |  
| **Cross-Platform** | UTF-8 encoding + ANSI colors for Termux compatibility |  
| **License** | Apache-2.0 (No redistribution/sales allowed) |  

---

## 📦 **Feature Details**  
### 1. **Prefix/Suffix Operations**  
- **Modify Prefix**: Replace full filename prefix (e.g., `old_name.txt` → `new_prefix.txt`)  
- **Add Prefix**: Insert content before/after original prefix (e.g., `file.txt` → `pre_file.txt` or `file_pre.txt`)  
- **Modify Suffix**: Replace full suffix (e.g., `.txt` → `.md`)  
- **Add Suffix**: Append content before/after original suffix (e.g., `file.txt` → `file.666.txt` or `file.txt.666`)  

### 2. **Text Injection**  
- Insert multi-line content at file headers (e.g., copyright notices, version info).  
  **Example**:  
  ```python
  # Inserted content example
  "SPRTA Tool - v1.0.0"
  "Author: Stop666two"

###3. **Auto-Backup & Logging**

Generates timestamped backup directories ( backup_2023-10-01_12-30-45 )
Logs include:

Backup Time: 2023-10-01_12-30-45
Function Used: Add Suffix
Parameters: Position=1, Content=.666
Modified Files:
file.txt -> file.666.txt

 

## 📌 **Installation Guide**

📱 Termux Environment

# Install Python and clone repo
pkg install python -y

git clone https://github.com/stop666two/SPRTA.git

cd SPRTA

# Run the tool
python3 sprta.py

🖥️ Universal Linux/macOS

# Ensure Python 3 is installed
git clone https://github.com/stop666two/SPRTA.git
cd SPRTA

chmod +x sprta.py

./sprta.py

 

## 📎 **License**

Apache-2.0 License

Free Use: Personal & commercial projects
No Redistribution: Source code/binaries cannot be resold/distributed
Attribution Required: Modified code must retain original copyright + change logs

 

## 🧑‍💻 **Contribution Guide**

Contributions welcome via GitHub!

🐛 Report Issues: GitHub Issues
💡 Suggest Improvements: Submit feature requests
🛠️ Code Contributions: Follow PEP8 style guide

 

## 👤 **Author**

Stop666two
📧 Email: stop666bilibili@gmail.com
🌐 GitHub: github.com/stop666two

 

🌟 SPRTA - Master Android file workflows with Python magic!
