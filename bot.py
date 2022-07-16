import pyautogui
import time
import sys

def repeat():
    if(arg2 == None):
        a = int(input("Amount to spam: "))
    else:
        a = int(arg2)
    
    if(arg3 == None):
        s = 0.5
    else:
        print("Changing the speed can get you banned on some platforms we do not condone this")
        yn = input("Continue, [y,n]: ")
        if(yn == "y"):
            s = float(arg3)
        else:
            quit()

    t = f.readline()
    
    print("5")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("Starting spamming")
    

    for i in range(a):
        pyautogui.typewrite(t)
        pyautogui.press("enter")
        time.sleep(s)

def multiline():
    if(arg2 == None):
        s = 0.5
    else:
        print("Changing the speed can get you banned on some platforms we do not condone this")
        yn = input("Continue, [y,n]: ")
        if(yn == "y"):
            s = float(arg2)
        else:
            quit()

    print("5")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("Starting spamming")
    
    for line in f:
        pyautogui.typewrite(line)
        pyautogui.press("enter")
        time.sleep(s)

f = open("spam.txt", "r")
arg2 = None
arg3 = None

try:
    type_input = sys.argv[1]
except:
    print("No input,  prompting input.")
    type_input = "-" + input("Mode select. Multiline, Repeat or chose help. [m,r,h]: ")

try:
    arg2 = sys.argv[2]
except:
    print("No seccond argument")

try:
    arg3 = sys.argv[3]
except:
    print("No third argument")

if(type_input == "-h"):
    print("Multiline types everyline in spam.txt once then hits enter then stops. Repeat types the first line then hits enter the amount of times you specify")
elif(type_input == "-r"):
    repeat()
elif(type_input== "-m"):
    multiline()
else:
    print("error incorect mode")
