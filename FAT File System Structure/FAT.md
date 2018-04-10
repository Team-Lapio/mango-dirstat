# FAT File System Structure

## FAT 란?

**F**ile **A**llocation **T**able의 약자로 파일의 할당 정보를 표현한 테이블로, Windows 기반의 소용량의 하드디스크에서 사용되었던 간단한 파일 시스템이다.

**FAT**는 `MS-DOS` 당시부터 사용되었던 용어로, `Windows` 운영체제가 대중화되고 난 후 파일 시스템 자체를 가리키는 용어가 되었다.

---

#### 파일 시스템이란?

컴퓨터에서 파일이나 자료를 쉽게 발견 및 접근할 수 있도록 보관 또는 조직하는 체제.

---

### 장점

* 호환성 (Compatibility)
    * 거의 모든 운영체제에서 FAT를 지원하기 때문에 **데이터 전송에 매우 적합**하다.

* 단순성 (Simplicity)
    * FAT 파일 시스템은 구조가 간단하고 신뢰성이 있어, 필요한 메모리의 양이 적어 메모리 절약에 유용하다.

* 저용량 볼륨에서의 파일 사용
    * 저용량 볼륨을 위해서 파일 시스템을 사용할 때에 성능 면으로는 다른 파일 시스템보다 우수하다.

---

#### 볼륨이란?

**볼륨(volume) 또는 논리 드라이브(logical drive)**

컴퓨터 운영 체제 환경에서, 하나의 파일 시스템을 갖춘 하나의 접근 가능한 스토리지 영역을 말한다.

---

위와 같은 FAT의 장점들 때문에, 일반 시스템 이외에도 메모리 카드, 디지털 카메라, 플래시 메모리 등 많은 장치에 사용되고 있다.

---

### 단점

* 보안 취약
    * 파일에 대한 접근을 제어할 보안 기능이 없어, 컴퓨터에 FAT32 파티션 또는 볼륨이 존재하면 컴퓨터에 접근 가능한 모든 사용자가 파일 시스템에 접근 가능하다.

* 크기 제한
    * FAT 파일 시스템의 종류 중 하나인 FAT32에는 크기 제한이 있는데, 32GB보다 큰 파티션을 만들 수 없고 FAT32 파티션에 4GB를 초과하는 파일을 저장할 수 없다.

* 대용량 볼륨에 비적합
    * 단순한 구조로 인해 운영을 위한 추가작업을 하는 데에 제약이 많다. 대용량 볼륨에는 FAT 보다 좋은 성능을 가진 파일 시스템들이 대거 나온 상태이다. `ex) NTFS (New Technology File System)`

---

## 종류

FAT 파일 시스템은 크게 FAT12, FAT16, FAT32로 나눌 수 있다. + exFAT, etc..

FAT 뒤의 숫자는 **비트 수로 최대 표현 가능한 클러스터의 수**를 의미한다.

~~나무위키에 따르면 FAT는 간단하게 말해 '클러스터를 제어하는 것' 이라고 한다.~~

|FAT 형식|최대 표현 가능한 클러스터 수|
|:-:|:-:|
|FAT12|4,084 (2^12-12)|
|FAT16|65,524 (2^16-12)|
|FAT32|268,435,444 (2^28-12)|

FAT의 비트 수는 날이 갈 수록 저장매체의 용량이 빠르게 커져 파일 시스템이 그 용량을 표현하지 못했기 때문에 자연스럽게 늘려가게 된 것이다.

---

## FAT 파일 시스템의 구조

FAT 파일 시스템은 크게 `Reserved Area`, `FAT Area`, `Data Area` 로 나눌 수 있다.

![Image](https://github.com/Team-Lapio/mango-dirstat/blob/master/FAT%20File%20System%20Structure/Image/FAT%20Structure.PNG)

### Reserved Area

`Reserved Area`는 FAT 파일 시스템 구조 중 가장 앞에 위치한 구조로, 여러 개의 섹터로 구성된다.

* Reserved Area 의 기본적인 크기
    * FAT12, FAT16 => 1 Sector
    * FAT32 => 32 Sectors

#### Reserved Area의 구조

`Reserved Area`는 `Boot Sector`, `FSINFO(File System INFOrmation) Sector`, 추가적인 섹터로 구성된다.

![Image](https://github.com/Team-Lapio/mango-dirstat/blob/master/FAT%20File%20System%20Structure/Image/Reserved%20Area%20Structure.PNG)

* Boot Sector
    `Boot Sector` 는 `Reserved Area` 구조 상에서 처음에 위치해 있다. 크기는 1 Sector.

* FSINFO (File System INFOmation)
    `FSINFO`는 일반적으로 `Boot Sector` 다음에 저장되는 구조이며, 7번째 섹터에 내용을 백업해 둔다.
    이는 `BPB`에 정의되어 있어 임의로 지정이 가능하다.
    * 용도<br/>
        운영체제에게 첫 비할당 클러스터의 위치와 전체 비할당 클러스터의 수를 알려준다.

#### BPB

`Boot Record`를 `BIOS Parameter Block` 라고 부르기도 하는데, 이를 줄여 `BPB`라고 부른다.

