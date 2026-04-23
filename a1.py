# a1.py

# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Victor Vargas Gonzalez
# vargasgv@uci.edu
# 49403244

from pathlib import Path



def create_file(dir, file):
    file = file
    p = Path(dir) / file
    p.touch()
    print(p.resolve())

def create_directory(dir):
    p = Path(dir)
    p.mkdir(parents=True)

def directory_exists(dir):
    p = Path(dir)
    if p.exists():
        return True
    else:
        return False

def file_exists(dir, file):
    p = Path(dir).joinpath(file)
    if p.exists():
        return True
    else:
        return False

def run():
    action = input("Please enter an action (Enter C to create a new file, D to delete a file, "
                   "R to read a file, or Q to quit): ")
    if action == "C":
        dir = input("Please enter the directory name: ")
        if not directory_exists(dir):
            print("Error: Directory does not exist")
        else:
            file = input("Please enter the file name: ")
            file = file + ".dsu"
            if file_exists(dir, file):
                print("Error: File already exists")
            else:
                create_file(dir, file)

    elif action == "D":
        pass
    elif action == "R":
        pass
    elif action == "Q":
        print("Exiting file explorer")
        return
    else:
        print("Invalid action")
    run()

if __name__ == '__main__':

    print("Welcome to this basic file explorer! \n")
    run()
