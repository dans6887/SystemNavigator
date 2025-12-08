import SystemNavigator
os = SystemNavigator.os
systemtype = SystemNavigator.platform.system()

#function 9
#Display NetworkInfomation
def displayNetworkInformation():
    if systemtype == 'Linux':
        data = os.system('ifconfig /all')
        print(data)
        
    elif systemtype == 'Windows':
        data = os.system('ipconfig /all')
        print(data)