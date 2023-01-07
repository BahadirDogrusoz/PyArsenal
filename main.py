import os
import time
import sys

from programs import Programs

try:
    os.system("apt-get install -y figlet")
    os.system("clear")
    os.system("figlet PyArsenal")

    print("""
    
    Welcome the PyArsenal - Made By C0nnect0r
    
    1)Brute Force Program
    2)Compiler Program
    3)Database Vulnerability Finder
    4)Firewall Detector
    5)Mac Changer
    6)Rootkit Scanner
    7)Search Exploit
    8)Server Vulnerability Analysis
    9)VPN Control
    10)Vulnerability Analysis
    11)Wordlist Creator
    12)Wordpress Scanner
    
    """)
    process_no = input("Enter a process number: ")

    if process_no == "1":
        program = Programs.bruteforce(self="default")
    elif process_no == "2":
        program = Programs.compilerProgram(self="default")
    elif process_no == "3":
        program = Programs.databaseHandler(self="default")
    elif process_no == "4":
        program = Programs.firewallDetector(self="default")
    elif process_no == "5":
        program = Programs.macChanger(self="default")
    elif process_no == "6":
        program = Programs.rootkitScanner(self="default")
    elif process_no == "7":
        program = Programs.searchExploit(self="default")
    elif process_no == "8":
        program = Programs.serverVuln(self="default")
    elif process_no == "9":
        program = Programs.vpnControl(self="default")
    elif process_no == "10":
        program = Programs.vulnAnalysis(self="default")
    elif process_no == "11":
        program = Programs.wordlistCreator(self="default")
    elif process_no == "12":
        program = Programs.wordpressScanner(self="default")
    else:
        print("Wrong process number!Program will restart!")
        time.sleep(2)
        os.system("python3 main.py")
except KeyboardInterrupt:
    ex = input("\nIf you want to quit press q and enter: ")
    if ex == "q":
        print("\033[92mProcess has completed!")
        sys.exit()