# Android

## The emulator process for AVD has terminated.

안드로이드 스튜디오로 디바이스를 생성해 실행하려고 하는데 `The emulator process for AVD has terminated.`의 로그와 함께 팝업이 떴다.

기본적으로 오류가 났을 때는 로그를 참조하는 것이 좋다. 사용자마다 세부적인 경로 차이는 있을 수 있다. 아래 경로 안의 idea.log 파일을 확인하면 된다.

> C:\Users\User\AppData\Local\Google\AndroidStudio2022.3\log

`The emulator process for AVD Pixel_2_API_30 has terminated.` 로그 위에서 최초로 에러가 난 부분을 살펴보니 아래와 같은 로그가 있었다.

> 2024-02-25 11:21:13,166 [ 444467]   INFO - Emulator: Pixel 2 API 30 - .exe: error while loading state for instance 0x0 of device 'goldfish_pipe'

위 로그를 구글링하니 아래 스택오버플로우를 찾을 수 있었다.

https://stackoverflow.com/questions/55969519/can-not-run-my-app-on-emulator-error-while-loading-state-for-instance-0x0-of-d

문제는 내가 이미 SDK Tools 패널에서 HAXM을 설치했다는 것이었다. 참고로 HAXM은 인텔에서 만든 하드웨어 가상화 지원 엔진이다. 크로스 플랫폼 지원이라 안드로이드 에뮬레이터에서도 사용된다고 한다.

한참을 다른 방법을 시도하며 삽질하다가 'HAXM가 정상적으로 설치되지 않은 건가?' 라는 생각에 HAXM을 삭제했다가 다시 설치해보니 에뮬레이터가 정상적으로 실행되었다.



# :books:참고자료

- https://stackoverflow.com/questions/55969519/can-not-run-my-app-on-emulator-error-while-loading-state-for-instance-0x0-of-d
- https://iamrealizer.tistory.com/44

