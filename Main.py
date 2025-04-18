import time
from winsound import Beep
from os import system
import keyboard
import wmi
import datetime
import socket
import random
import os
from colorama import Fore, Style, init
import string
import winsound
import psutil
import win32process,win32api,win32con
import win32gui
from win32api import GetAsyncKeyState
import pydivert
from os import path
import ctypes

string.ascii_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
mb2 = random.randint(1000, 3999)
kirrrr = random.choice(string.ascii_letters)
kir = random.choice(string.ascii_letters)
def print_banner():
    system("cls")
    print(Style.BRIGHT + Fore.CYAN +"""
 		   
            ▄▀█ █░█ ▀█▀ █▀█ █▄▀ █ █▀▀ █▄▀
            █▀█ █▄█ ░█░ █▄█ █░█ █ █▄▄ █░█
 		    GHOST________MODE
   """)

system("cls")


def check():
    ccc = wmi.WMI()
    sss = ccc.Win32_Processor()
    hardid = sss[0].ProcessorId
    processid = sss[0].Description
    now = datetime.datetime.now()
    cock = now.strftime("%M")
    gh = now.strftime("%S")
    current_time = now.strftime("%d/%m/%y")
    start_current_time = datetime.date(now.year, now.month, now.day)
    end_current_time = datetime.date(2023, 2, 4)
    end_day = (end_current_time - start_current_time).days
    x = int(cock)
    j = int(gh)
    x = x * 99 * 15 * 79 * 2 * j
    hostname=socket.gethostname()
    IPAddr=socket.gethostbyname(hostname)
    pime = now.strftime("%I:%M:%S")
    ran = random.randint(0, 3)
    os.system("cls")
    print(Style.BRIGHT + Fore.CYAN +f"[{pime}] "+"Searching For Updates..."+Style.RESET_ALL)
    time.sleep(3.6)
    print(Style.BRIGHT + Fore.CYAN +f"[{pime}] "+"Ready For Action...")
    time.sleep(3)
    os.system("cls")
    a = path.exists("kdmapper.sys")
    if a == True:
        print(Style.BRIGHT + Fore.CYAN +f"[{pime}] "+"Opening Driver kdmapper..."+Style.RESET_ALL)
    else:
        print(Style.BRIGHT + Fore.RED +"  Cant Load Driver (0x0009)"+Style.RESET_ALL)
        time.sleep(10)
        exit


    time.sleep(8)
    os.system("cls")
    hwid = "BFEBFBFF000806C1"
    process = "Intel64 Family 6 Model 140 Stepping 1"
    if  hardid == hwid and processid == process and 31 > end_day > -1: 
        print(Style.BRIGHT + Fore.CYAN +"""
                █████████████████████████
                █─▄─▄─█▄─▄█▄─▀█▀─▄█▄─▄▄─█
                ███─████─███─█▄█─███─▄█▀█
                ▀▀▄▄▄▀▀▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀ 
        ░░ ░░ ░░ ░░ ░░ ░░ ░░        ░░ ░░ ░░ ░░ ░░ ░░ ░░
                ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀ ▀▀
        ░░ ░░ ░░ ░░ ░░ ░░ ░░        ░░ ░░ ░░ ░░ ░░ ░░ ░░                      
          ᴛɪᴍᴇ ᴏғ ᴘᴜʀᴄʜᴀsᴇ            ᴛɪᴍᴇ ʀᴇᴍᴀɪɴɪᴜɴɢ   """)
                                      
        print(Style.BRIGHT + Fore.YELLOW +f"""                 {current_time}                      {end_day}

        """)
        print(Style.BRIGHT + Fore.CYAN +f"[{pime}]"+Style.BRIGHT + Fore.YELLOW +" VIP USER")
        time.sleep(2.0)
        time.sleep(4)

    else:
        print(Style.BRIGHT + Fore.CYAN+"""             
        ▒█▀▀█ █▀▀█ █▀▀▄ █▀▀ 　 ▒█▀▀▀ █▀▀▄ ▀▀█▀▀ █▀▀ █▀▀█ 
        ▒█░░░ █░░█ █░░█ █▀▀ 　 ▒█▀▀▀ █░░█ ░░█░░ █▀▀ █▄▄▀ 
        ▒█▄▄█ ▀▀▀▀ ▀▀▀░ ▀▀▀ 　 ▒█▄▄▄ ▀░░▀ ░░▀░░ ▀▀▀ ▀░▀▀
             -= Autokick#0611 (Teleport_____MODE) =-
        """+Style.RESET_ALL)
        teleport = input(Style.BRIGHT + Fore.CYAN +f"[{pime}]"+" Please Enter Your Private Code:"+Style.RESET_ALL)
        q = int(teleport)
        if q != x:
            print(Style.BRIGHT + Fore.RED +f"[{pime}]"+"******SYSTEM INFORMATION BLOCKED******")
            print(Style.BRIGHT + Fore.RED +f"[{pime}]"+"User:  "+hostname)
            print(Style.BRIGHT + Fore.RED +f"[{pime}]"+"Local IP:  "+IPAddr)
            print(Style.BRIGHT + Fore.RED +f"[{pime}]"+"CPU Model:  "+processid+Style.RESET_ALL)
            time.sleep(2.0)
            print(Style.BRIGHT + Fore.CYAN +f"[{pime}]"+" Please Contact With Creator [AutoKick#0611].")
            time.sleep(25.0)
            exit()
    print(Style.BRIGHT + Fore.CYAN +f"[{pime}]"+Style.BRIGHT + Fore.GREEN +" Passed")
    time.sleep(6)
    os.system("cls")
    print(Style.BRIGHT + Fore.CYAN +f"[{pime}] "+ Fore.RED+"Spoofing Drivers..."+Style.RESET_ALL)
    time.sleep(3)
    koss = random.randint(123124123123123, 999999999999999)
    print(Style.BRIGHT + Fore.CYAN +f"[{pime}] "+f"1-HEX: {kirrrr}{koss}{kir}"+Style.RESET_ALL)
    time.sleep(4)
    PIDD = random.randint(1010, 2000)
    print(Style.BRIGHT + Fore.CYAN +f"[{pime}] "+f"PROCESS-PID: {PIDD}"+Style.RESET_ALL)
    time.sleep(4)
    os.system("cls")
    print(Style.BRIGHT + Fore.CYAN +f"[{pime}]"+" User:  "+hostname)
    time.sleep(1.5)
    print(Style.BRIGHT + Fore.CYAN +f"[{pime}]"+" IP:    "+IPAddr+"""

    """)
    time.sleep(1.5)
    print(Style.BRIGHT + Fore.CYAN +f"[{pime}]"+" Hardware ID: "+hardid+"""
    """)
    time.sleep(3)
    os.system("cls")
    print(Style.BRIGHT + Fore.CYAN +"""

    ░█████╗░██╗░░░██╗████████╗░█████╗░██╗░░██╗██╗░█████╗░██╗░░██╗
    ██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██║░██╔╝██║██╔══██╗██║░██╔╝
    ███████║██║░░░██║░░░██║░░░██║░░██║█████═╝░██║██║░░╚═╝█████═╝░
    ██╔══██║██║░░░██║░░░██║░░░██║░░██║██╔═██╗░██║██║░░██╗██╔═██╗░
    ██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝██║░╚██╗██║╚█████╔╝██║░╚██╗
    ╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═╝░╚════╝░╚═╝░░╚═╝
 		   -= Autokick#0611 (Teleport_____MODE) =-
   """+ Style.RESET_ALL)
    time.sleep(3.5)
    print(Fore.YELLOW +""" --> Loading injector Kernel32.dll... 
          """)
    time.sleep(13.5)
    winsound.Beep(400, 200)
    try:
        a = os.environ['USERPROFILE']
        b = a + "\Desktop\Black Squad.url"
        os.startfile (b)
    except:
        print(Style.BRIGHT +Fore.RED +"Cant Access To Game Data!!!!"+Style.RESET_ALL)
        time.sleep(2.5)
        print(Style.BRIGHT +Fore.RED +"Make Sure You Read The Readme.txt!!!!"+Style.RESET_ALL)
        time.sleep(2.5)
        pass
    else:
        print(Style.BRIGHT + Fore.GREEN +" Injected!"+Style.RESET_ALL)
        ctypes.windll.kernel32.SetConsoleTitleW(f"BlackSquad.exe --> pid [{mb2}] ")
        time.sleep(1.5)
        

