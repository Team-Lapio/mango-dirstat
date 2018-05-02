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
        print("---------------------------------------------------")
        print("If the program does not grant administrator rights,")
        print("try running IDE as administrator,")
        print("and then running the program again.")
        print("---------------------------------------------------")
        print("프로그램에서 관리자 권한이 부여되지 않는다면")
        print("IDE를 관리자 권한으로 실행시킨 뒤 프로그램을 다시 실행해보세요")
        print("---------------------------------------------------")
        exit()
