
import SystemNavigator

#function 3
#Print contents of the current working directory
def printDirectoryContents():
    #display directory contents if windows
    
    path = SystemNavigator.os.getcwd()
    print(path)
    print(SystemNavigator.os.system('dir'))
    print()
    print()