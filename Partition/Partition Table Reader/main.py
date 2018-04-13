import ctypes
import sys
import admin
import os

admin.admin_permission()
admin.check_admin()

handle = open('\\\\.\\PhysicalDrive1', 'rb')

handle.seek(0)

mbr = handle.read(512)

handle.close()

if ord(mbr[510]) == 0x55 and ord(mbr[511]) == 0xAA:
    print("MBR Read Success!")
else:
    print("MBR Read Fail..")

# Test getting physical drive information
