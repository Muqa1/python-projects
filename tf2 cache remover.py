import time
import os
import colorama
from colorama import Fore, Back, Style
colorama.init()

path = input(Fore.CYAN + "Enter your tf2 custom folder path:\n")
file_count = 0

for root, directories, files in os.walk(path):
    for file in files:
        if os.path.splitext(file)[1] == ".cache" and "\\Team Fortress 2\\tf\\" in root:
            file_count += 1
            file_path = os.path.join(root, file)
            print(Fore.YELLOW + "Deleting file:", file_path)
            os.remove(file_path)

print(Fore.GREEN + "Deleted", file_count, "files.")
time.sleep(2)
