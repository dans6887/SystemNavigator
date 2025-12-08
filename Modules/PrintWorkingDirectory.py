
import SystemNavigator 
systemType = SystemNavigator.platform.system()
os = SystemNavigator.os
#function 1 - print working directory

def printWorkingDirectory():
    if systemType == 'Windows': #if windows system
        
        print("\033[32mYour current working directory is: \033[0m") 
        print(os.getcwd()) # prints the current working directory
        print()
        print()
    elif systemType == 'Linux':
        
        print("\033[32mYour current working directory is: \033[0m") 
        print(os.getcwd()) # prints the current working directory
        print()
        print()
        