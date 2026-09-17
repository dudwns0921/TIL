# 컨벤션

## 커밋 메시지

기본 틀은 유디시티 커밋 메시지 컨벤션을 따름.

### 타입

#### docs

TIL 문서 관련 모두 작업은 docs 타입

##### 예시

`docs: [방송통신대학교] (3학년 1학기) 운영체제 7강 작성`

위 예시에서 소분류는 생략 가능하며, 여러 개 작성할 수도 있다.

### chore

그 외 모든 작업은 chore 타입으로 작성

##### 예시

`chore: 기존 TIL 저장소 백업 ` 

### 기타

- 동일 주제에 대해 여러 문서를 작성할 경우

  ##### 예시

  ```bash
  docs: [FlowType]
  
  - Flow Language Support 이슈
  - Visual Studio 설정
  - .flowconfig 파일 설정
  ```

  
## 폴더 구조

- 최상위 폴더 하나 = 주제 하나 (`React`, `Git`, `Android`). 주제 안에서 묶음이 생기면 하위 폴더를 둔다 (`Vue/Pinia`, `Java/Spring`, `Android/cards`).
- 파일명은 `주제_제목.md` (`React_Effect.md`). 접두어 덕분에 Obsidian 에서 노트 이름이 겹치지 않는다. 하위 폴더 안에서는 접두어를 생략해도 된다.
- 주제 폴더마다 `README.md` 에 글 목록을 둔다. 새 글을 쓰면 그 폴더 README 에 한 줄, 새 주제면 루트 README 에도 한 줄.
- 이미지는 그 글이 있는 폴더의 `md-images/` 에 두고 `./md-images/파일명` 으로 건다. 역슬래시(`.\md-images\`)와 절대 경로(`C:\...`)는 GitHub 에서 깨진다.
- GitHub 은 링크의 대소문자를 가린다. 링크는 실제 파일명과 철자까지 같게 쓴다.
- 커밋 전에 `python3 scripts/check_links.py` 로 깨진 링크를 확인한다.

## Obsidian

- 이 저장소 루트를 그대로 볼트로 연다. `.obsidian/` 설정은 커밋하되 작업 상태(`workspace*.json`)는 `.gitignore` 로 뺐다.
- 링크는 위키링크(`[[ ]]`)가 아니라 상대 경로 마크다운 링크로 쓴다. GitHub 과 Obsidian 양쪽에서 열린다.
  Obsidian 설정 → 파일 및 링크 → "위키링크 사용" 끔, "새 링크 형식" 을 상대 경로로.
- 회사 코드나 사내 정보가 들어간 노트는 이 저장소에 두지 않는다. 공개 저장소다.
