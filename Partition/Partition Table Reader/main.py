import ctypes
import sys
import admin
import os

admin.admin_permission()  # 관리자 권한 상승 요청 함수
admin.check_admin()  # 관리자 권한 여부 확인 함수

handle = open('\\\\.\\PhysicalDrive1', 'rb')  # 하드디스크 1을 바이너리 읽기 형식으로 열기

handle.seek(0)  # 현재 위치에서 0으로 이동

mbr = handle.read(512)  # handle 에서 512Byte 만큼을 읽어와 mbr 변수에 저장

handle.close()  # 파일 입출력 함수 종료

if ord(mbr[510]) == 0x55 and ord(mbr[511]) == 0xAA:  # MBR의 Signature 값을 확인 // MBR Signature = 0xAA, 0x55
    print("MBR Read Success!")

    part_info = []  # 파티션 정보를 저장할 temp list

    for i in range(4):
        part_info.append(mbr[0x1BE + (i * 0x10): 0x1BE + (i * 0x10) + 0x10])  # 0x1BE부터 시작되는 파티션 테이블의 정보를 part_info 리스트에 저장

    for i in range(4):
        p = part_info[i]
        if ord(p[4]) == 0xF or ord(p[4]) == 0x5:
            print("{} : ExtendedPartition".format(i))  # 확장 파티션
        elif ord(p[4]) != 0:
            print("{} : PrimaryPartition".format(i))  # 주 파티션

else:
    print("MBR Read Fail..")

# Test getting physical drive information
