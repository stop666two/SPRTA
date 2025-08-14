# -*- coding: utf-8 -*-
import os
import shutil
import datetime
import sys

# ANSI 颜色代码（Termux 兼容）
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"

# 程序信息
PROGRAM_NAME = "SPRTA"
FULL_NAME = "Stop666-Python-Rename-Tool-Android"
AUTHOR = "stop666two"
EMAIL = "stop666bilibili@gmail.com"
REPO_URL = "https://github.com/stop666two/SPRTA"
VERSION = "1.0.0"
COPYRIGHT = "免费程序，严禁倒卖，违者必究。"

def clear_screen():
    """清屏函数（跨平台兼容）"""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_welcome():
    """显示欢迎界面"""
    clear_screen()
    print(f"{BOLD}{CYAN}{'='*40}{RESET}")
    print(f"{BOLD}{CYAN}  SPRTA - 文件重命名工具  {RESET}")
    print(f"{BOLD}{CYAN}{'='*40}{RESET}")
    print(f"{GREEN}全称：{FULL_NAME}{RESET}")
    print(f"{GREEN}作者：{AUTHOR}{RESET}")
    print(f"{GREEN}邮箱：{EMAIL}{RESET}")
    print(f"{GREEN}开源地址：{REPO_URL}{RESET}")
    print(f"{GREEN}版本：{VERSION}{RESET}")
    print(f"{RED}{COPYRIGHT}{RESET}")

def show_disclaimer():
    """显示免责声明"""
    clear_screen()
    print(f"{BOLD}{CYAN}===== 免责协议 ====={RESET}")
    print("本软件按“原样”提供，不提供任何明示或暗示的保证。")
    print("使用本软件造成的任何数据损坏或丢失，作者概不负责。")
    print(f"{COPYRIGHT}")
    choice = input(f"{YELLOW}输入 y 同意协议，其他键退出程序：{RESET}").lower()
    if choice != 'y':
        sys.exit()

def create_backup(function_name, params):
    """创建备份并生成日志文件"""
    try:
        now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backup_dir = f"backup_{now}"
        os.makedirs(backup_dir, exist_ok=True)

        current_dir = os.getcwd()
        script_name = os.path.basename(__file__)
        backed_up = []

        for filename in os.listdir(current_dir):
            if filename == script_name or filename.startswith('backup_'):
                continue
            file_path = os.path.join(current_dir, filename)
            if os.path.isfile(file_path):
                shutil.copy2(file_path, os.path.join(backup_dir, filename))
                backed_up.append(filename)

        stats_file = os.path.join(backup_dir, "backup_stats.txt")
        with open(stats_file, 'w', encoding='utf-8') as f:
            f.write(f"备份时间：{now}\n")
            f.write(f"使用功能：{function_name}\n")
            f.write("参数：\n")
            for key, value in params.items():
                f.write(f"  {key}: {value}\n")
            f.write("修改的文件列表：\n")
            f.write("(操作完成后自动生成)\n")
            f.write(f"开源地址：{REPO_URL}\n")
            f.write(f"作者：{AUTHOR}\n")
            f.write(f"邮箱：{EMAIL}\n")
            f.write(f"版本号：{VERSION}\n")
            f.write(f"{COPYRIGHT}\n")
        return stats_file, backed_up
    except Exception as e:
        print(f"{RED}创建备份失败：{str(e)}{RESET}")
        return None, []

def update_stats(stats_file, modified_files):
    """更新操作日志"""
    try:
        if not stats_file or not os.path.exists(stats_file):
            return
        with open(stats_file, 'a', encoding='utf-8') as f:
            f.write("\n修改的文件列表：\n")
            if not modified_files:
                f.write("  没有修改任何文件\n")
            else:
                for old, new in modified_files:
                    f.write(f"  {old} -> {new}\n")
    except Exception as e:
        print(f"{RED}更新日志失败：{str(e)}{RESET}")

def get_function_description():
    """功能描述"""
    return {
        '1': "修改前缀：替换文件名的整个前缀部分",
        '2': "添加前缀：选择在原前缀前或后添加内容",
        '3': "修改后缀：将后缀替换为新的完整后缀",
        '4': "添加后缀：选择在原后缀前或后添加内容",
        '5': "特殊功能：在文件最前面添加多行文本",
        '6': "显示作者信息",
        '7': "显示程序关于信息",
        '8': "退出程序"
    }

