# 🚀 SPRTA - Stop666 Python Rename Tool for Android  
**文件重命名神器 | Android 终端批量处理利器 | 开源地址：[GitHub](https://github.com/stop666two/SPRTA/tree/f7fee9a7eca66fc10f6c9fe2ceda3997be59690b)**  

---

## 🔥 **核心亮点**  
| 🌟 特性 | 📌 说明 |  
|--------|--------|  
| **智能重命名** | 支持前缀/后缀修改、保留原结构（如 `file.txt` → `new_file.666.txt`） |  
| **文本注入** | 批量向文件头部插入多行文本（代码、注释等） |  
| **安全防护** | 自动备份 + 详细日志（时间戳、操作记录、参数） |  
| **跨平台兼容** | UTF-8 编码 + ANSI 颜色，Termux 环境完美运行 |  
| **许可证** | Apache-2.0（禁止倒卖，违者必究） |  

---

## 📦 **功能详解**  
### 1. **前缀/后缀操作**  
- **修改前缀**：替换文件名整体前缀（如 `old_name.txt` → `new_prefix.txt`）  
- **添加前缀**：选择在原前缀前/后添加内容（如 `file.txt` → `pre_file.txt` 或 `file_pre.txt`）  
- **修改后缀**：完整替换后缀（如 `.txt` → `.md`）  
- **添加后缀**：在原后缀前/后追加内容（如 `file.txt` → `file.666.txt` 或 `file.txt.666`）  

### 2. **文本注入**  
- 向任意文本文件头部插入多行内容（如版权声明、版本信息）。  
  **示例**：  
  # 插入内容示例
  "SPRTA Tool - v1.0.0"
  "Author: Stop666two"

### 3. **自动备份与日志**

操作前自动生成带时间戳的备份目录（ backup_2023-10-01_12-30-45 ）
日志文件记录：

备份时间：2023-10-01_12-30-45
使用功能：添加后缀
参数：位置=1, 内容=.666
修改的文件列表：
file.txt -> file.666.txt


## 📌 **安装指南**

📱 Termux 环境

# 安装 Python 并克隆仓库
pkg install python -y

git clone https://github.com/stop666two/SPRTA.git

cd SPRTA
# 运行工具
python3 sprta.py

🖥️ 通用 Linux/macOS

# 确保 Python 3 已安装
git clone https://github.com/stop666two/SPRTA.git

cd SPRTA

chmod +x sprta.py

./sprta.py


## 📎 **许可证**

Apache-2.0 License

免费使用：个人或商业项目均免费
禁止倒卖：不得将源码或编译版本用于分发、销售
保留声明：修改后的代码需保留原始版权与变更声明


## 🧑‍💻 **贡献指南**

欢迎提交 Issue 和 Pull Request！

🐛 报告问题：GitHub Issues
💡 建议改进：提交功能需求或优化建议
🛠️ 代码贡献：请遵循 PEP8 编码规范


## 👤 **作者**

Stop666two
📧 邮箱: stop666bilibili@gmail.com
🌐 GitHub: github.com/stop666two


🌟 SPRTA - 用 Python 魔法掌控 Android 文件世界！*
