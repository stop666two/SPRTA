# -*- coding: utf-8 -*-
import os
import shutil
import datetime
import sys

# ANSI Color Codes
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"

# Program Info
PROGRAM_NAME = "SPRTA"
FULL_NAME = "Stop666-Python-Rename-Tool-Android"
AUTHOR = "stop666two"
EMAIL = "stop666bilibili@gmail.com"
REPO_URL = "https://github.com/stop666two/SPRTA"
VERSION = "1.0.0"
COPYRIGHT = "Free software, no redistribution allowed."

def clear_screen():
    """Clear screen for cross-platform compatibility"""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_welcome():
    """Welcome screen"""
    clear_screen()
    print(f"{BOLD}{CYAN}{'='*40}{RESET}")
    print(f"{BOLD}{CYAN}  SPRTA - File Renaming Tool  {RESET}")
    print(f"{BOLD}{CYAN}{'='*40}{RESET}")
    print(f"{GREEN}Full Name: {FULL_NAME}{RESET}")
    print(f"{GREEN}Author: {AUTHOR}{RESET}")
    print(f"{GREEN}Email: {EMAIL}{RESET}")
    print(f"{GREEN}GitHub: {REPO_URL}{RESET}")
    print(f"{GREEN}Version: {VERSION}{RESET}")
    print(f"{RED}{COPYRIGHT}{RESET}")

def show_disclaimer():
    """Disclaimer screen"""
    clear_screen()
    print(f"{BOLD}{CYAN}===== Disclaimer ====={RESET}")
    print("This software is provided 'as is', without any warranty.")
    print("The author is not responsible for data loss or corruption.")
    print(f"{COPYRIGHT}")
    choice = input(f"{YELLOW}Type 'y' to accept, any other key to exit: {RESET}").lower()
    if choice != 'y':
        sys.exit()

def create_backup(function_name, params):
    """Create backup and generate log file"""
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
            f.write(f"Backup Time: {now}\n")
            f.write(f"Function Used: {function_name}\n")
            f.write("Parameters:\n")
            for key, value in params.items():
                f.write(f"  {key}: {value}\n")
            f.write("Modified Files:\n")
            f.write("(Generated after operation)\n")
            f.write(f"GitHub: {REPO_URL}\n")
            f.write(f"Author: {AUTHOR}\n")
            f.write(f"Email: {EMAIL}\n")
            f.write(f"Version: {VERSION}\n")
            f.write(f"{COPYRIGHT}\n")
        return stats_file, backed_up
    except Exception as e:
        print(f"{RED}Failed to create backup: {str(e)}{RESET}")
        return None, []

def update_stats(stats_file, modified_files):
    """Update operation log"""
    try:
        if not stats_file or not os.path.exists(stats_file):
            return
        with open(stats_file, 'a', encoding='utf-8') as f:
            f.write("\nModified Files:\n")
            if not modified_files:
                f.write("  No files modified\n")
            else:
                for old, new in modified_files:
                    f.write(f"  {old} -> {new}\n")
    except Exception as e:
        print(f"{RED}Failed to update log: {str(e)}{RESET}")

def get_function_description():
    """Function descriptions"""
    return {
        '1': "Modify Prefix: Replace the entire prefix of the filename",
        '2': "Add Prefix: Add content before or after the existing prefix",
        '3': "Modify Suffix: Replace the entire suffix with a new one",
        '4': "Add Suffix: Add content before or after the existing suffix",
        '5': "Add Header: Add multiple lines of text at the beginning of files",
        '6': "Show Author Info",
        '7': "Show About Info",
        '8': "Exit Program"
    }

def main_menu():
    """Main menu"""
    while True:
        clear_screen()
        print(f"{BOLD}{CYAN}===== SPRTA - File Renaming Tool ====={RESET}")
        print(f"{GREEN}Full Name: {FULL_NAME}{RESET}")
        print(f"{GREEN}Version: {VERSION}{RESET}")
        print(f"{GREEN}Author: {AUTHOR}{RESET}")
        print(f"{GREEN}Email: {EMAIL}{RESET}")
        print(f"{GREEN}GitHub: {REPO_URL}{RESET}")
        print(f"{YELLOW}{COPYRIGHT}{RESET}")
        print(f"{YELLOW}Select an operation from the options below:{RESET}")

        descriptions = get_function_description()
        for i in range(1, 9):
            print(f"{i}. {descriptions[str(i)]}")

        choice = input(f"{YELLOW}Enter option (1-8): {RESET}").strip()
        if choice in [str(i) for i in range(1, 9)]:
            if choice == '8':
                print(f"{GREEN}Thank you for using SPRTA, goodbye!{RESET}")
                sys.exit()
            return choice
        print(f"{YELLOW}Invalid input, please try again!{RESET}")

def modify_prefix(new_prefix):
    """Modify prefix"""
    modified = []
    for filename in os.listdir():
        if any([
            filename.startswith('backup_'),
            filename == os.path.basename(__file__),
            os.path.isdir(filename)
        ]):
            continue
        root, ext = os.path.splitext(filename)
        new_name = f"{new_prefix}{ext}"
        if new_name != filename:
            try:
                os.rename(filename, new_name)
                modified.append((filename, new_name))
            except Exception as e:
                print(f"{YELLOW}Failed to rename {filename}: {str(e)}{RESET}")
    return modified

def add_prefix(position, content):
    """Add prefix"""
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
            new_name = f"{content}{root}{ext}"
        else:
            new_name = f"{root}{content}{ext}"
        if new_name != filename:
            try:
                os.rename(filename, new_name)
                modified.append((filename, new_name))
            except Exception as e:
                print(f"{YELLOW}Failed to rename {filename}: {str(e)}{RESET}")
    return modified

