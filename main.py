import os
import os.path
import sys

from colorama import init, Fore, Back, Style

def lock(file_path):
    """Encrypts a file by flipping bits and adding .lock extension."""
    if not os.path.exists(file_path):
        print(Style.BRIGHT + Fore.RED + f"<Error> File '{file_path}' not found.")
        return

    if file_path.endswith('.lock'):
        print(Fore.WHITE + f"<Skip> '{file_path}' is already locked.")
        return

    try:
        with open(file_path, 'rb') as f:
            data = f.read()

        # Bitwise NOT operation
        processed_data = bytearray(~b & 0xFF for b in data)

        with open(file_path, 'wb') as f:
            f.write(processed_data)

        new_path = file_path + '.lock'
        os.rename(file_path, new_path)
        print(Style.BRIGHT + Fore.GREEN + f"<Locked> {file_path} --> {new_path}")

    except Exception as e:
        print(Style.BRIGHT + Fore.RED + f"<Lock Error> {e}")

def unlock(file_path):
    """Decrypts a .lock file by flipping bits and removing the extension."""
    if not os.path.exists(file_path):
        print(Style.BRIGHT + Fore.RED + f"<Error> File '{file_path}' not found.")
        return

    if not file_path.endswith('.lock'):
        print(Fore.WHITE + f"<Skip> '{file_path}' is not a .lock file.")
        return

    try:
        with open(file_path, 'rb') as f:
            data = f.read()

        # Bitwise NOT operation (returns to original)
        processed_data = bytearray(~b & 0xFF for b in data)

        with open(file_path, 'wb') as f:
            f.write(processed_data)

        new_path = file_path[:-5]
        os.rename(file_path, new_path)
        print(Style.BRIGHT + Fore.GREEN + f"<Unlocked> {file_path} --> {new_path}")

    except Exception as e:
        print(Style.BRIGHT + Fore.RED + f"<Unlock Error> {e}")

def walkFiles(path):
    print(Fore.WHITE + f"Scaning directory {path} ...")
    temp_file = []

    for root, dirs, files in os.walk(path):

        for f in files:
            print(Style.BRIGHT + Fore.BLACK + f"<Scanned> File {os.path.join(root, f)} scanned.")
            temp_file.append(os.path.join(root, f))
       
    print(Fore.WHITE + f"Directory {path} scanned.")
    return temp_file

def lockDir(dir):
    dir_path = dir
    if not(os.path.isdir(dir_path)):
        print(Style.BRIGHT + Fore.RED + f"<Error> Directory {dir_path} not found.")
        return
    
    # lock dir here
    files = walkFiles(dir_path)
    for i in range(len(files)):
        lock(files[i])

def unlockDir(dir):
    dir_path = dir
    if not(os.path.isdir(dir_path)):
        print(Style.BRIGHT + Fore.RED + f"<Error> Dir {dir_path} not found.")
        return
    
    # lock dir here
    files = walkFiles(dir_path)
    for i in range(len(files)):
        unlock(files[i])

def instroduce():
    print(Fore.LIGHTRED_EX + "<< Dir Locker >>")
    print(Style.BRIGHT + Fore.BLACK + \
"""
--Name: Dir Locker
--Function: Lock or Unlock a specified directory.
--Version: v1.0.0
--Designer: Coder
""")
    print(Fore.RED + "<!> Please ensure that the following operations are performed with the consent of the computer owner.")
    print(Fore.RED + "<!> We are not responsible for any errors that may occur.\n")

def main():
    init(autoreset=True)
    instroduce()
    print()
    print(Fore.WHITE + "." * 20)
    print(Fore.CYAN + "Press [Enter] key to continue > ", end = '')
    input()
    os.system("cls")
    instroduce()
    print(Fore.CYAN + "Enter a directory path > ", end = '')
    path = input()
    print("\n")
    work = ""
    while work == "":
        print(Fore.CYAN + "Select work: [0]Lock / [1]Unlock > ", end = '')
        work = input()
        if work == "0" or work == "1":
            break
        else:
            work = ""
    if work == "0":
        lockDir(path)
    else:
        unlockDir(path)

    print("\n")
    print(Fore.WHITE + "[Work finished.]")
    print(Fore.CYAN + "Press [Enter] key to colse > ", end = '')
    input()
    sys.exit()

if __name__ == "__main__":
    main()