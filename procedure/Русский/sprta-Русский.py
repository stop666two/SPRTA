# -*- coding: utf-8 -*-
import os
import shutil
import datetime
import sys

# ANSI Цветовые коды
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"

# Информация о программе
PROGRAM_NAME = "SPRTA"
FULL_NAME = "Stop666-Python-Rename-Tool-Android"
AUTHOR = "stop666two"
EMAIL = "stop666bilibili@gmail.com"
REPO_URL = "https://github.com/stop666two/SPRTA"
VERSION = "1.0.0"
COPYRIGHT = "Бесплатное программное обеспечение, запрещено перепродажа."

def clear_screen():
    """Очистка экрана (кроссплатформенная)"""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_welcome():
    """Приветственное сообщение"""
    clear_screen()
    print(f"{BOLD}{CYAN}{'='*40}{RESET}")
    print(f"{BOLD}{CYAN}  SPRTA - Инструмент переименования файлов  {RESET}")
    print(f"{BOLD}{CYAN}{'='*40}{RESET}")
    print(f"{GREEN}Полное имя: {FULL_NAME}{RESET}")
    print(f"{GREEN}Автор: {AUTHOR}{RESET}")
    print(f"{GREEN}Email: {EMAIL}{RESET}")
    print(f"{GREEN}Репозиторий: {REPO_URL}{RESET}")
    print(f"{GREEN}Версия: {VERSION}{RESET}")
    print(f"{RED}{COPYRIGHT}{RESET}")

def show_disclaimer():
    """Показать отказ от ответственности"""
    clear_screen()
    print(f"{BOLD}{CYAN}===== Отказ от ответственности ====={RESET}")
    print("Программа предоставляется «как есть», без гарантий.")
    print("Автор не несет ответственности за потерю данных.")
    print(f"{COPYRIGHT}")
    choice = input(f"{YELLOW}Введите 'y' чтобы принять, любую другую клавишу для выхода: {RESET}").lower()
    if choice != 'y':
        sys.exit()

def create_backup(function_name, params):
    """Создание резервной копии и лог-файла"""
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
            f.write(f"Время резервного копирования: {now}\n")
            f.write(f"Функция: {function_name}\n")
            f.write("Параметры:\n")
            for key, value in params.items():
                f.write(f"  {key}: {value}\n")
            f.write("Измененные файлы:\n")
            f.write("(Сгенерировано после операции)\n")
            f.write(f"Репозиторий: {REPO_URL}\n")
            f.write(f"Автор: {AUTHOR}\n")
            f.write(f"Email: {EMAIL}\n")
            f.write(f"Версия: {VERSION}\n")
            f.write(f"{COPYRIGHT}\n")
        return stats_file, backed_up
    except Exception as e:
        print(f"{RED}Ошибка создания резервной копии: {str(e)}{RESET}")
        return None, []

def update_stats(stats_file, modified_files):
    """Обновление лога операций"""
    try:
        if not stats_file or not os.path.exists(stats_file):
            return
        with open(stats_file, 'a', encoding='utf-8') as f:
            f.write("\nИзмененные файлы:\n")
            if not modified_files:
                f.write("  Ни один файл не изменён\n")
            else:
                for old, new in modified_files:
                    f.write(f"  {old} -> {new}\n")
    except Exception as e:
        print(f"{RED}Ошибка обновления лога: {str(e)}{RESET}")

def get_function_description():
    """Описание функций"""
    return {
        '1': "Изменить префикс: заменить весь префикс имени файла",
        '2': "Добавить префикс: добавить содержимое до или после существующего префикса",
        '3': "Изменить суффикс: заменить весь суффикс на новый",
        '4': "Добавить суффикс: добавить содержимое до или после существующего суффикса",
        '5': "Добавить заголовок: добавить несколько строк текста в начало файла",
        '6': "Показать информацию об авторе",
        '7': "Показать информацию о программе",
        '8': "Выход из программы"
    }

def main_menu():
    """Главное меню"""
    while True:
        clear_screen()
        print(f"{BOLD}{CYAN}===== SPRTA - Инструмент переименования файлов ====={RESET}")
        print(f"{GREEN}Полное имя: {FULL_NAME}{RESET}")
        print(f"{GREEN}Версия: {VERSION}{RESET}")
        print(f"{GREEN}Автор: {AUTHOR}{RESET}")
        print(f"{GREEN}Email: {EMAIL}{RESET}")
        print(f"{GREEN}Репозиторий: {REPO_URL}{RESET}")
        print(f"{YELLOW}{COPYRIGHT}{RESET}")
        print(f"{YELLOW}Выберите операцию из следующих вариантов:{RESET}")

        descriptions = get_function_description()
        for i in range(1, 9):
            print(f"{i}. {descriptions[str(i)]}")

        choice = input(f"{YELLOW}Введите опцию (1-8): {RESET}").strip()
        if choice in [str(i) for i in range(1, 9)]:
            if choice == '8':
                print(f"{GREEN}Спасибо за использование SPRTA, до свидания!{RESET}")
                sys.exit()
            return choice
        print(f"{YELLOW}Неверный ввод, попробуйте снова!{RESET}")

def modify_prefix(new_prefix):
    """Изменить префикс"""
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
                print(f"{YELLOW}Не удалось переименовать {filename}: {str(e)}{RESET}")
    return modified

def add_prefix(position, content):
    """Добавить префикс"""
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
                print(f"{YELLOW}Не удалось переименовать {filename}: {str(e)}{RESET}")
    return modified

def modify_suffix(new_suffix):
    """Изменить суффикс"""
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
                print(f"{YELLOW}Не удалось переименовать {filename}: {str(e)}{RESET}")
    return modified

