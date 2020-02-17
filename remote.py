import os

# changes the color of the command prompt 
os.system('color f1')

# global varibles 
ipAddress = ""
command = ""

def WriteHistory(ipAddress):
    lines = []
    # put file in lines list
    try:
        f = open("HISTORY.txt")
        for line in f:
            lines.append(line)
        f.close()
    except:
        pass

    # insert value at begining
    lines.insert(0,ipAddress + '\n')

    # rewrite file
    f = open("HISTORY.txt", "w")
    for i in lines:
        f.write(i)
    f.close()


# gives a prompt to set a new ip address 
def SetIP():
    global ipAddress
    print("Type in IP address or computer name")
    ipAddress = str(input())
    WriteHistory(ipAddress)
    os.system('cls')

# main menu for the application 
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
        print("13. History")
        print()
        print()
        print("Command Ran         " + command)
        print()
        print()
        command = ""
        
        # gets the input 
        selection = input()

        # runs command for get information
        if (selection == "1"):
            c = "start cmd /k psinfo \\" + "\\" + ipAddress
            os.system(c)
            command = "psinfo \\" + "\\" + ipAddress

        # runs command for getting domain name
        elif (selection == "2"):
            c = "start cmd /k nslookup " + ipAddress
            os.system(c)
            command = "nslookup " + ipAddress

        # runs command for seeing who is logged in
        elif (selection == "3"):
            c = "start cmd /k psloggedon \\" + "\\" + ipAddress
            os.system(c)
            command = "psloggedon \\" + "\\" + ipAddress

        # runs command for executing the command prompt 
        elif (selection == "4"):
            c = "start cmd /k psexec \\" + "\\" + ipAddress + " cmd" 
            os.system(c)
            command = "psexec \\" + "\\" + ipAddress + " cmd"
        
        # runs command for executing ipconfig
        elif (selection == "5"):
            c = "start cmd /k psexec \\" + "\\" + ipAddress + " ipconfig" 
            os.system(c)
            command = "psexec \\" + "\\" + ipAddress + " ipconfig"

        # runs command for executing ipconfig /all
        elif (selection == "6"):
            c = "start cmd /k psexec \\" + "\\" + ipAddress + " ipconfig /all" 
            os.system(c)
            command = "psexec \\" + "\\" + ipAddress + " ipconfig /all"

        # runs command for launching team view on remote computer
        elif (selection == "7"):
            c = "start cmd /k psexec -s -d -i \\" + "\\" + ipAddress + ' "C:\Program Files (x86)\TeamViewer\TeamViewer.exe"' 
            os.system(c)
            command = "psexec -s -d -i \\" + "\\" + ipAddress + ' "C:\Program Files (x86)\TeamViewer\TeamViewer.exe"'

        # runs command for launching any application on remote computer
        elif (selection == "8"):
            os.system('cls')
            print("Type the name of the program you want to launch remotly (notepad or cmd)")
            program = input()
            c = "start cmd /k psexec -s -d -i \\" + "\\" + ipAddress + " " + program 
            os.system(c)
            command = "psexec -s -d -i \\" + "\\" + ipAddress + " " + program 

        # changes IP address
        elif (selection == "9"):
            SetIP()

        # runs command for pinging or pinging a port 
        elif (selection == "10"):
            print("Type in the port you want to connect to or leave blank to ping IP only")
            port = input()
            if (port == ""):
                c = "start cmd /k ping -t " + ipAddress 
                os.system(c)
                command = "ping -t " + ipAddress 
            else:
                c = "start cmd /k psping -t " + ipAddress + ":" + port
                os.system(c)
                command = "psping -t " + ipAddress + ":" + port

        # runs command for seeing if tool will work
        elif (selection == "11"):
            c = "start cmd /k net view " + ipAddress 
            os.system(c)
            command = "net view " + ipAddress 

        # runs command for seeing if tool will work
        elif (selection == "12"):
            c = "start cmd /k psping -t " + ipAddress + ":139"
            os.system(c)
            command = "psping -t " + ipAddress + ":139"

        elif (selection == "13"):
            c = "HISTORY.txt"
            os.system(c)
            command = c

MainMenu()