from termcolor import colored
import os.path

def write_to_file(file_with_targets, value):
    if os.path.isdir(value) or os.path.isfile(value) == True:
        file_with_targets.write(value)
    else:
        print(colored("This directory/file doesn't exist", "red"))

    

def create_folder_paths():
    if os.path.isfile("paths_to_targets.txt"):
        file_with_targets = open("paths_to_targets.txt", "w")
    else:
        file_with_targets = open("paths_to_targets.txt", "x")

    print(colored("Please enter the paths to folder/file you want to backup with root(/) path:", "magenta"))
    file_path = input()
    write_to_file(file_with_targets, file_path)
    while True:
        print(colored("If you want to add one more path, please write it, if no - just Enter", "magenta"))
        decision = input()
        if decision != '':
            write_to_file(file_with_targets, decision)
        else:
            print(colored("Your backup targets was successfully writed", "green"))
            file_with_targets.close()
            break

create_folder_paths()