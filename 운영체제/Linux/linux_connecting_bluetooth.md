# linux

## Bluetooth 연결하기

linux에서 airpod을 연결할 때 어려움이 있어서 그 과정을 기록한다. 

```bash
sudo vi /etc/bluetooth/main.conf
sudo /etc/init.d/bluetooth restart
```

- 블루투스 설정 파일 편집기로 열기
- ControllerMode의 값을 dual 혹은 bredr로 변경 (에어팟 문제 있을시)
  - ContollerMode를 사용하면 통신하려는 장치 유형에 따라 Bluetooth 동작을 최적화 가능
- 블루투스 재시작

# :books:참고 자료

https://velog.io/@jinyongp/%EB%A6%AC%EB%88%85%EC%8A%A4%EC%97%90%EC%84%9C-Bluetooth-%EC%97%B0%EA%B2%B0%EC%9D%B4-%EC%95%88-%EB%90%A0-%EB%95%8C