import os
from colorama import Fore, Back
import json

i =1

def main():
    print("""Choose your options:
        1. Add a task ( ➕ )
        2. Remove a task ( ➖ )
        3. Show all tasks ( 👁‍🗨 )
        4. Exit (🏃)""")
    opt = input("Your options is: ")
    if opt == "1":
        add_task()
    elif opt == "2":
        remove_task()
    elif opt == "3":
        show_task()
    elif opt == "4":
        exit()
    else:
        print("Invalid option")
        return main()

def add_task():
    print("Type here to input your task(required): ")
    task = input(">: ")
    if task == "" or task == " ":
        print("Task cannot be empty")
        return add_task()
    time = input("Time(required): ")
    if time == "" or time == " ":
        print("Time cannot be empty")
        return add_task()
    AMORPM = input("AM/PM: ")
    if AMORPM == "" or AMORPM == " ":
        print("AM/PM cannot be empty")
        return add_task()
    elif AMORPM == "am":
        amorpm = AMORPM.upper()
    if AMORPM == "pm":
        amorpm = AMORPM.upper()
    elif AMORPM == "AM" or AMORPM == "PM":
        amorpm = AMORPM
    tags = input("Tags?: ")
    content = input("Decription?: ")

    
    works = { f"{tags}": {"name": task, "time": f"{time}{amorpm}","description": content} }

    with open("work.json", "r") as f:
        file_add = json.load(f)
    with open("work.json", "w") as f:
        file_add.update(works)
        json.dump(file_add, f)
    print(f"Task {task} was added! If you want to delete it, type '{Fore.RED}{tags}{Fore.RESET}' in the remove task option. \nYou can check your task at the show all task option(Option number 3).")
    return main()

def remove_task():
    rm_task = input("Type the tags of the task you want to remove: ")
    with open("work.json", "r") as f:
        file_rm = json.load(f)
    if rm_task == "" or rm_task == " ":
        print("Tags cannot be empty")
        return remove_task()
    elif rm_task not in file_rm:
        print("Tags not found")
        return remove_task()
    elif rm_task in file_rm:
        del file_rm[rm_task]
        with open("work.json", "w") as f:
            json.dump(file_rm, f)
        os.system("clear")
        print(f"Task '{Fore.RED}{rm_task}{Fore.RESET}' was successfully removed!")
        return main()

def show_task():
    with open("work.json", "r") as f:
        file_show = json.load(f)
    for key, value in file_show.items():
        print("                                                                     ") 
        print(f"    {value['name']}('{key}')({value['time']}): {value['description']}")

if __name__ == "__main__":
    main()