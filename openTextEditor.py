#function 10
#open text editor

import SystemNavigator
os = SystemNavigator.os
systemType = SystemNavigator.platform.system()
subprocess = SystemNavigator.subprocess

def openTextEditor():
    if systemType == 'Linux':#if the system is linux based
        pass
    
    elif systemType == 'Windows':#if the system is windows based
        """
        Opens the Notepad application on a Windows system.
        """
        try:
            # Check if the operating system is Windows
            if os.name == 'nt':
                # Use 'notepad.exe' for the Windows built-in text editor
                subprocess.Popen('notepad.exe')
                print("✅ Notepad has been launched.")
            else:
                print("⚠️ This script is intended for Windows. For Linux/macOS, try 'gedit' or 'TextEdit' (using the appropriate command).")

        except FileNotFoundError:
            print("❌ Error: 'notepad.exe' not found. Ensure the application is correctly installed and in the system's PATH.")
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")