def main_menu():
    """主菜单"""
    while True:
        clear_screen()
        print(f"{BOLD}{CYAN}===== SPRTA - 文件重命名工具 ====={RESET}")
        print(f"{GREEN}全称：{FULL_NAME}{RESET}")
        print(f"{GREEN}版本：{VERSION}{RESET}")
        print(f"{GREEN}作者：{AUTHOR}{RESET}")
        print(f"{GREEN}邮箱：{EMAIL}{RESET}")
        print(f"{GREEN}开源地址：{REPO_URL}{RESET}")
        print(f"{YELLOW}请从下列选项中选择操作：{RESET}")

        descriptions = get_function_description()
        for i in range(1, 9):
            print(f"{i}. {descriptions[str(i)]}")

        print(f"{YELLOW}{COPYRIGHT}{RESET}")
        choice = input(f"{YELLOW}请输入选项(1-8)：{RESET}").strip()
        if choice in [str(i) for i in range(1, 9)]:
            if choice == '8':
                print(f"{GREEN}感谢使用 SPRTA，再见！{RESET}")
                sys.exit()
            return choice
        print(f"{YELLOW}无效输入，请重新输入！{RESET}")

# 功能函数（示例实现）

def add_suffix(position, content):
    """添加后缀"""
    modified = []
    for filename in os.listdir():
        if any([
            filename.startswith('backup_'),
            filename == os.path.basename(__file__),
            os.path.isdir(filename)
        ]):
            continue
        
        root, ext = os.path.splitext(filename)
        
        if position == '1':  # 在后缀前添加
            new_name = f"{root}{content}{ext}"  # 直接拼接，不加额外点
        else:                # 在后缀后添加
            if ext:          # 如果有后缀
                new_name = f"{root}{ext}{content}"  # 直接拼接
            else:            # 如果无后缀
                new_name = f"{filename}{content}"   # 直接拼接
        
        if new_name != filename:
            try:
                os.rename(filename, new_name)
                modified.append((filename, new_name))
            except Exception as e:
                print(f"{YELLOW}无法重命名 {filename}: {str(e)}{RESET}")
    return modified

def add_suffix(position, content):
    """添加后缀"""
    modified = []
    for filename in os.listdir():
        if any([
            filename.startswith('backup_'),
            filename == os.path.basename(__file__),
            os.path.isdir(filename)
        ]):
            continue
        
        root, ext = os.path.splitext(filename)
        
        if position == '1':  # 在后缀前添加
            if ext:  # 如果有后缀
                new_name = f"{root}.{content}{ext}"  # 保留原后缀
            else:    # 如果无后缀
                new_name = f"{root}.{content}"       # 添加新后缀
        else:        # 在后缀后添加
            if ext:  # 如果有后缀
                new_name = f"{root}{ext}.{content}"  # 保留原后缀并追加
            else:    # 如果无后缀
                new_name = f"{filename}.{content}"   # 直接追加
        
        if new_name != filename:
            try:
                os.rename(filename, new_name)
                modified.append((filename, new_name))
            except Exception as e:
                print(f"{YELLOW}无法重命名 {filename}: {str(e)}{RESET}")
    return modified

def modify_suffix(new_suffix):
    """修改后缀"""
    modified = []
    for filename in os.listdir():
        if any([
            filename.startswith('backup_'),
            filename == os.path.basename(__file__),
            os.path.isdir(filename)
        ]):
            continue
        root, _ = os.path.splitext(filename)
        new_name = f"{root}{new_suffix}"
        if new_name != filename:
            try:
                os.rename(filename, new_name)
                modified.append((filename, new_name))
            except Exception as e:
                print(f"{YELLOW}无法重命名 {filename}: {str(e)}{RESET}")
    return modified

def add_suffix(position, content):
    """添加后缀"""
    modified = []
    for filename in os.listdir():
        if any([
            filename.startswith('backup_'),
            filename == os.path.basename(__file__),
            os.path.isdir(filename)
        ]):
            continue
        root, ext = os.path.splitext(filename)
        if position == '1':
            new_name = f"{root}.{content}{ext[1:]}" if ext else f"{root}.{content}"
        else:
            new_name = f"{root}{ext}.{content}"
        if new_name != filename:
            try:
                os.rename(filename, new_name)
                modified.append((filename, new_name))
            except Exception as e:
                print(f"{YELLOW}无法重命名 {filename}: {str(e)}{RESET}")
    return modified

def add_prefix_text(lines):
    """在文件开头添加多行文本"""
    modified = []
    for filename in os.listdir():
        if any([
            filename.startswith('backup_'),
            filename == os.path.basename(__file__),
            os.path.isdir(filename)
        ]):
            continue
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            with open(filename, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines) + '\n' + content)
            modified.append((filename, filename))
        except Exception as e:
            print(f"{YELLOW}无法处理文件 {filename}: {str(e)}{RESET}")
    return modified

