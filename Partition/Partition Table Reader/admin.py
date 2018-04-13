import ctypes
import sys


def admin_permission():
    try:
        if ctypes.windll.shell32.IsUserAnAdmin():
            return
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, sys.argv[0], None, 1)

    except:
        return False


def check_admin():
    if ctypes.windll.shell32.IsUserAnAdmin():
        print("Hello Admin!")
    else:
        print("You are not admin!")
        exit()
