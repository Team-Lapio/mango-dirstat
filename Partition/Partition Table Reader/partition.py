import struct

def UnitChange(num):
    sector_size = ['B', 'KB', 'MB', 'GB']

    t = sizes = (num * 512.)

    for i in range(4):
        t = t / 1024
        if int(t) > 0:
            sizes = sizes / 1024
        else:
            break

    return "%.2f %s" % (sizes, sector_size[i])

def ExtendedPartition(part, start):
    handle = open('\\\\.\\PhysicalDrive0', 'rb')
    base = struct.unpack('<L', part[8:8+4])[0]

    print("ExtendedPartition")
    print(base)  # main.py의 base 값을 전달받을 방법을 알아봐야한다!!
    
    handle.seek((base + start) * 512)
    data = handle.read(0x200)

    if hex(data[510]) == '0x55' and hex(data[511]) == '0xaa':
        print("Partition Read Success")
        
        # 논리 드라이브 정보 획득
        logical_part = []

        for i in range(2):
            logical_part.append(data[0x1BE + (i*0x10):0x1BE + (i*0x10) + 0x10])

        if hex(logical_part[0][4]) != '0x0':  # 논리 드라이브 정보가 존재하면 조건문 실행
            LogicalDrivePartition(logical_part[0], base+start)
        if hex(logical_part[1][4]) != '0x0':  # 확장 논리 드라이브 정보가 존재하면 조건문 실행
            start = struct.unpack('<L', logical_part[1][8:8+4])[0]
            ExtendedPartition(logical_part[1], start)


def LogicalDrivePartition(part, base):
    print("LogicalDrivePartition")
    start = struct.unpack('<L', part[8:8+4])[0]  # Starting LBA
    num = struct.unpack('<L', part[12:12+4])[0]  # Print Partition's size
    print("[Logical] %10d %s" % (start, UnitChange(num)))


def PrimaryPartition(part):  # 주 파티션 정보 출력
    start = struct.unpack('<L', part[8:8+4])[0]  # Starting LBA
    num = struct.unpack('<L', part[12:12+4])[0]  # Print Partition's size
    print("[Primary] %10d %s" % (start, UnitChange(num)))
