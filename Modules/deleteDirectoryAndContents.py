import SystemNavigator
shutil = SystemNavigator.shutil
main = SystemNavigator.main

#function 6
#Delete directory and its contents
def deleteDirectoryAndContents():
    #Warn user
    print("\033[31mWARNING! WARNING! WARNING!\033[0m")#prints warning message in red text
    print("\033[31mThis will delete the directory and all its contents.\033[0m")

    userChoice = str(input("\033[36mDo you wish to proceed? Yes / No : \033[0m"))
            
    userChoiceYes = ["yes", "y", "YES", "Yes"]
    userChoiceNo = ["no","n", "NO", "No","N"]
    
    #if user selects yes, proceed with creating the directory
    if userChoice in userChoiceYes:
        userDirectoryInput = str(input("\033[32m" + r"Please enter or copy / paste the path to delete the directory and its contents: " + "\033[0m"))
        newDirectoryName = str(userDirectoryInput)

        confirmDelete = str(input("this will delete the directory:" + newDirectoryName + " ,including subdirectories and their contents. Do you wish to proceed: "))
        
        confirmDeleteYes = ["yes", "y", "YES", "Yes","Y"]
        confirmDeleteNo = ["no","n", "NO", "No", "N"]

        if confirmDelete in confirmDeleteYes:
            #did you install shutil module???
            shutil.rmtree(newDirectoryName)

        elif confirmDelete in confirmDeleteNo:
            main()
    #if user selects no, return to main selection
    elif userChoice in userChoiceNo:
        main()