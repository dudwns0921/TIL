# Android

## adb 스크린 캡처하기

```shell
> adb shell screencap -p /sdcard/screen.png
> adb pull /sdcard/screen.png
> adb shell rm /sdcard/screen.png
```

1. screencap 명령으로 캡쳐한다.
2. pull 명령어를 통해 원하는 위치로 가져온다.
3. rm 명령어로 생성한 이미지 파일을 삭제한다.

### screencap

#### -d : 디스플레이 선택

장치에 여러 디스플레이 또는 화면이 있는 경우 캡처하려는 특정 화면을 지정해야 할 수 있다. 이 때 디스플레이 ID를 통해 특정 화면만 캡처가 가능하다.

```shell
> screencap -d 1 /path/to/screenshot.png
```

#### -p : 명시적으로 png 형식으로 저장

#### --delay : 지연 후 캡처

```shell
> screencap --delay 2000 /path/to/screenshot.png
```

# :books: 참고자료

http://heyo.net/wp/66574
