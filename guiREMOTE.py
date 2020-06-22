import tkinter as tk
import os
ipAddress = ""
command = ""
LARGE_FONT= ("Verdana", 12)

# start window 
class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):  
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Service Desk tool")
        self.geometry("400x500")
        self.resizable(0, 0)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPageFrame, ExecuteAProgramFrame, PingFrame):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPageFrame)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# main menu frame      
class StartPageFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.init_window(controller)

    def WriteHistory(self, ipAddress):
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
        
    def UpdateIP(self):
        global ipAddress
        if (self.e1.get() == ""):
            ipAddress = "Bad ip or computer name"
        else:
            ipAddress = self.e1.get()
            self.WriteHistory(ipAddress)
        self.text.set(ipAddress)
        print(self.e1.get())

    def GetInfo(self):
        global ipAddress
        c = "start cmd /k psinfo \\" + "\\" + ipAddress
        os.system(c)
        command = "psinfo \\" + "\\" + ipAddress
        print(command)

    def GetDomainName(self):
        c = "start cmd /k nslookup " + ipAddress
        os.system(c)
        command = "nslookup " + ipAddress
        print(command)

    def GetLoggedOn(self):
        c = "start cmd /k psloggedon \\" + "\\" + ipAddress
        os.system(c)
        command = "psloggedon \\" + "\\" + ipAddress
        print(command)

    def GetRemoteCommandPrompt(self):
        c = "start cmd /k psexec \\" + "\\" + ipAddress + " cmd" 
        os.system(c)
        command = "psexec \\" + "\\" + ipAddress + " cmd"
        print(command)

    def GetIpconfig(self):
        c = "start cmd /k psexec \\" + "\\" + ipAddress + " ipconfig" 
        os.system(c)
        command = "psexec \\" + "\\" + ipAddress + " ipconfig"
        print(command)

    def GetIpconfigAll(self):
        c = "start cmd /k psexec \\" + "\\" + ipAddress + " ipconfig /all" 
        os.system(c)
        command = "psexec \\" + "\\" + ipAddress + " ipconfig /all"
        print(command)

    def GetTeamViewer(self):
        c = "start cmd /k psexec -s -d -i \\" + "\\" + ipAddress + ' "C:\Program Files (x86)\TeamViewer\TeamViewer.exe"' 
        os.system(c)
        command = "psexec -s -d -i \\" + "\\" + ipAddress + ' "C:\Program Files (x86)\TeamViewer\TeamViewer.exe"'
        print(command)

    def GetNetView(self):
        c = "start cmd /k net view " + ipAddress 
        os.system(c)
        command = "net view " + ipAddress 
        print(command)

    def GetPortCheck(self):
        c = "start cmd /k psping -t " + ipAddress + ":139"
        os.system(c)
        command = "psping -t " + ipAddress + ":139"
        print(command)

    def GetHistory(self):
        c = "HISTORY.txt"
        os.system(c)
        command = c
        print(command)
    
    #Creation of widgets
    def init_window(self, controller):
        # creating 
        self.text = tk.StringVar()
        self.text.set("Type in IP address or computer name below")
        self.lab = tk.Label(self, textvariable=self.text)
        
        self.e1 = tk.Entry(self)
        self.updateIP = tk.Button(self, text="Update IP",command=self.UpdateIP)
        self.getInfo = tk.Button(self, text="Get Information", width=40, command=self.GetInfo)
        self.DomainName = tk.Button(self, text="Get Domain Name", width=40, command=self.GetDomainName)
        self.LoggedOn = tk.Button(self, text="See who is logged on", width=40, command=self.GetLoggedOn)       
        self.RemoteCommandPrompt = tk.Button(self, text="Remote Command Prompt", width=40, command=self.GetRemoteCommandPrompt)
        self.Ipconfig = tk.Button(self, text="Ipconfig", width=40, command=self.GetIpconfig)
        self.IpconfigAll = tk.Button(self, text="Ipconfig /all", width=40, command=self.GetIpconfigAll)
        self.TeamViewer = tk.Button(self, text="Execute TeamViewer", width=40, command=self.GetTeamViewer)
        self.ExecuteProgram = tk.Button(self, text="Execute another Program", width=40, command=lambda: controller.show_frame(ExecuteAProgramFrame))
        self.Ping = tk.Button(self, text="Ping / Ping Port", width=40, command=lambda: controller.show_frame(PingFrame))
        self.History = tk.Button(self, text="History", width=40, command=self.GetHistory)

        self.lab2 = tk.Label(self, text="These are tools to see if this program will work")
        self.NetView = tk.Button(self, text="Net View", width=40, command=self.GetNetView)
        self.PortCheck = tk.Button(self, text="Port 139", width=40, command=self.GetPortCheck)
        

        # placing
        self.lab.place(relx=0.5, y=20, anchor=tk.CENTER)
        
        self.e1.place(relx=0.3, y=50, anchor=tk.CENTER)
        self.updateIP.place(relx=0.7, y=50, anchor=tk.CENTER)    
        self.getInfo.place(relx=0.5, y=80, anchor=tk.CENTER)
        self.DomainName.place(relx=0.5, y=110, anchor=tk.CENTER)
        self.LoggedOn.place(relx=0.5, y=140, anchor=tk.CENTER)
        self.RemoteCommandPrompt.place(relx=0.5, y=170, anchor=tk.CENTER)
        self.Ipconfig.place(relx=0.5, y=200, anchor=tk.CENTER)
        self.IpconfigAll.place(relx=0.5, y=230, anchor=tk.CENTER)
        self.TeamViewer.place(relx=0.5, y=260, anchor=tk.CENTER)
        self.ExecuteProgram.place(relx=0.5, y=290, anchor=tk.CENTER)
        self.Ping.place(relx=0.5, y=320, anchor=tk.CENTER)
        self.History.place(relx=0.5, y=350, anchor=tk.CENTER)

        self.lab2.place(relx=0.5, y=380, anchor=tk.CENTER)
        self.NetView.place(relx=0.5, y=410, anchor=tk.CENTER)
        self.PortCheck.place(relx=0.5, y=440, anchor=tk.CENTER)
        

