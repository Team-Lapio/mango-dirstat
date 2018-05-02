import struct
import admin
import partition


admin.admin_permission()  # 관리자 권한 상승 요청 함수
admin.check_admin()  # 관리자 권한 여부 확인 함수

if __name__ == '__main__':
    handle = open('\\\\.\\PhysicalDrive0', 'rb')  # 하드디스크 1을 바이너리 읽기 형식으로 열기

    handle.seek(0 * 512)  # 현재 위치에서 0으로 이동
    
    mbr = handle.read(0x200)  # handle 에서 512Byte 만큼을 읽어와 mbr 변수에 저장
    
    if hex(mbr[510]) == '0x55' and hex(mbr[511]) == '0xaa':  # MBR의 Signature 값을 확인 // MBR Signature = 0xAA, 0x55
        print("MBR Read Success!")

        part_info = []  # 파티션 정보를 저장할 temp list

        for i in range(4):
            part_info.append(mbr[0x1BE + (i * 0x10): 0x1BE + (i * 0x10) + 0x10])  # 0x1BE부터 시작되는 파티션 테이블의 정보를 part_info 리스트에 저장

        for i in range(4):
            p = part_info[i]
            if hex(p[4]) == '0xF' or hex(p[4]) == '0x5':
                base = struct.unpack('<L', p[8:8+4])[0]  # Base
                partition.ExtendedPartition(p, 0)  # 확장 파티션
            elif hex(p[4]) != 0:
                partition.PrimaryPartition(p)  # 주 파티션
    else:
        print("MBR Read Fail..")

    handle.close()  # 파일 입출력 함수 종료
    