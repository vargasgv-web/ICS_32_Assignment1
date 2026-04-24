# a1.py

# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Victor Vargas Gonzalez
# vargasgv@uci.edu
# 49403244
from pathlib import Path


def create_file(dir, file):
    p = Path(dir) / file
    p.touch()
    print(p.resolve())

def directory_exists(dir):
    p = Path(dir)
    if p.exists():
        return True
    else:
        return False

def file_exists(dir, file):
    p = Path(dir) / file
    if p.exists():
        return True
    else:
        return False

def file_exists2(file):
    p = Path(file)
    if p.exists():
        return True
    else:
        return False

def delete_file(file):
    p = Path(file)
    print(p.resolve(), "DELETED")
    p.unlink()

def read_file(dir, file):
    p = Path(dir) / file
    with open(p, 'r') as f:
        if not f.read(1):
            print('EMPTY')
        else:
            f.seek(0)
            print(f.read())

def dsu_check(file):
    My_file = Path(file)
    if My_file.suffix == ".dsu":
        return True
    else:
        return False

def run():
    action = input("Enter your file command (Q to exit): ")
    action_list = action.split()

    if action_list[0] == "C":
        if len(action_list) == 4:
            if not directory_exists(action_list[1]):
                print("ERROR: directory does not exist")
            else:
                file = action_list[3]
                file = file + ".dsu"
                if file_exists(action_list[1], file):
                    print("ERROR: File already exists")
                else:
                    create_file(action_list[1], file)
        else:
            print("ERROR: incorrect format for C")

    elif action_list[0] == "D":
        if len(action_list) == 2:
            file = action_list[1]
            if dsu_check(file):
                if not file_exists2(file):
                    print("ERROR: File does not exists")
                else:
                    delete_file(file)
            else:
                print("ERROR: not a dsu file")
        else:
            print("ERROR: incorrect format for D")

    elif action_list[0] == "R":
        dir = input("Please enter the directory name: ")
        if not directory_exists(dir):
            print("ERROR: Directory does not exist")
        else:
            file = input("Please enter the file name: ")
            file = file + ".dsu"
            if not file_exists(dir, file):
                print("ERROR: File does not exists")
            else:
                read_file(dir, file)

    elif action_list[0] == "Q":
        print("Exiting file explorer")
        return

    else:
        print("ERROR: Not an available command")
    run()

if __name__ == '__main__':

    #print("Welcome to this basic file explorer! \n")
    run()