# ececute a program frame
class ExecuteAProgramFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.init_window(controller)
    
    def GetExecuteProgram(self):
        program = self.e1.get()
        c = "start cmd /k psexec -s -d -i \\" + "\\" + ipAddress + " " + program 
        os.system(c)
        command = "psexec -s -d -i \\" + "\\" + ipAddress + " " + program 
        print(command)

    def init_window(self, controller):
        self.lab = tk.Label(self, text="Type in the program you want to execute")
        self.lab2 = tk.Label(self, text="You might need to type in the path")
        self.e1 = tk.Entry(self)
        self.Execute = tk.Button(self, text="Execute",command=self.GetExecuteProgram)
        self.Back = tk.Button(self, text="Back",command=lambda: controller.show_frame(StartPageFrame))

        self.lab.place(relx=0.5, y=20, anchor=tk.CENTER)
        self.lab2.place(relx=0.5, y=50, anchor=tk.CENTER)
        self.e1.place(relx=0.3, y=80, anchor=tk.CENTER)
        self.Execute.place(relx=0.7, y=80, anchor=tk.CENTER) 
        self.Back.place(relx=0.5, y=110, anchor=tk.CENTER) 

class PingFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.init_window(controller)

    def getPing(self):
        print("ping")
        port = self.e1.get()
        if (port != ""):
            c = "start cmd /k psping -t " + ipAddress + ":" + port
            os.system(c)
            command = "psping -t " + ipAddress + ":" + port
        else:
            c = "start cmd /k ping -t " + ipAddress 
            os.system(c)
            command = "ping -t " + ipAddress 
        print(command)


    def init_window(self, controller):
        self.lab = tk.Label(self, text="Type in the port number")
        self.lab2 = tk.Label(self, text="or click Ping Port for a continuous ping")
        self.e1 = tk.Entry(self)
        self.Ping = tk.Button(self, text="Ping Port",command=self.getPing)
        self.Back = tk.Button(self, text="Back",command=lambda: controller.show_frame(StartPageFrame))

        self.lab.place(relx=0.5, y=20, anchor=tk.CENTER)
        self.lab2.place(relx=0.5, y=50, anchor=tk.CENTER)
        self.e1.place(relx=0.3, y=110, anchor=tk.CENTER)
        self.Ping.place(relx=0.7, y=110, anchor=tk.CENTER) 
        self.Back.place(relx=0.5, y=140, anchor=tk.CENTER)
        


app = SeaofBTCapp()
app.mainloop()