def add_suffix(position, content):
    """Добавить суффикс"""
    modified = []
    for filename in os.listdir():
        if any([
            filename.startswith('backup_'),
            filename == os.path.basename(__file__),
            os.path.isdir(filename)
        ]):
            continue
        root, ext = os.path.splitext(filename)
        if position == '1':  # До суффикса
            new_name = f"{root}{content}{ext}"
        else:  # После суффикса
            if ext:
                new_name = f"{root}{ext}{content}"
            else:
                new_name = f"{filename}{content}"
        if new_name != filename:
            try:
                os.rename(filename, new_name)
                modified.append((filename, new_name))
            except Exception as e:
                print(f"{YELLOW}Не удалось переименовать {filename}: {str(e)}{RESET}")
    return modified

def add_prefix_text(lines):
    """Добавить несколько строк в начало файла"""
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
            print(f"{YELLOW}Ошибка обработки файла {filename}: {str(e)}{RESET}")
    return modified

def show_author():
    """Показать информацию об авторе"""
    clear_screen()
    print(f"{BOLD}{CYAN}===== Информация об авторе ====={RESET}")
    print(f"{GREEN}Автор: {AUTHOR}{RESET}")
    print(f"{GREEN}Email: {EMAIL}{RESET}")
    print(f"{GREEN}Репозиторий: {REPO_URL}{RESET}")
    print(f"{GREEN}Версия: {VERSION}{RESET}")
    print(f"{YELLOW}{COPYRIGHT}{RESET}")
    input(f"{YELLOW}Нажмите Enter для возврата...{RESET}")

def show_about():
    """Показать информацию о программе"""
    clear_screen()
    print(f"{BOLD}{CYAN}===== О программе SPRTA ====={RESET}")
    print("Это мощный инструмент для переименования файлов")
    print("Поддерживает 5 режимов переименования и систему резервного копирования")
    print("Функции:")
    print("- Полная система резервного копирования")
    print("- Поддержка специальных символов и Emoji")
    print("- Подробные логи операций")
    print("- Открытое ПО, запрещена перепродажа")
    print(f"{YELLOW}Автор: {AUTHOR}{RESET}")
    print(f"{YELLOW}Email: {EMAIL}{RESET}")
    print(f"{YELLOW}Репозиторий: {REPO_URL}{RESET}")
    input(f"{YELLOW}Нажмите Enter для возврата...{RESET}")

def main():
    """Основная программа"""
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
                    print(f"{BOLD}{CYAN}\n=== Функция 1: Изменить префикс ==={RESET}")
                    new_prefix = input(f"{YELLOW}Введите новый префикс (поддерживает символы и Emoji): {RESET}")
                    function_name = "Изменить префикс"
                    params = {"Новый префикс": new_prefix}
                    stats_file, _ = create_backup(function_name, params)
                    modified_files = modify_prefix(new_prefix)

                elif choice == '2':
                    print(f"{BOLD}{CYAN}\n=== Функция 2: Добавить префикс ==={RESET}")
                    position = input(f"{YELLOW}Позиция добавления (1: перед префиксом 2: после префикса): {RESET}")
                    content = input(f"{YELLOW}Введите содержимое для добавления (поддерживает символы и Emoji): {RESET}")
                    function_name = "Добавить префикс"
                    params = {"Позиция": position, "Содержимое": content}
                    stats_file, _ = create_backup(function_name, params)
                    modified_files = add_prefix(position, content)

                elif choice == '3':
                    print(f"{BOLD}{CYAN}\n=== Функция 3: Изменить суффикс ==={RESET}")
                    new_suffix = input(f"{YELLOW}Введите новый суффикс (должен начинаться с ., например .txt): {RESET}")
                    if not new_suffix.startswith('.'):
                        print(f"{YELLOW}Ошибка: суффикс должен начинаться с . !{RESET}")
                        continue
                    function_name = "Изменить суффикс"
                    params = {"Новый суффикс": new_suffix}
                    stats_file, _ = create_backup(function_name, params)
                    modified_files = modify_suffix(new_suffix)

                elif choice == '4':
                    print(f"{BOLD}{CYAN}\n=== Функция 4: Добавить суффикс ==={RESET}")
                    position = input(f"{YELLOW}Позиция добавления (1: перед суффиксом 2: после суффикса): {RESET}")
                    content = input(f"{YELLOW}Введите содержимое для добавления (поддерживает символы и Emoji): {RESET}")
                    function_name = "Добавить суффикс"
                    params = {"Позиция": position, "Содержимое": content}
                    stats_file, _ = create_backup(function_name, params)
                    modified_files = add_suffix(position, content)

                elif choice == '5':
                    print(f"{BOLD}{CYAN}\n=== Функция 5: Добавить заголовок ==={RESET}")
                    print(f"{YELLOW}Введите текст для добавления (введите END для завершения):{RESET}")
                    lines = []
                    while True:
                        line = input()
                        if line.strip().upper() == "END":
                            break
                        lines.append(line)
                    function_name = "Добавить заголовок"
                    params = {"Добавлено строк": len(lines)}
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
                    print(f"{GREEN}\nОперация завершена, изменено {len(modified_files)} файлов!{RESET}")
                else:
                    print(f"{YELLOW}\nОперация не выполнена, резервная копия не создана.{RESET}")

            except Exception as e:
                print(f"{RED}Произошла ошибка: {str(e)}{RESET}")
                import traceback
                traceback.print_exc()

            input(f"{YELLOW}Нажмите Enter для продолжения...{RESET}")

    except KeyboardInterrupt:
        print(f"\n{RED}Программа прервана пользователем, выход...{RESET}")
        sys.exit()
    except Exception as e:
        print(f"{RED}Произошла критическая ошибка: {str(e)}{RESET}")
        sys.exit()

if __name__ == "__main__":
    main()