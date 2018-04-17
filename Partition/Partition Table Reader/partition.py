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


def PrimaryPartition(part):  # 주 파티션 정보 출력
    print("PrimaryPartition")

    # Starting LBA
    start = struct.unpack('<L', part[8:8+4])[0]
    print("LBA : {}".format(start))

    # Print Partition's size
    num = struct.unpack('<L', part[12:12+4])[0]
    size = (num * 512.) / 1024 / 1024 / 1024
    print("Partition size : {}".format(UnitChange(num)))