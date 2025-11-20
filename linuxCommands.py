#Linux System commands for system navigator
#Written by: DrSundae
#Date: 11/20/25

import os
import platform
import shutil
import subprocess
import platform
import psutil
import sys
import getpass
import SystemNavigator

#function 1 - print working directory
def printWorkingDirectory():
    print("\033[32mYour current working directory is: \033[0m") 
    print(os.getcwd()) # prints the current working directory
    print()
    print()
  
#function 2
#changes the directory and print the new working directoy for user
def changeWorkingDirectory():
    #enter the desired path
    pathInput = str(input( "\033[32m" + r"Please enter or copy / paste the desired path then press ENTER: " + "\033[0m"))
    os.chdir(pathInput)
    workingDirectory = os.getcwd()
    print("\033[32mYour new working directory is: \033[0m" + workingDirectory)
    #print(workingDirectory)
    print()


#function 3
#Print contents of the current working directory
def printDirectoryContents():
    #display directory contents if windows
    path = os.getcwd()
    print(path)
    print(os.system('ls'))
    print()
    print()

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
        SystemNavigator.main()

#function 5
#Get System Info
def displaySystemInformation():
    # Get basic system information
    print("System:", platform.system())
    print("Hostname:", platform.node())
    print("Release:", platform.release())
    print("Version:", platform.version())
    print("Machine:", platform.machine())
    print("Processor:", platform.processor())

    #Get CPU information
    cpu_info = platform.processor()
    cpu_count = psutil.cpu_count(logical=False)
    logical_cpu_count = psutil.cpu_count(logical=True)

    print("\nCPU Information:")
    print(f"Processor: {cpu_info}")
    print(f"Physical Cores: {cpu_count}")
    print(f"Logical Cores: {logical_cpu_count}")

    #Get memory information
    memory_info = psutil.virtual_memory()
    #memory_info_gb = int(memory_info / 1000000000)
    print("\nMemory Information:")
    #print(f"Total Memory (GB): {memory_info_gb} GB ")
    print(f"Total Memory: {memory_info.total} bytes")
    print(f"Available Memory: {memory_info.available} bytes")
    print(f"Used Memory: {memory_info.used} bytes")
    print(f"Memory Utilization: {memory_info.percent}%")

    #Get disk information
    disk_info = psutil.disk_usage('/')
    print("\nDisk Information:")    
    print(f"Total Disk Space: {disk_info.total} bytes")
    print(f"Used Disk Space: {disk_info.used} bytes")
    print(f"Free Disk Space: {disk_info.free} bytes")
    print(f"Disk Space Utilization: {disk_info.percent}%")

   
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
            SystemNavigator.main()
    #if user selects no, return to main selection
    elif userChoice in userChoiceNo:
        SystemNavigator.main()

#function 7 
#Remove an empty directory
def removeEmptyDirectory():
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
            SystemNavigator.main()

    #if user selects no, return to main selection
    elif userChoice in userChoiceNo:
        SystemNavigator.main()


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
        SystemNavigator.main()
  
#function 9
#Display NetworkInfomation
def displayNetworkInformation():
    data = os.system('ifconfig /all')
    print(data)
    

#function 11
#create Basic user account
def createBasicLinuxUser(self, cmd):
    username = print(input("Enter a username for the account: "))
    new_password = print(input("Enter a password for the account: "))
    
    adminpass = getpass.getpass() #ask for user's password
    try:
        subprocess.run(['useradd ',username, ' -p ', new_password ])
    except:
        print("Failed to add user. Please try again later.")
        sys.exit(1)
    
    