from os import system, name
import time

def clear():  
    if name == 'nt': 
        _ = system('cls')

clear()

def run():
    clear() 
    
    print("*"*10)
    print("\nCOMMANDS\n")
    print("ls - list current passwords\na - add new password\nq - quit\n")
    print("*"*10)
   
    cmd = ""

    while cmd != "q": 
        cmd = input("\nWhat do you want to do?: ")

        if cmd == "ls":
            with open("list.txt", "r") as fl:
                content = fl.read() 
                print("\n" + content)
            print()
        elif cmd == "a":
            with open("list.txt", "a") as f:
                print()
                newsite = input("Enter a new website: ")
                newusr = input("Enter the new username: ")
                newps = input("Enter the new password: ")
                f.write(f"\n{newsite}\n{newusr}\n{newps}")
            print()
        if cmd not in "qals":
            print("Unknown command entered. Quitting program in 5 seconds")
            time.sleep(5)
            quit()
    clear()
    quit()


run()