def modify_suffix(new_suffix):
    """Modify suffix"""
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
                print(f"{YELLOW}Failed to rename {filename}: {str(e)}{RESET}")
    return modified

def add_suffix(position, content):
    """Add suffix"""
    modified = []
    for filename in os.listdir():
        if any([
            filename.startswith('backup_'),
            filename == os.path.basename(__file__),
            os.path.isdir(filename)
        ]):
            continue
        root, ext = os.path.splitext(filename)
        if position == '1':  # Before suffix
            new_name = f"{root}{content}{ext}"
        else:  # After suffix
            if ext:
                new_name = f"{root}{ext}{content}"
            else:
                new_name = f"{filename}{content}"
        if new_name != filename:
            try:
                os.rename(filename, new_name)
                modified.append((filename, new_name))
            except Exception as e:
                print(f"{YELLOW}Failed to rename {filename}: {str(e)}{RESET}")
    return modified

def add_prefix_text(lines):
    """Add multiple lines to the beginning of files"""
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
            print(f"{YELLOW}Failed to process {filename}: {str(e)}{RESET}")
    return modified

def show_author():
    """Show author info"""
    clear_screen()
    print(f"{BOLD}{CYAN}===== Author Info ====={RESET}")
    print(f"{GREEN}Author: {AUTHOR}{RESET}")
    print(f"{GREEN}Email: {EMAIL}{RESET}")
    print(f"{GREEN}GitHub: {REPO_URL}{RESET}")
    print(f"{GREEN}Version: {VERSION}{RESET}")
    print(f"{YELLOW}{COPYRIGHT}{RESET}")
    input(f"{YELLOW}Press Enter to return...{RESET}")

def show_about():
    """Show about info"""
    clear_screen()
    print(f"{BOLD}{CYAN}===== About SPRTA ====={RESET}")
    print("This is a powerful file renaming tool")
    print("Supports 5 renaming modes and detailed backup system")
    print("Features:")
    print("- Full backup system")
    print("- Supports special characters and Emoji")
    print("- Detailed operation logs")
    print("- Open-source and free, redistribution is prohibited")
    print(f"{YELLOW}Author: {AUTHOR}{RESET}")
    print(f"{YELLOW}Email: {EMAIL}{RESET}")
    print(f"{YELLOW}GitHub: {REPO_URL}{RESET}")
    input(f"{YELLOW}Press Enter to return...{RESET}")

def main():
    """Main program"""
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
                    print(f"{BOLD}{CYAN}\n=== Function 1: Modify Prefix ==={RESET}")
                    new_prefix = input(f"{YELLOW}Enter new prefix (supports symbols and Emoji): {RESET}")
                    function_name = "Modify Prefix"
                    params = {"New Prefix": new_prefix}
                    stats_file, _ = create_backup(function_name, params)
                    modified_files = modify_prefix(new_prefix)

                elif choice == '2':
                    print(f"{BOLD}{CYAN}\n=== Function 2: Add Prefix ==={RESET}")
                    position = input(f"{YELLOW}Add position (1: Before prefix 2: After prefix): {RESET}")
                    content = input(f"{YELLOW}Enter content to add (supports symbols and Emoji): {RESET}")
                    function_name = "Add Prefix"
                    params = {"Position": position, "Content": content}
                    stats_file, _ = create_backup(function_name, params)
                    modified_files = add_prefix(position, content)

                elif choice == '3':
                    print(f"{BOLD}{CYAN}\n=== Function 3: Modify Suffix ==={RESET}")
                    new_suffix = input(f"{YELLOW}Enter new suffix (must start with ., e.g. .txt): {RESET}")
                    if not new_suffix.startswith('.'):
                        print(f"{YELLOW}Error: Suffix must start with . !{RESET}")
                        continue
                    function_name = "Modify Suffix"
                    params = {"New Suffix": new_suffix}
                    stats_file, _ = create_backup(function_name, params)
                    modified_files = modify_suffix(new_suffix)

                elif choice == '4':
                    print(f"{BOLD}{CYAN}\n=== Function 4: Add Suffix ==={RESET}")
                    position = input(f"{YELLOW}Add position (1: Before suffix 2: After suffix): {RESET}")
                    content = input(f"{YELLOW}Enter content to add (supports symbols and Emoji): {RESET}")
                    function_name = "Add Suffix"
                    params = {"Position": position, "Content": content}
                    stats_file, _ = create_backup(function_name, params)
                    modified_files = add_suffix(position, content)

                elif choice == '5':
                    print(f"{BOLD}{CYAN}\n=== Function 5: Add Header Text ==={RESET}")
                    print(f"{YELLOW}Enter text to add (type END to finish):{RESET}")
                    lines = []
                    while True:
                        line = input()
                        if line.strip().upper() == "END":
                            break
                        lines.append(line)
                    function_name = "Add Header Text"
                    params = {"Lines Added": len(lines)}
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
                    print(f"{GREEN}\nOperation complete, modified {len(modified_files)} files!{RESET}")
                else:
                    print(f"{YELLOW}\nNo operation performed, no backup generated.{RESET}")

            except Exception as e:
                print(f"{RED}Error occurred: {str(e)}{RESET}")
                import traceback
                traceback.print_exc()

            input(f"{YELLOW}Press Enter to continue...{RESET}")

    except KeyboardInterrupt:
        print(f"\n{RED}Program interrupted by user, exiting...{RESET}")
        sys.exit()
    except Exception as e:
        print(f"{RED}Fatal error occurred: {str(e)}{RESET}")
        sys.exit()

if __name__ == "__main__":
    main()