import struct

def ExtendedPartition(part):
    print("ExtendedPartition")


def PrimaryPartition(part):  # 주 파티션 정보 출력
    print("PrimaryPartition")

    # Starting LBA
    start = struct.unpack('<L', part[8:8+4])[0]
    print("LBA value : {}".format(start))

    # Print Partition's size
    num = struct.unpack('<L', part[12:12+4])[0]
    size = (num * 512.) / 1024 / 1024 / 1024
    print("Partition size : {} GB".format(size))