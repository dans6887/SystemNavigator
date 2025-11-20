import os
import platform
import shutil
import subprocess

import platform
import psutil
import linuxCommands
import windowsCommands

def main():
    systemType = platform.system()
    
    while True:
        ######################################################################       
        #if the system is Windows based load the choices for Windows systems.#
        ######################################################################
        if systemType == 'Windows': #if windows system
            print (f"Welcome to System Navigator for {systemType}. ")
            print ("Select a task to continue.")
            print ()
            print ("1. Print Working Directory")
            print ("2. Change Directory")
            print ("3. Display directory contents ")#NEEDS ATTENTION!!!!!
            print ("4. Make new directory")
            print ("5. Print System Information") #need exapanded windows and full linux functionality
            print ("6. Remove Directory and its contents")
            print ("7. Remove an empty directory")
            print ("8. Delete a file")
            print ("9. Display Network Information")
            print ("10. Open a text editor - Coming soon")
            print ("11. Create new basic user")
            print ("12. create new admin user account")
            print ("700. Call a Test Function")
            print ("600. Quit ")
            print ()
            
            #user enters their choice and presses ENTER
            userSelect = input("Make A selection and press ENTER: ")
            print()
            
            #run selection 1-Print working directory
            if userSelect == '1':
                windowsCommands.printWorkingDirectory()
            
            #change directory and display new working path
            elif userSelect == '2':
                windowsCommands.changeWorkingDirectory()

            #display directory contents (windows)
            elif userSelect == '3':
                windowsCommands.printDirectoryContents()

            #make a new directory
            elif userSelect == '4':
                windowsCommands.makeNewDirectory()

            #Print System Information (windows)
            elif userSelect == '5':
                windowsCommands.displaySystemInformation()

            #call deleteDirectoryAndContents function
            elif userSelect == '6':
                windowsCommands.deleteDirectoryAndContents()
            
            #remove an empty directory
            elif userSelect == '7':
                windowsCommands.removeEmptyDirectory()

            #call deleteFile function
            elif userSelect == '8':
                windowsCommands.deleteFile()

            #call displayNetworkInformation function
            elif userSelect == '9':
                windowsCommands.displayNetworkInformation
            
            elif userSelect == '10':
                windowsCommands.openTextEditor()
                
            elif userSelect == '11':
                windowsCommands.createBasicUser()
            elif userSelect == '12'    :
                windowsCommands.createAdminUser()
            
            #call a test function
            elif userSelect == '700':
                windowsCommands.testFunction()
        
            #exit Program
            elif userSelect == '600':
                return False
            
            elif userSelect =='800':
                windowsCommands.openShellPrompt()

            #Ignore invalid entry
            else:
                print("Invalid selection. Please try again \n")
                print()
                
                
        ##################################################################       
        #if the system is linux based load the choices for linux systems.#
        ##################################################################  
        elif systemType == 'Linux': #if linux system            
            print (f"Welcome to System Navigator for {systemType}. ")
            print ("Select a task to continue.")
            print()
            print ("1. Print Working Directory")
            print ("2. Change Directory")
            print ("3. Display directory contents ")
            print ("4. Make new directory")
            print ("5. Print System Information ")
            print ("6. Remove Directory and its contents")
            print ("7. Remove an empty directory")
            print ("8. Delete a file")
            print ("9. Display Network Information")
            print ("10. Open a text editor - Coming soon")
            print ("11. Create a new basic linux user")
            print ("12. Update user account password")
            print ("13. Upgrade user to admin.")
            print ("700. Call a Test Function")
            print ("600. Quit ")
            print()
            
            #user enters their choice and presses ENTER
            userSelect = input("Make A selection and press ENTER: ")
            print()
            
            #run selection 1-Print working directory
            if userSelect == '1':
                linuxCommands.printWorkingDirectory()
            
            #change directory and display new working path
            elif userSelect == '2':
                linuxCommands.changeWorkingDirectory()

            #display directory contents (windows)
            elif userSelect == '3':
                linuxCommands.printDirectoryContents()

            #make a new directory
            elif userSelect == '4':
                linuxCommands.makeNewDirectory()

            #Print System Information (windows)
            elif userSelect == '5':
                linuxCommands.displaySystemInformation()

            #call deleteDirectoryAndContents function
            elif userSelect == '6':
                linuxCommands.deleteDirectoryAndContents()
            
            #remove an empty directory
            elif userSelect == '7':
                linuxCommands.removeEmptyDirectory()

            #call deleteFile function
            elif userSelect == '8':
                linuxCommands.deleteFile()

            #call displayNetworkInformation function
            elif userSelect == '9':
                linuxCommands.displayNetworkInformation
            
            elif userSelect == '10':
                linuxCommands.openTextEditor()
            elif userSelect == '11':
                linuxCommands.createBasicLinuxUser()
            
            #call a test function
            elif userSelect == '700':
                linuxCommands.testFunction()
        
            #exit Program
            elif userSelect == '600':
                return False
            
            elif userSelect =='800':
                linuxCommands.openShellPrompt()
            
if __name__ == "__main__":
    main()