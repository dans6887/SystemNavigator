import SystemNavigator
os = SystemNavigator.os
main = SystemNavigator.main

#function 7 
#Remove an empty directory
def deleteEmptyDirectory():
    print("\033[31mWARNING! WARNING! WARNING!\033[0m")#prints warning message in red text
    print("\033[31mThis will delete the directory.\033[0m")

    userChoice = str(input("\033[36mDo you wish to proceed? Yes / No : \033[0m"))

    userChoiceYes = ["yes", "y", "YES", "Yes"]
    userChoiceNo = ["no","n", "NO", "No","N"]

    #confirm user's choice to delete the directory
    if userChoice in userChoiceYes:
        userDirectoryInput = str(input("\033[32m" + r"Please enter or copy / paste the path to delete the directory: " + "\033[0m"))
        pathNoQuotes = userDirectoryInput.replace('"',"")


        confirmDelete = str(input("\033[36mThis will delete the directory: \033[0m" + pathNoQuotes + "\033[36m \nDo you wish to proceed: \033[0m"))
        
        confirmDeleteYes = ["yes", "y", "YES", "Yes","Y"]
        confirmDeleteNo = ["no","n", "NO", "No", "N"]

        #give the user one last chance to change their mind
        if confirmDelete in confirmDeleteYes:
            if os.path.exists(pathNoQuotes) and not os.path.isfile(pathNoQuotes):#check the directory exists and is not a file
                #check if the directory is empty
                if not os.listdir(pathNoQuotes):
                    os.rmdir(pathNoQuotes)#delete the directory if it is empty
                    print("The directory "+ pathNoQuotes + " has been removed")
                    print()
                else:
                    #End function if directory is not empty
                    print("The directory is not empty")
                    print()
            else:
                #return to the main menu if the path is a file or not a valid directory
                print("The path is either a file or not valid")
                print()

        elif confirmDelete in confirmDeleteNo:#return to main menue if user changes their mind
            main()

    #if user selects no, return to main selection
    elif userChoice in userChoiceNo:
        main()