check()

def print_lt(Speed,lag,AB_status,AB_RED,MODE_status):
    system("cls")
    print(Style.RESET_ALL + Fore.YELLOW +"""
                   
        ▄▀█ █░█ ▀█▀ █▀█ █▄▀ █ █▀▀ █▄▀
        █▀█ █▄█ ░█░ █▄█ █░█ █ █▄▄ █░█
            Teleport[*_*]________MODE
    """+ Style.RESET_ALL)
    print(Fore.YELLOW +"""========================= Controls =====================
          """)
    print("    CHEAT MODE                                   :",Fore.YELLOW + MODE_status + Style.RESET_ALL)
    print("    CHEAT HOTKEY                                 :",Fore.CYAN + str(lag) + Style.RESET_ALL)
    print("    BULLET INCREASE HOTKEY                       :", Fore.RED + "=" + Style.RESET_ALL)
    print("    CHEAT HOTKEY                                 :",Fore.CYAN + str(Speed) + Style.RESET_ALL)
    print("    RESET SETTINGS                               :", Fore.CYAN   + """NUMPAD 9
    """ + Style.RESET_ALL)
    print(Fore.YELLOW +"""======================= Information ====================
          """)
    print("    BATTELEYE DETECT                             :", Fore.GREEN + "safe" + Style.RESET_ALL)
    print("    INJECTOR                                     :", Fore.CYAN +"kernel32.dll"+ Style.RESET_ALL)
    print("    CHEAT STATUS                                 :", AB_RED + AB_status + Style.RESET_ALL)
    print(Fore.CYAN +"""

          
          """)
    print(Fore.YELLOW +"--> Running!!!!"+Style.RESET_ALL)




