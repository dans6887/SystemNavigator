import os
import platform
import shutil
import subprocess
import platform
import psutil
import Modules #import all your modules


systemType = platform.system()

def main():
    while True:
        
        print (f"Welcome to System Navigator for {systemType}. ")
        print ("Select a task to continue.")
        print ()
        print ("1. Print Working Directory")
        print ("2. Change Directory")
        print ("3. Display directory contents ")#NEEDS ATTENTION!!!!!
        print ("4. Make new directory")
        print ("5. Print System Information") #need expanded windows and full linux functionality
        print ("6. Remove Directory and its contents")
        print ("7. Remove an empty directory")
        print ("8. Delete a file")
        print ("9. Display Network Information")
        print ("10. Open a text editor - Coming soon")
        print ("11. Create new basic user")
        print ("12. create new admin user account")
        print ("13. Upgrade user to admin.")
        print ("700. Call a Test Function")
        print ("600. Quit ")
        print ()
        userSelect = input("Make A selection and press ENTER: ")
        print()
        
        #user enters their choice and presses ENTER
        
        
        #run selection 1-Print working directory
        if userSelect == '1':
            from Modules.PrintWorkingDirectory import printWorkingDirectory
            printWorkingDirectory()
        
        elif userSelect == '2':
            from Modules.changeWorkingDirectory import changeWorkingDirectory
            changeWorkingDirectory()
        
        elif userSelect == '3':
            from Modules.printDirectoryContents import printDirectoryContents
            printDirectoryContents()

        elif userSelect == '4':
            from Modules.makeNewDirectory import makeNewDirectory
            makeNewDirectory()
        
        elif userSelect == '5':
            from Modules.displaySystemInformation import displaySystemInformation
            displaySystemInformation()
        
        elif userSelect == '6':
            from Modules.deleteDirectoryAndContents import deleteDirectoryAndContents
            deleteDirectoryAndContents()
        
        elif userSelect == '7':
            from Modules.deleteEmptyDirectory import deleteEmptyDirectory
            deleteEmptyDirectory()
        
        #call deleteFile function
        elif userSelect == '8':
            from Modules.deleteFile import deleteFile
            deleteFile()

        #call displayNetworkInformation function
        elif userSelect == '9':
            from Modules.displayNetworkinformation import displayNetworkInformation
            displayNetworkInformation()
            
        elif userSelect == '10':
            from Modules.openTextEditor import openTextEditor
            openTextEditor()
            #linux text editor option still indevelopment
            
        elif userSelect == '11':
            from Modules.createBasicUserAccount import createBasicUserAccount
            createBasicUserAccount()
            
        elif userSelect == '12'    :
            from Modules.createAdminUserAccount import createAdminAccount
            createAdminAccount()
            
        elif userSelect == '13':
            from Modules.upgradeUserToAdmin import upgradeUserToAdmin
            upgradeUserToAdmin()
                   
        #exit Program
        elif userSelect == '600':
            return False
        
        
        
        #Ignore invalid entry
        else:
            print("Invalid selection. Please try again \n")
            print()
            
            
if __name__ == "__main__":
    main()