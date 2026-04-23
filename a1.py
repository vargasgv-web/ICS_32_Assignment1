# a1.py

# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Victor Vargas Gonzalez
# vargasgv@uci.edu
# 49403244

from pathlib import Path

def run():
    action = input("Please enter an action (enter C to create a new file, D to delete a file, "
                   "R to read a file, or Q to quit): ")
    if action == "C":
        pass
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