def show_author():
    """显示作者信息"""
    clear_screen()
    print(f"{BOLD}{CYAN}===== 作者信息 ====={RESET}")
    print(f"{GREEN}作者：{AUTHOR}{RESET}")
    print(f"{GREEN}邮箱：{EMAIL}{RESET}")
    print(f"{GREEN}开源地址：{REPO_URL}{RESET}")
    print(f"{GREEN}版本号：{VERSION}{RESET}")
    print(f"{YELLOW}{COPYRIGHT}{RESET}")
    input(f"{YELLOW}按回车返回主菜单...{RESET}")

def show_about():
    """显示程序关于信息"""
    clear_screen()
    print(f"{BOLD}{CYAN}===== 关于 SPRTA ====={RESET}")
    print("这是一个强大的文件重命名工具")
    print("支持5种重命名模式和详细的备份功能")
    print("特点：")
    print("- 完整的备份系统")
    print("- 支持特殊字符和Emoji")
    print("- 详细的操作日志")
    print("- 开源免费，严禁倒卖")
    print(f"{YELLOW}作者：{AUTHOR}{RESET}")
    print(f"{YELLOW}邮箱：{EMAIL}{RESET}")
    print(f"{YELLOW}开源地址：{REPO_URL}{RESET}")
    input(f"{YELLOW}按回车返回主菜单...{RESET}")

def main():
    """主程序"""
    try:
        show_welcome()
        show_disclaimer()

        while True:
            choice = main_menu()
            function_name = ""
            params = {}
            modified_files = []
            stats_file = None

            try:
                if choice == '1':
                    print(f"{BOLD}{CYAN}\n=== 功能1：修改前缀 ==={RESET}")
                    new_prefix = input(f"{YELLOW}请输入新的前缀（支持特殊符号和Emoji）：{RESET}")
                    function_name = "修改前缀"
                    params = {"新前缀": new_prefix}
                    stats_file, _ = create_backup(function_name, params)
                    modified_files = modify_prefix(new_prefix)

                elif choice == '2':
                    print(f"{BOLD}{CYAN}\n=== 功能2：添加前缀 ==={RESET}")
                    position = input(f"{YELLOW}添加位置（1:前缀前添加 2:前缀后添加）：{RESET}")
                    content = input(f"{YELLOW}请输入添加的内容（支持特殊符号和Emoji）：{RESET}")
                    function_name = "添加前缀"
                    params = {"位置": position, "添加内容": content}
                    stats_file, _ = create_backup(function_name, params)
                    modified_files = add_prefix(position, content)

                elif choice == '3':
                    print(f"{BOLD}{CYAN}\n=== 功能3：修改后缀 ==={RESET}")
                    new_suffix = input(f"{YELLOW}请输入新后缀（必须以点开头，如.txt）：{RESET}")
                    if not new_suffix.startswith('.'):
                        print(f"{YELLOW}错误：后缀必须以点开头！{RESET}")
                        continue
                    function_name = "修改后缀"
                    params = {"新后缀": new_suffix}
                    stats_file, _ = create_backup(function_name, params)
                    modified_files = modify_suffix(new_suffix)

                elif choice == '4':
                    print(f"{BOLD}{CYAN}\n=== 功能4：添加后缀 ==={RESET}")
                    position = input(f"{YELLOW}添加位置（1:后缀前添加 2:后缀后添加）：{RESET}")
                    content = input(f"{YELLOW}请输入添加的内容（支持特殊符号和Emoji）：{RESET}")
                    function_name = "添加后缀"
                    params = {"位置": position, "添加内容": content}
                    stats_file, _ = create_backup(function_name, params)
                    modified_files = add_suffix(position, content)

                elif choice == '5':
                    print(f"{BOLD}{CYAN}\n=== 功能5：添加前导文本 ==={RESET}")
                    print(f"{YELLOW}请输入要添加的文本（输入 END 完成输入）：{RESET}")
                    lines = []
                    while True:
                        line = input()
                        if line.strip().upper() == "END":
                            break
                        lines.append(line)
                    function_name = "添加前导文本"
                    params = {"添加行数": len(lines)}
                    stats_file, _ = create_backup(function_name, params)
                    modified_files = add_prefix_text(lines)

                elif choice == '6':
                    show_author()
                    continue

                elif choice == '7':
                    show_about()
                    continue

                if stats_file:
                    update_stats(stats_file, modified_files)
                    print(f"{GREEN}\n操作完成，共修改{len(modified_files)}个文件！{RESET}")
                else:
                    print(f"{YELLOW}\n操作未执行，未生成备份文件。{RESET}")

            except Exception as e:
                print(f"{RED}发生错误：{str(e)}{RESET}")
                import traceback
                traceback.print_exc()

            input(f"{YELLOW}按回车继续...{RESET}")

    except KeyboardInterrupt:
        print(f"\n{RED}程序被用户中断，退出中...{RESET}")
        sys.exit()
    except Exception as e:
        print(f"{RED}程序发生致命错误：{str(e)}{RESET}")
        sys.exit()

if __name__ == "__main__":
    main()