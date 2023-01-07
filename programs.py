import os
import time
import sys
import py_compile


class Programs:
    def bruteforce(self):
        try:
            os.system("apt-get install -y figlet")
            os.system("apt-get install -y ncrack")
            os.system("clear")
            os.system("figlet Brute Force")

            print("""
    
            Welcome the Brute Force Program - Made By C0nnect0r
    
            1)FTP
            2)SSH
            3)Telnet
            4)HTTP
            5)SMB
            6)RDP
            7)VNC
            8)Redis
            9)PostgreSQL
            10)MySQL
    
            """)

            process_no = input("Enter a process number: ")
            targetIp = input("Enter the target ip: ")
            port = input("Enter the port number: ")
            username = input("Usernames path: ")
            password = input("Passwords path: ")

            if process_no == "1":
                os.system(f"ncrack -p {port} -U {username} -P {password} {targetIp}")
                print("\033[92mProcess has completed!")
            elif process_no == "2":
                os.system(f"ncrack -p {port} -U {username} -P {password} {targetIp}")
                print("\033[92mProcess has completed!")
            elif process_no == "3":
                os.system(f"ncrack -p {port} -U {username} -P {password} {targetIp}")
                print("\033[92mProcess has completed!")
            elif process_no == "4":
                os.system(f"ncrack -p {port} -U {username} -P {password} {targetIp}")
                print("\033[92mProcess has completed!")
            elif process_no == "5":
                os.system(f"ncrack -p {port} -U {username} -P {password} {targetIp}")
                print("\033[92mProcess has completed!")
            elif process_no == "6":
                os.system(f"ncrack -p {port} -U {username} -P {password} {targetIp}")
                print("\033[92mProcess has completed!")
            elif process_no == "7":
                os.system(f"ncrack -p {port} -U {username} -P {password} {targetIp}")
                print("\033[92mProcess has completed!")
            elif process_no == "8":
                os.system(f"ncrack -p {port} -U {username} -P {password} {targetIp}")
                print("\033[92mProcess has completed!")
            elif process_no == "9":
                os.system(f"ncrack -p {port} -U {username} -P {password} {targetIp}")
                print("\033[92mProcess has completed!")
            elif process_no == "10":
                os.system(f"ncrack -p {port} -U {username} -P {password} {targetIp}")
                print("\033[92mProcess has completed!")
            else:
                print("Wrong process number!Program will restart")
                time.sleep(2)
                os.system(f"python3 {Programs.bruteforce()}")
        except KeyboardInterrupt:
            ex = input("\nIf you want to quit press q and enter: ")
            if ex == "q":
                print("\033[92mProcess has completed!")
                sys.exit()

    # --------------------------------------- Compiler Program -------------------------------------------------------------
    def compilerProgram(self):
        try:
            os.system("apt-get install -y figlet")
            os.system("clear")
            os.system("figlet Compiler")

            print("""
    
            Welcome the Compiler Program - Made By C0nnect0r
    
            """)

            program = input("Enter the program name: ")

            py_compile.compile(program)
            print("\033[92mProcess has completed!")
        except KeyboardInterrupt:
            ex = input("\nIf you want to quit press q and enter: ")
            if ex == "q":
                print("\033[92mProcess has completed!")
                sys.exit()

    # -------------------------------------- Database Vulnerability Finder -------------------------------------------------

    def databaseHandler(self):
        try:
            os.system("apt-get install -y figlet")
            os.system("apt-get install -y sqlmap")
            os.system("clear")
            os.system("figlet Database Vulnerability Finder")

            print("""
    
            Welcome the Database Vulnerability Finder Program - Made By C0nnect0r
    
            1)Vuln Link
            2)Vuln Link and Database Name
            3)Vuln Link and Database Name and Table Name
            4)Vuln Link and Database Name and Table Name and Column Name
    
            """)

            process_no = input("Enter the process number: ")

            if process_no == "1":
                vulnerableLink = input("Enter the vulnerable link: ")
                os.system(f"sqlmap -u {vulnerableLink} --dbs --random-agent")
                print("\033[92mProcess has completed!")
            elif process_no == "2":
                vulnerableLink = input("Enter the vulnerable link: ")
                database = input("Enter the database name: ")
                os.system(f"sqlmap -u {vulnerableLink} -D {database} --tables --random-agent")
                print("\033[92mProcess has completed!")
            elif process_no == "3":
                vulnerableLink = input("Enter the vulnerable link: ")
                database = input("Enter the database name: ")
                table = input("Enter the table name: ")
                os.system(f"sqlmap -u {vulnerableLink} -D {database} -T {table} --columns --random-agent")
                print("\033[92mProcess has completed!")
            elif process_no == "4":
                vulnerableLink = input("Enter the vulnerable link: ")
                database = input("Enter the database name: ")
                table = input("Enter the table name: ")
                column = input("Enter the column name: ")
                os.system(f"sqlmap -u {vulnerableLink} -D {database} -T {table} -C {column} --dump --random-agent")
                print("\033[92mProcess has completed!")
            else:
                print("Wrong process number!Program will restart")
                time.sleep(2)
                os.system(f"python3 {Programs.databaseHandler()}")
        except KeyboardInterrupt:
            ex = input("\nIf you want to quit press q and enter: ")
            if ex == "q":
                print("\033[92mProcess has completed!")
                sys.exit()

    # -------------------------------------- Firewall Detector -------------------------------------------------------------
    def firewallDetector(self):
        try:
            os.system("apt-get install -y figlet")
            os.system("apt-get install -y wafw00f")
            os.system("clear")
            os.system("figlet Firewall Detector")

            print("""
    
            Welcome the Firewall Detector Program - Made By C0nnect0r
    
            1)Firewall Lists
            2)Firewall Detection
    
            """)

            process_no = input("Enter a process number: ")

            if process_no == "1":
                os.system("wafw00f -l")
                print("\033[92mProcess has completed!")

            elif process_no == "2":
                targetSite = input("Enter a website without http/https: ")
                os.system(f"wafw00f {targetSite}")
                print("\033[92mProcess has completed!")
            else:
                print("Wrong process number!Program will restart!")
                time.sleep(2)
                os.system(f"python3 {Programs.firewallDetector()}")
        except KeyboardInterrupt:
            ex = input("\nIf you want to quit press q and enter: ")
            if ex == "q":
                print("\033[92mProcess has completed!")
                sys.exit()

    # -------------------------------------- Mac Changer -------------------------------------------------------------------

    def macChanger(self):
        try:
            os.system("apt-get install -y figlet")
            os.system("apt-get install -y macchanger")
            os.system("clear")
            os.system("figlet Mac Changer")

            print("""
    
            Welcome the Mac Changer Program - Made By C0nnect0r
    
            1)Random MAC Address
            2)Manual MAC Address
            3)Original MAC Address
    
            """)

            process_no = input("Enter a process number: ")

            if process_no == "1":
                interface = input("Enter an interface(eth0/wlan0): ")
                os.system(f"ifconfig {interface} down")
                os.system(f"macchanger -r {interface}")
                os.system(f"ifconfig {interface} up")
                print("\033[92mMAC Address has changed randomly!")
            elif process_no == "2":
                interface = input("Enter an interface(eth0/wlan0): ")
                macAddress = input("Enter a new MAC Address: ")
                os.system(f"ifconfig {interface} down")
                os.system(f"macchanger --mac {macAddress} {interface}")
                os.system(f"ifconfig {interface} up")
                print("\033[92mNew MAC Address has changed manually")
            elif process_no == "3":
                interface = input("Enter an interface(eth0/wlan0): ")
                os.system(f"ifconfig {interface} down")
                os.system(f"macchanger -p {interface}")
                os.system(f"ifconfig {interface} up")
                print("\033[92mMAC Address changed to the originally!")
            else:
                print("Wrong process number!Program will restart!")
                time.sleep(2)
                os.system(f"python3 {Programs.macChanger()}")
        except KeyboardInterrupt:
            ex = input("\nIf you want to quit press q and enter: ")
            if ex == "q":
                print("\033[92mProcess has completed!")
                sys.exit()

    # -------------------------------------- Rootkit Scanner ---------------------------------------------------------------

    def rootkitScanner(self):
        try:
            os.system("apt-get install -y figlet")
            os.system("apt-get install -y chkrootkit")
            os.system("clear")
            os.system("figlet Rootkit Scanner")

            print("""
    
            Welcome the Rootkit Scanner Program - Made By C0nnect0r 
    
            """)

            os.system("chkrootkit")
            print("\033[92mProcess has completed!")
        except KeyboardInterrupt:
            ex = input("\nIf you want to quit press q and enter: ")
            if ex == "q":
                print("\033[92mProcess has completed!")
                sys.exit()

    # -------------------------------------- Search Exploit ----------------------------------------------------------------

    def searchExploit(self):
        try:
            os.system("apt-get install -y figlet")
            os.system("apt-get install -y searchsploit")
            os.system("clear")
            os.system("figlet Search Exploit")

            print("""
    
            Welcome the Search Exploit Program - Made By C0nnect0r
    
            """)

            keyword = input("Enter the keyword for searching: ")
            os.system(f"searchsploit {keyword}")
            print("\033[92mProcess has completed!")

            request = input("Do you want to make a new search (y/n): ")

            if request == "y":
                os.system(f"python3 {Programs.searchExploit()}")
            elif request == "n":
                print("Goodbye!")
            else:
                print("Wrong answer!Program will restart!")
                time.sleep(2)
                os.system(f"python3 {Programs.searchExploit()}")
        except KeyboardInterrupt:
            ex = input("\nIf you want to quit press q and enter: ")
            if ex == "q":
                print("\033[92mProcess has completed!")
                sys.exit()

    # -------------------------------------- Server Vuln Analysis ----------------------------------------------------------

    def serverVuln(self):
        try:
            os.system("apt-get install -y figlet")
            os.system("apt-get install -y nikto")
            os.system("clear")
            os.system("figlet Server Vuln Analysis")

            print("""
    
            Welcome the Server Vulnerability Analysis Program - Made By C0nnect0r
    
            """)

            targetIp = input("Enter the target ip: ")
            os.system(f"nikto -h {targetIp}")
            print("\033[92mProcess has completed!")
        except KeyboardInterrupt:
            ex = input("\nIf you want to quit press q and enter: ")
            if ex == "q":
                print("\033[92mProcess has completed!")
                sys.exit()

    # -------------------------------------- VPN Control -------------------------------------------------------------------

    def vpnControl(self):
        try:
            os.system("apt-get install -y figlet")
            os.system("apt-get install -y ike-scan")
            os.system("clear")
            os.system("figlet Vpn Control")

            print("""
    
            Welcome the Vpn Control Program - Made By C0nnect0r
    
            """)

            targetIp = input("Enter the target ip: ")

            os.system(f"ike-scan {targetIp}")

            print("\033[92mProcess has completed")
        except KeyboardInterrupt:
            ex = input("\nIf you want to quit press q and enter: ")
            if ex == "q":
                print("\033[92mProcess has completed!")
                sys.exit()

