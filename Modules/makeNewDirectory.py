
import SystemNavigator
os = SystemNavigator.os
main = SystemNavigator.main()
#funtion 4
#make a new directory

def makeNewDirectory():   
    
    #make a new directory in the current working directory
    print("\033[31mWARNING! WARNING! WARNING!\033[0m")#prints warning message in red text
    print("\033[31mThis will make a new directory in your current working directory\033[0m")
    
    userChoice = str(input("\033[36mDo you wish to proceed? Yes / No : \033[0m"))
    
    userChoiceYes = ["yes", "y", "YES", "Yes","Y"]
    userChoiceNo = ["no","n", "NO", "No","N"]
    
    #if user selects yes, proceed with creating the directory
    if userChoice in userChoiceYes:
        userDirectoryInput = str(input("\033[32m" + r"Enter a new directory name: " + "\033[0m"))
        newDirectoryName = str("./"+ userDirectoryInput)
        os.makedirs(newDirectoryName, exist_ok=True)

    #if user selects no, return to main selection
    elif userChoice in userChoiceNo:
        print("You need to go back and code this option")
        main()

    