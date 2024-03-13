#!/bin/bash

# 현재 디렉토리의 파일 중에서 "(2)"를 포함하는 파일들을 찾아서 반복 처리
for file in *\(2\)*; do
    # 새 파일명 생성: "(2)" 문자열을 제거
    new_name=$(echo "$file" | sed 's/(2)//g')
    # 파일명 변경
    mv "$file" "$new_name"
done

