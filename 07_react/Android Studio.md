# Android Studio 

## 설치 및 설정 

### Prerequisite

- **JDK >=8.0** Install (http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)

- **Intel VT enabled** - BIOS Menu - Restart with UEFI Firmware Settings - Trigger Key differred by brand

  -  우선 본인의 CPU가 인텔 VT-x 기술을 지원하는지 확인한다.
    `①` https://ark.intel.com/content/www/kr/ko/ark.html **- 찾아서 확인**
    `②` https://downloadcenter.intel.com/ko/download/28539?v=t **- 프로그램 설치로 확인** 

    (source: https://jdh5202.tistory.com/514 )

- **Intel HAXM Installed**  https://github.com/intel/haxm/releases 

  - check `cmd $  sc query intelhaxm `  status: 4 RUNNING

  ** Prerequesite : Hyper-V **MUST** be disabled 

### Android Studio Install...



### Configure Virtual Device Machine with AVD Manager

