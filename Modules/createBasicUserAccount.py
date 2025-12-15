import SystemNavigator
import subprocess
subprocess = SystemNavigator.subprocess
import string
import time
import getpass
import sys

os = SystemNavigator.os
systemtype = SystemNavigator.platform.system()

#function 11
#create Basic user account



########################################################################################
###                                                                                  ###
###                        This option still in development                          ###
###                                                                                  ###
########################################################################################


 
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

    ##############################################
    # If Windows system, create new windows user #
    ##############################################
    elif systemtype == 'Windows':
        try:
            print("Create new windows user account.")
            confirm_user_create = input("do you wish to continue? ")

            confirm_create_yes = ["yes", "y", "Y", "Yes", "YES"]
            confirm_create_no = ["no", "n", "N", "No", "NO"]

            if confirm_user_create in  confirm_create_yes:
                
                username = input("Enter the name of the new user: " ).strip()
                print("""
                #########################################
                # Passwords must contain the following: #
                #########################################
                1. Upper and lowercase letters
                2. Contain at least one number
                3. Contain at least one special character
                4. Be at least 10 characters long

                """)
                user_password = getpass.getpass("Enter a password for the new user account: ").strip()
                user_password_confirm = getpass.getpass("Re-enter the new user password to confirm: ").strip()
            
                password_length = len(user_password)#get lenth of password

                special_characters = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'}
                capital_letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
                lower_case_letters ="qwertyuiopasdfghjklzxcvbnm"
                numbers = "1234567890"
                if password_length >= 10:
                    if any(char in special_characters for char in user_password):
                        if any(char in capital_letters for char in user_password):
                            if any(char in lower_case_letters for char in user_password):
                                if any(char in numbers for char in user_password):
                                    if user_password_confirm == user_password:  #If ALL conditions are met create the user account and password
                                        
                                        print(f"Attempting to create user: {username}")
                                        print("-" * 30)

                                        # The net user command to create a new user:
                                        # net user <username> <password> /add
                                        creation_command = ["net", "user", username, user_password, "/add"]

                                        try:
                                            # 1. Execute the user creation command
                                            # NOTE: This script **MUST be run with Administrator privileges**.
                                            result = subprocess.run(
                                                creation_command,
                                                time.wait(5),
                                                print("Processing..."),
                                                capture_output=True,
                                                text=True,
                                                check=True  # Will raise CalledProcessError on failure
                                            )
                                            
                                            print(f"✅ User '{username}' created successfully.")

                                        except subprocess.CalledProcessError as e:
                                            # Check for common permission error (Access is denied)
                                            if "Access is denied" in e.stderr:
                                                print("❌ FAILED: Access Denied.")
                                                print("Please ensure you run this Python script with **Administrator privileges** (Right-click -> Run as Administrator).")
                                            elif "already exists" in e.stderr:
                                                print(f"❌ FAILED: User '{username}' already exists on this system.")
                                            else:
                                                print(f"❌ FAILED to create user '{username}'.")
                                                print(f"Error: {e.stderr.strip()}")
                                            sys.exit(1) # Exit if user creation failed

                                        except FileNotFoundError:
                                            print("❌ Error: 'net' command not found. Ensure you are running this on a Windows system.")
                                            sys.exit(1)

                                    else:
                                        print("Passwords do not match")
                                        exit
                                else:
                                    print("Password must contain at least one number")
                            else:
                                print("password must contain at least one lower-case letter")
                        else:
                            print("Password must contain at least one capital letter")
                    else:
                        print("Password must contain at least one special character")
                else:
                    print("Password must be ten or more characters")

            elif confirm_user_create in confirm_create_no:
                exit
        except subprocess.CalledProcessError:
            print("🚨 **ERROR:** This script must be run with Administrator privileges.")
            print("Please right-click the script and choose 'Run as administrator'.")
            return False
        
        except FileNotFoundError:
            print("🚨 **ERROR:** 'net user' command not found. Are you running on Windows?")
            return False
########################################################################################
###                                                                                  ###
###                        This option still in development                          ###
###                                                                                  ###
########################################################################################