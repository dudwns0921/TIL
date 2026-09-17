---
type: card
title: ConstraintLayout에서 Button 배치하기 (XML View)
tags: [android]
---

# ConstraintLayout에서 Button 배치하기 (XML View)


```xml
<Button
    android:id="@+id/btn_reply"
    android:layout_width="0dp"
    android:layout_height="56dp"
    android:layout_marginTop="32dp"
    android:text="@string/detail_reply"
    app:layout_constraintTop_toBottomOf="@id/tv_title"
    app:layout_constraintStart_toStartOf="parent"
    app:layout_constraintEnd_toEndOf="parent" />
```

- `@+id/`는 id 생성, `@id/`는 참조. ViewBinding에서 `btn_reply` → `binding.btnReply`.
- ConstraintLayout 안에서 `0dp` = "제약에 맞춰 늘려라"(`width: 100%` 역할). `match_parent`는 여기서 비권장.
- `constraintTop_toBottomOf="@id/x"`로 뷰끼리 연결해 세로로 쌓는다. margin은 제약이 걸린 방향에만 적용.
- 글자 크기는 `sp`, 길이는 `dp`. 텍스트는 `strings.xml`로 빼야 경고가 안 뜬다. `tools:text`는 미리보기 전용.
- AppCompat 테마(`Theme.AppCompat.*`)에서 `<Button>`은 AppCompatButton, Material 테마면 MaterialButton으로 자동 치환된다.
- 클릭: `binding.btnReply.setOnClickListener { }` (= `onClick`). 연타 방지가 필요하면 `setOnSingleClickListener` 같은 확장 함수를 따로 만들어 쓴다.
- 실수: 제약 0개면 (0,0)에 붙는다. 참조 대상 뷰는 먼저 선언. Binding 클래스가 빨갛면 Build > Make Project.
