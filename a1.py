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

def file_exists_create(dir, file):
    p = Path(dir) / file
    if p.exists():
        return True
    else:
        return False

def file_exists(file):
    p = Path(file)
    if p.exists():
        return True
    else:
        return False

def delete_file(file):
    p = Path(file)
    print(p.resolve(), "DELETED")
    p.unlink()

def read_file(file):
    p = Path(file)
    with open(p, 'r') as f:
        if f.read() == "":
            f.seek(0)
            print("EMPTY")
        else:
            f.seek(0)
            text = f.read().strip()
            print(text)

def dsu_check(file):
    My_file = Path(file)
    if My_file.suffix == ".dsu":
        return True
    else:
        return False

def run():
    action = input()
    action_list = action.split()
    if action_list[0] == "C":
        if len(action_list) == 4:
            if not directory_exists(action_list[1]):
                print("ERROR")
            else:
                file = action_list[3]
                file = file + ".dsu"
                if file_exists_create(action_list[1], file):
                    print("ERROR")
                else:
                    create_file(action_list[1], file)
        else:
            print("ERROR")

    elif action_list[0] == "D":
        if len(action_list) == 2:
            file = action_list[1]
            if dsu_check(file):
                if not file_exists(file):
                    print("ERROR")
                else:
                    delete_file(file)
            else:
                print("ERROR")
        else:
            print("ERROR")

    elif action_list[0] == "R":
        if len(action_list) == 2:
            file = action_list[1]
            if dsu_check(file):
                if not file_exists(file):
                    print("ERROR")
                else:
                    read_file(file)
            else:
                print("ERROR")
        else:
            print("ERROR")

    elif action_list[0] == "Q":
        return

    else:
        print("ERROR")
    run()

if __name__ == '__main__':

    run()
