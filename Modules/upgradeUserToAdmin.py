import SystemNavigator
os = SystemNavigator.os
systemType = SystemNavigator.platform.system()
def upgradeUserToAdmin():
    if systemType == 'Linux': #if the system is linux based
        pass
    elif systemType == 'Windows':#if the system is windows based
        # --- Optional: Add the user to the local Administrators group ---
        username = input("Enter the username that you want to upgrade: ").strip()
            # The net localgroup command:
            # net localgroup Administrators <username> /add
        admin_group_command = ["net", "localgroup", "Administrators", username, "/add"]

        try:
            print("\nAttempting to add user to Administrators group...")
            result = subprocess.run(
                admin_group_command,
                capture_output=True,
                text=True,
                check=True
            )
            print(f"✅ User '{username}' successfully added to the Administrators group.")

        except subprocess.CalledProcessError as e:
            # This failure is usually less critical than the user creation failure
            print(f"⚠️ Warning: Could not add user '{username}' to Administrators group.")
            # In some non-English Windows versions, "Administrators" might be translated.
            print(f"Warning/Error Output: {e.stderr.strip()}")
    
    
########################################################################################
###                                                                                  ###
###                        This option still in development                          ###
###                                                                                  ###
########################################################################################