import os
import sys
from colorama import Fore, Style

def print_tree(path, level=0):
    
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            print(f"{level*'  '} {Fore.BLUE}{entry}{Style.RESET_ALL}/")
            print_tree(full_path, level + 1)
        else:
            print(f"{level*'  '} {Fore.GREEN}{entry}{Style.RESET_ALL}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Неправильна кількість аргументів.")
        sys.exit(1)

    directory = sys.argv[1]
    try:
        print_tree(directory)
    except FileNotFoundError:
        print(f"Директорія {directory} не знайдена.")
