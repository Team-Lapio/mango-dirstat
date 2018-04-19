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

def ExtendedPartition(part):
    print("ExtendedPartition")
    start = struct.unpack('<L', part[8:8+4])[0]  # Starting LBA
    print("[Extended] %10d" % (start))


def PrimaryPartition(part):  # 주 파티션 정보 출력
    start = struct.unpack('<L', part[8:8+4])[0]  # Starting LBA
    num = struct.unpack('<L', part[12:12+4])[0]  # Print Partition's size
    print("[Primary] %10d %s" % (start, UnitChange(num)))