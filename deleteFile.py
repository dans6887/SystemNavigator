
import SystemNavigator
os = SystemNavigator.os
main = SystemNavigator.main

#function 8
#delete a file

def deleteFile():
    filepath = str(input("Enter or copy / paste the path to the file you want to delete: "))
    newFilePath = filepath.replace('"',"")
    print("\033[31mWARNING! WARNING! WARNING!\033[0m")#prints warning message in red text
    print("\033[31mThis will permanently delete the file at  \033[0m" + newFilePath )

    userChoice = str(input("\033[36mDo you wish to proceed? Yes / No : \033[0m"))

    userChoiceYes = ["yes", "y", "YES", "Yes"]
    userChoiceNo = ["no","n", "NO", "No","N"]

    

    #if user selects yes, proceed with creating the directory
    if userChoice in userChoiceYes:
        if os.path.exists(newFilePath):
            os.remove(newFilePath)
            print()
        else:
            print("The file does not exist") 
            print()   

        
    #if user selects no, return to main selection
    elif userChoice in userChoiceNo:
        main()