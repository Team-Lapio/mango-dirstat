# Master Boot Record

|MBR 구조|
|:-:|
|Boot code - 446 Byte|
|Partition Table - 64 Byte|
|Signature (2 byte)|

## Boot code

#### 부트 코드의 역할

파티션 테이블에서 부팅 가능한 파티션을 찾아 해당 파티션의 부트 섹터를 호출한다.

부팅 가능한 파티션이 없으면 에러를 출력한다.

- 부트 섹터
    - Reserved Area 섹터의 첫 부분

---

## MBR 영역 데이터 구조

|범위|설명|크기|
|:-:|:-:|:-:|
|0x0000 ~ 0x01BD|Boot code|446 Bytes|
|0x01BE ~ 0x01CD|Partition 1|16 Bytes|
|0x01CE ~ 0x01DD|Partition 2|16 Bytes|
|0x01DE ~ 0x01ED|Partition 3|16 Bytes|
|0x01EE ~ 0x01FD|Partition 4|16 Bytes|
|0x01FE ~ 0x01FF|Signature (0x55AA)|2 Bytes|

---

## 파티션 테이블 데이터 구조

|범위|설명|크기|
|:-:|:-:|:-:|
|0x0000 ~ 0x0000|Boot Indicator|1 Byte|
|0x0001 ~ 0x0003|Starting CHS address|3 Bytes|
|0x0004 ~ 0x0004|Partition type|1 Byte|
|0x0005 ~ 0x0007|Ending CHS address|3 Bytes|
|0x0008 ~ 0x000B|Starting LBA address|4 Bytes|
|0x000C ~ 0x000F|Total Sectors|4 Bytes|

---

#### Boot Indicator

`Boot Indicator`의 Hex 값은 2가지로 구분이 가능하다.

**00 = 부팅에 사용되지 않는 파티션임을 나타낸다.**

**80 = 시스템 파티션임을 나타낸다.**

---

#### Partition type

해당 파티션의 타입을 Hex 값으로 나타낸다.

#### 파티션 테이블 스크립트 제작 시 제외 가능 목록

* Starting CHS address

* Ending CHS address

최근에는 사용하지 않는 부분?

#### CHS

CHS는 Cylinder-Head-Sector의 약자이며 실린더, 헤드, 섹터로 이루어져있는 하드디스크의 물리적 구조를 기반으로 탐색하는 주소 지정 방식이다.

CHS는 물리적 구조 방식을 사용하며, 최근에는 기억 장치의 용량의 제한이 생겨 LBA(Logical Block Addressing) 주소 지정 방식이 많이 사용된다.

LBA는 CHS와 달리 물리적이 아닌 논리적으로 주소를 지정해주고 이를 물리적으로 변환하는 과정은 컴퓨터가 알아서 진행해주기 때문에 유용하게 사용되고 있다.

#### Starting LBA address

LBA의 시작 주소를 나타낸다.

#### Partition type

![Image](https://github.com/Team-Lapio/mango-dirstat/blob/master/Partition/Master%20Boot%20Record/Image/partition%20type.png)

출처 : forensic-proof

1 Byte 크기의 파티션 타입에 대한 Hex 값 정보이다.

```
07h : Windows NT NTFS
0Bh : Windows 95 with 32-bit FAT
0Ch : Windows 95 with 32-bit FAT (using LBA-mode INT 13 extensions)
```
---

HxD에서 Hex 값을 읽을 때는 거꾸로 읽자!!

#### 파티션을 분석해보자!

```
Partition 1 : 80 01 01 00 07 FE FF FF 3F 00 00 00 0B AC FF 09
```

**다음과 같은 파티션이 존재한다면?**

- Boot Indicator : 0x80 -> System Partition

---

**80** 01 01 00 07 FE FF FF 3F 00 00 00 0B AC FF 09

---

- Starting CHS address : 0x00, 0x01, 0x01

---

80 **01 01 00** 07 FE FF FF 3F 00 00 00 0B AC FF 09

---

- Partition Type : 0x07

---

80 01 01 00 **07** FE FF FF 3F 00 00 00 0B AC FF 09

---

- Ending CHS address : 0xFF, 0xFF, 0xFE

---

80 01 01 00 07 **FE FF FF** 3F 00 00 00 0B AC FF 09

---

- Starting LBA address : 0x0000003F => 63

---

80 01 01 00 07 FE FF FF **3F 00 00 00** 0B AC FF 09

---

- Total Sectors : 0x09FFAC0B => 167,750,667

파티션 총 용량 : 167,750,667 * 512 Bytes = 85,888,341,504 Bytes = 76GB

---

80 01 01 00 07 FE FF FF 3F 00 00 00 **0B AC FF 09**

---