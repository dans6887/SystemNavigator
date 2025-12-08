
import SystemNavigator
os = SystemNavigator.os
#function 2
#changes the directory and print the new working directoy for user


def changeWorkingDirectory():
    if os == 'Windows':
        #enter the desired path
        pathInput = str(input( "\033[32m" + r"Please enter or copy / paste the desired path then press ENTER: " + "\033[0m"))
        os.chdir(pathInput)
        workingDirectory = os.getcwd()
        print("\033[32mYour new working directory is: \033[0m" + workingDirectory)
        #print(workingDirectory)
        print()
    
    elif os == 'Linux':
    
        #enter the desired path
        pathInput = str(input( "\033[32m" + r"Please enter or copy / paste the desired path then press ENTER: " + "\033[0m"))
        os.chdir(pathInput)
        workingDirectory = os.getcwd()
        print("\033[32mYour new working directory is: \033[0m" + workingDirectory)
        #print(workingDirectory)
        print()