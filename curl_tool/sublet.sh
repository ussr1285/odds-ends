#!/bin/bash

# 로그인하여 쿠키를 가져옵니다.
user_cookie=$(curl -X POST -s -c - "http://localhost:4000/auth/login" -d "id=test&password=Test@0525" | grep 'connect.sid' | awk '{print $7}')
echo "User cookie: $user_cookie"

for i in {1..100000}
do
  # GET 요청을 통해 게시물 데이터를 가져옵니다.
  posts=$(curl -s "http://localhost:4000/post" | jq '.[] | .key')
  if [ "$posts" == "" ]; then
    echo "No more posts to delete."
    break
  fi

  # 각 게시물에 대해 DELETE 요청을 보냅니다.
  for key in $posts; 
  do
      # key 값에서 따옴표를 제거합니다.
      key=$(echo $key | tr -d '"')
      # DELETE 요청을 보냅니다.
      curl -X DELETE "http://localhost:4000/post/$key" --cookie "connect.sid=$user_cookie"
      echo "Deleted post with key: $key"
  done
done