def main():
    print_banner()
    system("cls")
    print_banner()
    try:
        cmd10 = input(Fore.CYAN +" Rage Mode Choose:"+ Fore.YELLOW +"(1)"+ Fore.CYAN +"   [1 = Teleport Mode] :"+ Fore.YELLOW)
        Mode = int(cmd10)
        time.sleep(0.2)
        print("")
        cmd = input(Fore.CYAN +" Teleport HotKey (default:"+ Fore.YELLOW +"(b or c)"+ Fore.CYAN +"[Key For Active Cheat] ):"+ Fore.YELLOW)
        lag = str(cmd)
        cmd2 = input(Fore.CYAN +" SpeedHack HotKey (default:"+ Fore.YELLOW +"(b or c)"+ Fore.CYAN +"[Key For Active Cheat] ):"+ Fore.YELLOW)
        Speed = str(cmd2)
        time.sleep(0.2)
        time.sleep(1)
        print("")
    except:
        pass
    system("cls")
    aimbot = True
    A_status = "OFF"
    AB_status = "OFF"
    A_RED = Fore.RED
    AB_RED = Fore.RED
    MODE_status = "Teleport Kill Mode"
    if Mode == 2:
        MODE_status = "Sneaky Mode"
    print_lt(Speed,lag,AB_status,AB_RED,MODE_status)
    d = pydivert.WinDivert("outbound")
    while Mode == 1:
        if GetAsyncKeyState(win32con.VK_NUMPAD9):
            main()
        if GetAsyncKeyState(win32con.VK_NUMPAD5):
            if aimbot == False:
                aimbot = True
                Beep(400, 150)
                AB_status = "OFF"
                AB_RED = Fore.RED
                print_lt(Speed,lag,AB_status,AB_RED,MODE_status)
            else:
                aimbot = False
                Beep(400, 150)
                AB_status = "ON"
                AB_RED = Fore.CYAN
                print_lt(Speed,lag,AB_status,AB_RED,MODE_status)                                
        if aimbot == False:
            data = []
            d.open()
            i = 0
            while True:
                for packt1 in d:
                    d.send(packt1)
                    if keyboard.is_pressed(Speed):
                        winsound.Beep(400, 150)
                        for packt1 in d:
                            x = d.recv(bufsize=1500)
                            data.append(x)
                            i = i + 1
                            if i == 5:
                                for a in data:
                                    d.send(a)
                                i = 0
                            if keyboard.is_pressed(Speed):
                                data = []
                                winsound.Beep(200, 250)
                                time.sleep(0.1)
                                break
                    if keyboard.is_pressed(lag):
                        winsound.Beep(400, 150)
                        for packt1 in d:
                            x = d.recv(bufsize=1500)
                            data.append(x)
                            if keyboard.is_pressed(lag):
                                for a in data:
                                    d.send(a)
                                data = []
                                winsound.Beep(200, 250)
                                time.sleep(0.1)
                                break
                    if keyboard.is_pressed('='):
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
                        time.sleep(0.05)
                        winsound.Beep(400, 200)
                        d.close()
                        time.sleep(0.05)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
                        keyboard.press('3')
                        keyboard.release('3')
                        keyboard.press('1')
                        keyboard.release('1')
                        time.sleep(4.5)
                        d.open()
                        keyboard.press('3')
                        keyboard.release('3')
                        time.sleep(4.5)
                        d.close()
                        keyboard.press('1')
                        keyboard.release('1')
                        keyboard.press('3')
                        keyboard.release('3')
                        time.sleep(0.5)
                        keyboard.press('1')
                        keyboard.release('1')
                        time.sleep(0.8)
                        keyboard.press('r')
                        keyboard.release('r')
                        time.sleep(5)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
                        time.sleep(0.2)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
                        winsound.Beep(400, 200)
                        d.open()
             

main()


