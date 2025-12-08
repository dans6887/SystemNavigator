import SystemNavigator
subprocess = SystemNavigator.subprocess

os = SystemNavigator.os
systemtype = SystemNavigator.platform.system()

#function 11
#create Basic user account

 
def createBasicUserAccount():
    if systemtype == 'Linux':#if the system is linux based
        username = print(input("Enter a username for the account: "))
        new_password = print(input("Enter a password for the account: "))
        print("Enter your admin password.")
        #password = getpass.getpass() #ask for user's password
        try:
            subprocess.run(['sudo', 'useradd ',username, ' -p ', new_password ])
        except:
            print("Failed to add user. Please try again later.")
            #system.exit(1)
            
########################################################################################
###                                                                                  ###
###                        This option still in development                          ###
###                                                                                  ###
########################################################################################