# 20190223
SJVA이라는 비디오 관련 Assistant 프로그램을 만드는 중입니다.
기본 기능은 RSS부터 PLEX 라이브러리까지 과정을 자동화해주는 것이며, 
이외 비디오 관련된 툴을 하나로 모아서 편하게 사용하는데 있습니다.

SJVA는 웹 기반으로 동작하며 klive도 하나의 모듈로 SJVA에 포함될 예정입니다.
klive 새 버전은 녹화를 지원하며 웹에서 설정, 커스텀 채널 편집, 채널별 해상도 설정, 녹화 설정 등을 할 수 있게 됩니다.

문제는 SJVA에 포함되면서 전체 코드가 많이 변경되어 지금 git에 있는 버전과 차이가 많이 납니다.
(제가 python을 접한지 이제 2년차이기에, 이전 코드를 보면 너무 창피하네요;;)

아무튼 두 버전을 모두 유지하기 어렵기에, 문제가 있더라도 당분간은 이번 올레 같은 문제 정도만 대응할 수 있으니 양해 바랍니다.
이슈에 올려주시는 사항들 관련하여 수정하거나 답변은 바로 드리지 못하지만, 
가급적 새 버전에 모두 적용하도록 하겠습니다.

# KLive
KLive는 라이브 방송을 제공하는 사이트 및 앱을 크롤링하는 python 코드이다.

- KODI addon
- PLEX plugin
- KLive Server + Android TV App

# 메뉴얼
https://soju6jan.github.io/klive


---
## 폴더구조
####  lib 폴더 내 파일은 공용파일이다. 직접 파일을 복사한 후 설치 해야한다.
  - KODI
  ```
    - plugin.video.KLive
        resoureces
          language
            Korean
            English
          lib  (lib 폴더 복사)
  ```

  - PLEX
  ```
    - KLive.bundle
        Contents
          Code (lib 폴더 내 파일 복사)
          esources
            English
  ```
  - Server
  ```
    - klive_server
        data
        lib  (lib 폴더 복사)
  ```


---
## 변경사항
#### 0.3.0 (2018-10-16)
  - custom 채널 설정 지원
  - Android TV 앱 연동
  -
#### 0.2.2 (2018-08-28)
  - 일부 OS에서 옥수수 안되는 문제 수정

#### 0.2.1 (2018-08-28)
  - KBS 수정

#### 0.1.4 (2018-04-01)
  - KODI / PLEX RADIO2 버그 수정

#### 0.1.3 (2018-03-28)
  - 일부 OS에서 m3u, xml 파일 쓰기가 안되는 문제 수정

#### 0.1.0 (2018-03-18)
  - First Release