# -------------------------------------- Vuln Analysis -----------------------------------------------------------------

    def vulnAnalysis(self):
        try:
            os.system("apt-get install -y figlet")
            os.system("apt-get install -y lynis")
            os.system("clear")
            os.system("figlet Vulnerability Analysis")

            print("""
    
            Welcome the Vulnerability Analysis Program - Made By C0nnect0r
    
            """)

            os.system("lynis audit system")
            print("\033[92mProcess has completed!")
        except KeyboardInterrupt:
            ex = input("\nIf you want to quit press q and enter: ")
            if ex == "q":
                print("\033[92mProcess has completed!")
                sys.exit()

# -------------------------------------- Wordlist Creator --------------------------------------------------------------

    def wordlistCreator(self):
        try:
            os.system("apt-get install -y figlet")
            os.system("apt-get install -y crunch")
            os.system("clear")
            os.system("figlet Wordlist Creator")

            print("""
    
            Welcome the Wordlist Creator Program - Made By C0nnect0r
    
            """)

            minimum_character = input("Enter the minimum character number: ")
            maximum_character = input("Enter the maximum character number: ")
            character = input("Enter the characters: ")
            register_path = input("Enter the register path: ")

            os.system(f"crunch {minimum_character} {maximum_character} {character} -o {register_path}")
            print("\033[92mProcess has completed!")
        except KeyboardInterrupt:
            ex = input("\nIf you want to quit press q and enter: ")
            if ex == "q":
                print("\033[92mProcess has completed!")
                sys.exit()

