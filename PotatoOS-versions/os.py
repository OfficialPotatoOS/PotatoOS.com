from fileinput import filename
import time
import random

User_ID = random.randint(1, 9999999999999999999999999999999999999999999999999999999999999999999)
VRAM = "64mb"
CPU = "Pear Corp CPU home edition"

print("ram:" + VRAM)
print("Booting from Drive 0 (HDD)...")
print("CPU:" + CPU)
print("Welcome to PotatoOS Dev Release 5 type help for all commands")
file_download = []
while True:
    enter = input("Drive 0/Disk_Unallocated_Space> ")

    if enter == "exit":
        exit(0)

    if enter == "setup":
        print("Entering Setup...")
        print("Welcome to setup")
        username = input("Enter Username for this PC: ")
        password = input("Enter Password for this User: ")
        print("If you close and open this you will have to restart setup so do that if you made the wrong password")
        disk = input("input 1 for download on disk drive 0 2 for disk 1")
        if disk == "2":
            print("An Error has occured at 0X7C00:0A5HH")
            time.sleep(12)
            print("BIOS Drive Formated...")
            time.sleep(5)
            print("System Error CMOS 653")
            time.sleep(15)
            exit(0)
        else:
            print("downloading data required for system")
            print("[===      12%        ]")
            time.sleep(12)
            print("[===      17%        ]")
            time.sleep(12)
            print("[=====    36%        ]")
            time.sleep(12)
            print("[=======  46%        ]")
            time.sleep(12)
            print("[=========50%        ]")
            time.sleep(12)
            print("[=========100%=======]")
            input("the system is now activated press any key and then enter to leave the setup> ")
    
    if enter == "potver":
        print("Potato OS Development Release #5")

    if enter == "help":
        print("""Here is the list of commands:
                 exit: exits the system no data is saved
                 setup: sets up the system so you can login whenever you dwonload anything
                 potver: shows PotatoOS version
                 download: downloads a specific file
                 directory/disk0 shows all the files you have on your pc including registries
                 help: shows lists of commands""")
    if enter == "download":
        file_downloads = input("Type the file you want to download> ")
        file_download.append(file_downloads)
        print(f"added {file_downloads}. Total Files: {len(file_download)}")
        if file_downloads == "hacktool.eyx":
            print("An Error has occured at 0X7C00:0A55H Type Error: KERNEL_UNIDENTIFIED_PANIC_STATE 0x4B45524E454C5F554E4944454E5449464945445F50414E49435F5354415445")
    if enter == "open":
        file_open = input("Type the file you want to open> ")
        if file_open in file_download:
            print(f"Opening {file_open}...")
            time.sleep(5)
            print(f"{file_open} opened")
        else:
            print("File not found")