import time

VRAM = "64mb"
CPU = "Pear Corp CPU home edition"

print(VRAM)
print("Booting from Drive 0 (HDD)...")
print(CPU)
enter = input("Drive 0/Disk_Unallocated_Space>")

if enter == "exit":
    exit(0)