# -------------------------------------- Wordpress Scanner -------------------------------------------------------------

    def wordpressScanner(self):
        try:
            os.system("apt-get install -y figlet")
            os.system("apt-get install -y wpscan")
            os.system("clear")
            os.system("figlet Wordpress Scanner")

            print("""
    
            Welcome the Wordpress Scanner - Made By C0nnect0r
    
            1)Quick Scan
            2)Plugin Scan
            3)Theme Scan
            4)Admin Username Scan
    
            """)

            process_no = input("Enter the process number: ")

            if process_no == "1":
                site = input("Enter the site address: ")
                os.system(f"wpscan --url {site}")
                print("\033[92mProcess has completed")
            elif process_no == "2":
                site = input("Enter the site address: ")
                os.system(f"wpscan --url {site} --enumerate p")
                print("\033[92mProcess has completed")
            elif process_no == "3":
                site = input("Enter the site address: ")
                os.system(f"wpscan --url {site} --enumerate t")
                print("\033[92mProcess has completed")
            elif process_no == "4":
                site = input("Enter the site address: ")
                os.system(f"wpscan --url {site} --enumerate u")
                print("\033[92mProcess has completed")
            else:
                print("Wrong process number!Program will restart!")
                time.sleep(2)
                os.system(f"python3 {Programs.wordpressScanner()}")
        except KeyboardInterrupt:
            ex = input("\nIf you want to quit press q and enter: ")
            if ex == "q":
                print("\033[92mProcess has completed!")
                sys.exit()