import os

ipAddress = ""
command = ""

def SetIP():
    global ipAddress
    print("Type in IP address or computer name")
    ipAddress = input()
    os.system('cls')

def GetInfo():
    so.system("start cmd /k echo 'psinfo \\192.168.0.44'")

def MainMenu():
    global ipAddress, command
    while (True):
        os.system('cls')
        if (ipAddress == ""):
            SetIP()
        print("REMOTE TOOL")
        print("Current Working IP/Computer Name = " + ipAddress)
        print()
        print(" 1. Get Information")
        print(" 2. Get Domain Name")
        print(" 3. See who is logged on")
        print(" 4. Remote Command Prompt")
        print(" 5. Ipconfig")
        print(" 6. Ipconfig /all")
        print(" 7. Execute TeamViewer")
        print(" 8. Execute another Program")
        print(" 9. Change Working IP/Computer Name")
        print("10. Ping / Ping Port")
        print("11. Net View (checks if this tool will work)")
        print("12. Port 139 (checks if this tool will work)")
        print()
        print()
        print("Command Ran         " + command)
        print()
        print()
        command = ""
        selection = input()

        if (selection == "1"):
            c = "start cmd /k psinfo \\" + "\\" + str(ipAddress)
            os.system(c)
            command = "psinfo \\" + "\\" + str(ipAddress)

        elif (selection == "2"):
            c = "start cmd /k nslookup " + str(ipAddress)
            os.system(c)
            command = "nslookup " + str(ipAddress)

        elif (selection == "3"):
            c = "start cmd /k psloggedon \\" + "\\" + str(ipAddress)
            os.system(c)
            command = "psloggedon \\" + "\\" + str(ipAddress)

        elif (selection == "4"):
            c = "start cmd /k psexec \\" + "\\" + str(ipAddress) + " cmd" 
            os.system(c)
            command = "psexec \\" + "\\" + str(ipAddress) + " cmd"
        
        elif (selection == "5"):
            c = "start cmd /k psexec \\" + "\\" + str(ipAddress) + " ipconfig" 
            os.system(c)
            command = "psexec \\" + "\\" + str(ipAddress) + " ipconfig"

        elif (selection == "6"):
            c = "start cmd /k psexec \\" + "\\" + str(ipAddress) + " ipconfig /all" 
            os.system(c)
            command = "psexec \\" + "\\" + str(ipAddress) + " ipconfig /all"

        elif (selection == "7"):
            c = "start cmd /k psexec -s -d -i \\" + "\\" + str(ipAddress) + ' "C:\Program Files (x86)\TeamViewer\TeamViewer.exe"' 
            os.system(c)
            command = "psexec -s -d -i \\" + "\\" + str(ipAddress) + ' "C:\Program Files (x86)\TeamViewer\TeamViewer.exe"'

        elif (selection == "8"):
            os.system('cls')
            print("Type the name of the program you want to launch remotly (notepad or cmd)")
            program = input()
            c = "start cmd /k psexec -s -d -i \\" + "\\" + str(ipAddress) + " " + program 
            os.system(c)
            command = "psexec -s -d -i \\" + "\\" + str(ipAddress) + " " + program 

        elif (selection == "9"):
            SetIP()

        elif (selection == "10"):
            print("Type in the port you want to connect to or leave blank to ping IP only")
            port = input()
            if (port == ""):
                c = "start cmd /k psping -t " + str(ipAddress) 
                os.system(c)
                command = "psping -t " + str(ipAddress) 
            else:
                c = "start cmd /k psping -t " + str(ipAddress) + ":" + port
                os.system(c)
                command = "psping -t " + str(ipAddress) + ":" + port

        elif (selection == "11"):
            c = "start cmd /k net view " + str(ipAddress) 
            os.system(c)
            command = "net view " + str(ipAddress) 

        elif (selection == "12"):
            c = "start cmd /k psping -t " + str(ipAddress) + ":139"
            os.system(c)
            command = "psping -t " + str(ipAddress) + ":139"

MainMenu()
