import ctypes
import admin
import os
import sys
import win32com.shell


# -----------------------------------------------------------------
# 관리자 권한 여부 확인 후 권한 상승

def admin_permission():
    try:
        if ctypes.windll.shell32.IsUserAnAdmin():
            return
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, sys.argv[0], None, 1)

    except:
        return False


admin_permission()  # 함수 실행
# -----------------------------------------------------------------
# 관리자 권한 여부 체크

if ctypes.windll.shell32.IsUserAnAdmin():
    print("Hello Admin!")
else:
    print("You are not admin!")
    exit()
# -----------------------------------------------------------------
# 관리자 권한일 경우 HDD1 섹터 정보를 파일로 입력

handle = open('\\\\.\\PhysicalDrive1', 'rb')

handle.seek(0)

mbr = handle.read(512)

handle.close()

if ord(mbr[510]) == 0x55 and ord(mbr[511]) == 0xAA:
    print("MBR Read Success!")
else:
    print("MBR Read Fail..")
