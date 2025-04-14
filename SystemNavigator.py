#System Navigator
#created by: Daniel Scott
#Date: 4/10/25
#Note: Incomplete version. submitted for final project on Codedex.

import os
import platform
import shutil
import subprocess

import platform
import psutil





#Function 1
#print the working directory
def printWorkingDirectory():
    print("\033[32mYour current working directory is: \033[0m") 
    print(os.getcwd()) # prints the current working directory
    print()
    print()
    #return False

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
    systemType = platform.system()
    if systemType == "Windows":
        path = os.getcwd()
        print(path)
        print(os.system('dir'))
        print()
        print()
    elif systemType == "Linux":
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
        main()

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

    #Get GPU information
    #gpus = GPUtil.getGPUs()

    #if not gpus:
     #   print("No GPU detected.")
    #else:
     #   for i, gpu in enumerate(gpus):
      #      print(f"\nGPU {i + 1} Information:")
       #     print(f"ID: {gpu.id}")
        #    print(f"Name: {gpu.name}")
         #   print(f"Driver: {gpu.driver}")
         #   print(f"GPU Memory Total: {gpu.memoryTotal} MB")
        #  print(f"GPU Memory Free: {gpu.memoryFree} MB")
         #   print(f"GPU Memory Used: {gpu.memoryUsed} MB")
          #  print(f"GPU Load: {gpu.load * 100}%")
           # print(f"GPU Temperature: {gpu.temperature}°C")

    print()

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
            main()

    #if user selects no, return to main selection
    elif userChoice in userChoiceNo:
        main()


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


#function 9
#Display NetworkInfomation
def displayNetworkInformation():
    systemType = platform.system()
    if systemType == "Windows":
        data = subprocess.check_output(['ipconfig', '/all']).decode('utf-8').split('\n')
        for item in data: 
            print(item.split('\r')[:-1])
        print()
    elif systemType == "Linux":
        print()

#Function 10
#open a text Editor
def openTextEditor():
    print("Coming Soon")


#function 700
#run a test function
def testFunction():
    print("Hello I am here")
    #print(os.name)
    #print(os.getcwd())
    #print(os.getlogin())

#Function 800
#Open a shell prompt
def openShellPrompt():
    os.system("start /wait cmd /c {command}")



def main():
    
    while True:
        print ("What would you like to do today?\n")
        print ("Please make a selection or quit.\n")
        print ("1. Print Working Directory")
        print ("2. Change Directory")
        print ("3. Display directory contents ")
        print ("4. Make new directory")
        print ("5. Print System Information (windows) - need exapanded windows and full linux functionality")
        print ("6. Remove Directory and its contents")
        print ("7. Remove an empty directory")
        print ("8. Delete a file")
        print ("9. Display Network Information - need linux functionality")
        print ("10. Open a text editor - Coming soon")
        print ("700. Call a Test Function")
        print ("600. Quit ")
        print()

        #user enters their choice and presses ENTER
        userSelect = input("Make A selection and press ENTER: ")
        print()

        #run selection 1-Print working directory
        if userSelect == '1':
            printWorkingDirectory()
        
        #change directory and display new working path
        elif userSelect == '2':
            changeWorkingDirectory()

        #display directory contents (windows)
        elif userSelect == '3':
            printDirectoryContents()

        #make a new directory
        elif userSelect == '4':
            makeNewDirectory()

        #Print System Information (windows)
        elif userSelect == '5':
            displaySystemInformation()

        #call deleteDirectoryAndContents function
        elif userSelect == '6':
            deleteDirectoryAndContents()
        
        #remove an empty directory
        elif userSelect == '7':
            removeEmptyDirectory()

        #call deleteFile function
        elif userSelect == '8':
            deleteFile()

        #call displayNetworkInformation function
        elif userSelect == '9':
            displayNetworkInformation()

        elif userSelect == '10':
            openTextEditor()
        
        #call a test function
        elif userSelect == '700':
            testFunction()
    
        #exit Program
        elif userSelect == '600':
            return False
        
        elif userSelect =='800':
            openShellPrompt()

        #Ignore invalid entry
        else:
            print("Invalid selection. Please try again \n")
            print()
        
if __name__ == "__main__":
    main()