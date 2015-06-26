 curl -X POST -d "username=jmitchel3&password=123" http://127.0.0.1:8000/api/auth/token/

{"active":true,
	"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImptaXRjaGVsMyIsInVzZXJfaWQiOjEsImVtYWlsIjoiY29kaW5nZm9yZW50cmVwcmVuZXVyc0BnbWFpbC5jb20iLCJleHAiOjE0MjQ5NDI4MjV9.9H5fKOiOzN7-kCOjYaaYeLn0MvI0HrkujCwyb5l-R5E",
	"user":"jmitchel3"}




 curl -X POST -d "text='Some text'" http://127.0.0.1:8000/api/comments/.json
 {"detail":"Authentication credentials were not provided."}


 curl -X POST -d "text='Some text'" http://127.0.0.1:8000/api/comments/.json -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImptaXRjaGVsMyIsInVzZXJfaWQiOjEsImVtYWlsIjoiY29kaW5nZm9yZW50cmVwcmVuZXVyc0BnbWFpbC5jb20iLCJleHAiOjE0MjQ5NDI4MjV9.9H5fKOiOzN7-kCOjYaaYeLn0MvI0HrkujCwyb5l-R5E"

 {"user":["This field is required."]}

curl -X POST -d "text='Some text'&user=jmitchel3" http://127.0.0.1:8000/api/comments/.json -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImptaXRjaGVsMyIsInVzZXJfaWQiOjEsImVtYWlsIjoiY29kaW5nZm9yZW50cmVwcmVuZXVyc0BnbWFpbC5jb20iLCJleHAiOjE0MjQ5NDI4MjV9.9H5fKOiOzN7-kCOjYaaYeLn0MvI0HrkujCwyb5l-R5E"
{"user":["Incorrect type. Expected pk value, received unicode."]}

curl -X POST -d "text='Some text'&user=1" http://127.0.0.1:8000/api/comments/.json -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImptaXRjaGVsMyIsInVzZXJfaWQiOjEsImVtYWlsIjoiY29kaW5nZm9yZW50cmVwcmVuZXVyc0BnbWFpbC5jb20iLCJleHAiOjE0MjQ5NDI4MjV9.9H5fKOiOzN7-kCOjYaaYeLn0MvI0HrkujCwyb5l-R5E"
{"url":"http://127.0.0.1:8000/api/comments/133/.json","id":133,"children":[],"user":1,"text":"'Some text'"}

curl -X DELETE http://127.0.0.1:8000/api/comments/133/.json -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImptaXRjaGVsMyIsInVzZXJfaWQiOjEsImVtYWlsIjoiY29kaW5nZm9yZW50cmVwcmVuZXVyc0BnbWFpbC5jb20iLCJleHAiOjE0MjQ5NDI4MjV9.9H5fKOiOzN7-kCOjYaaYeLn0MvI0HrkujCwyb5l-R5E"

#return nil


#GET
curl http://127.0.0.1:8000/api/comments/133/.json -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImptaXRjaGVsMyIsInVzZXJfaWQiOjEsImVtYWlsIjoiY29kaW5nZm9yZW50cmVwcmVuZXVyc0BnbWFpbC5jb20iLCJleHAiOjE0MjQ5NDI4MjV9.9H5fKOiOzN7-kCOjYaaYeLn0MvI0HrkujCwyb5l-R5E"
{"detail":"Not found"}



curl -X POST -d "text='Some text'&user=1&video=24" http://127.0.0.1:8000/api/comments/.json -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImptaXRjaGVsMyIsInVzZXJfaWQiOjEsImVtYWlsIjoiY29kaW5nZm9yZW50cmVwcmVuZXVyc0BnbWFpbC5jb20iLCJleHAiOjE0MjQ5NDI4MjV9.9H5fKOiOzN7-kCOjYaaYeLn0MvI0HrkujCwyb5l-R5E"
{"video":["Invalid hyperlink - No URL match"]}

curl -X POST -d "text=This is some great video AGAIN&user=1&video=http://127.0.0.1:8000/api/videos/24/" http://127.0.0.1:8000/api/comments/.json -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImptaXRjaGVsMyIsInVzZXJfaWQiOjEsImVtYWlsIjoiY29kaW5nZm9yZW50cmVwcmVuZXVyc0BnbWFpbC5jb20iLCJleHAiOjE0MjQ5NDI4MjV9.9H5fKOiOzN7-kCOjYaaYeLn0MvI0HrkujCwyb5l-R5E"
{"url":"http://127.0.0.1:8000/api/comments/135/.json","id":135,"children":[],"user":1,"video":"http://127.0.0.1:8000/api/videos/24/.json","text":"This is some great video AGAIN"}



curl -X POST -d "text=Even newer&user=1&parent=229" http://127.0.0.1:8000/api/comments/.json -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImptaXRjaGVsMyIsInVzZXJfaWQiOjEsImVtYWlsIjoiY29kaW5nZm9yZW50cmVwcmVuZXVyc0BnbWFpbC5jb20iLCJleHAiOjE0MzUwOTExMTV9.ZKrCIMvcj32RNrV9f26A7Zsz15bfC6tePErjfMXGeYk"
{"url":"http://127.0.0.1:8000/api/comments/136/.json","id":136,"children":[],"user":1,"video":null,"text":"'Some text'"}


curl -X POST -d "text='NEW CHILD COMMENT'&user=1&parent=http://127.0.0.1:8000/api/comments/135/" http://127.0.0.1:8000/api/comments/.json -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImptaXRjaGVsMyIsInVzZXJfaWQiOjEsImVtYWlsIjoiY29kaW5nZm9yZW50cmVwcmVuZXVyc0BnbWFpbC5jb20iLCJleHAiOjE0MjQ5NDI4MjV9.9H5fKOiOzN7-kCOjYaaYeLn0MvI0HrkujCwyb5l-R5E"
{"url":"http://127.0.0.1:8000/api/comments/139/.json","id":139,"children":[],"parent":"http://127.0.0.1:8000/api/comments/135/.json","user":1,"video":null,"text":"'NEW CHILD COMMENT'"}



#API 2 with CBViews

curl -X POST -d "text='NEW CHILD COMMENT'&user=1&parent=http://127.0.0.1:8000/api2/comment/135/" http://127.0.0.1:8000/api2/comment/133/ -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImptaXRjaGVsMyIsInVzZXJfaWQiOjEsImVtYWlsIjoiY29kaW5nZm9yZW50cmVwcmVuZXVyc0BnbWFpbC5jb20iLCJleHAiOjE0MjUwMjExNjR9.3OtWG20Dx1hl4vSaznokkuW9fBee4MBYfM742b1G2vA"
{"detail":"Method 'POST' not allowed."}


curl -X DELETE -d "text='NEW CHILD COMMENT'&user=1&parent=http://127.0.0.1:8000/api/comments/135/" http://127.0.0.1:8000/api2/projects/djangogap/ -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImptaXRjaGVsMyIsInVzZXJfaWQiOjEsImVtYWlsIjoiY29kaW5nZm9yZW50cmVwcmVuZXVyc0BnbWFpbC5jb20iLCJleHAiOjE0MjUwMjExNjR9.3OtWG20Dx1hl4vSaznokkuW9fBee4MBYfM742b1G2vA"
{"detail":"Method 'DELETE' not allowed."}


curl -X PUT -d "text='NEW CHILD COMMENT'&user=1&parent=http://127.0.0.1:8000/api/comments/135/" http://127.0.0.1:8000/api2/projects/djangogap/ -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImptaXRjaGVsMyIsInVzZXJfaWQiOjEsImVtYWlsIjoiY29kaW5nZm9yZW50cmVwcmVuZXVyc0BnbWFpbC5jb20iLCJleHAiOjE0MjUwMjExNjR9.3OtWG20Dx1hl4vSaznokkuW9fBee4MBYfM742b1G2vA"
{"detail":"Method 'PUT' not allowed."}

curl http://127.0.0.1:8000/api2/projects/djangogap/ -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImptaXRjaGVsMyIsInVzZXJfaWQiOjEsImVtYWlsIjoiY29kaW5nZm9yZW50cmVwcmVuZXVyc0BnbWFpbC5jb20iLCJleHAiOjE0MjUwMjExNjR9.3OtWG20Dx1hl4vSaznokkuW9fBee4MBYfM742b1G2vA"
{"url":"http://127.0.0.1:8000/api2/projects/djangogap/","id":2,"slug":"djangogap","title":"DjangoGap","description":"","image":"http://127.0.0.1:8000/media/images/djangogap.png"}

curl http://127.0.0.1:8000/api2/projects/djangogap/
{"detail":"Authentication credentials were not provided."}


curl -X PUT -d "text=YET ANOTHER AWESOME NEW COMMENT" http://127.0.0.1:8000/api2/comment/135/ -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImptaXRjaGVsMyIsInVzZXJfaWQiOjEsImVtYWlsIjoiY29kaW5nZm9yZW50cmVwcmVuZXVyc0BnbWFpbC5jb20iLCJleHAiOjE0MjU0NTc1ODV9.5aA5mTmyuoMI0BhMYPL03qI-vwnE-pSzWe-14yDMnS8"
{"id":135,"user":"jmitchel3","text":"'YET ANOTHER AWESOME NEW COMMENT'"}


curl -X DELETE http://127.0.0.1:8000/api2/comment/143/ -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImptaXRjaGVsMyIsInVzZXJfaWQiOjEsImVtYWlsIjoiY29kaW5nZm9yZW50cmVwcmVuZXVyc0BnbWFpbC5jb20iLCJleHAiOjE0MjU0NTc1ODV9.5aA5mTmyuoMI0BhMYPL03qI-vwnE-pSzWe-14yDMnS8"
{"detail":"You do not have permission to perform this action."}

curl -X DELETE http://127.0.0.1:8000/api2/comment/142/ -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImptaXRjaGVsMyIsInVzZXJfaWQiOjEsImVtYWlsIjoiY29kaW5nZm9yZW50cmVwcmVuZXVyc0BnbWFpbC5jb20iLCJleHAiOjE0MjU0NTc1ODV9.5aA5mTmyuoMI0BhMYPL03qI-vwnE-pSzWe-14yDMnS8"
#returned 204


curl -X POST -d "text='NEW COMMENT'&user=1&parent=229" http://127.0.0.1:8000/api2/comment/create/ -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImptaXRjaGVsMyIsInVzZXJfaWQiOjEsImVtYWlsIjoiY29kaW5nZm9yZW50cmVwcmVuZXVyc0BnbWFpbC5jb20iLCJleHAiOjE0MzUwOTExMTV9.ZKrCIMvcj32RNrV9f26A7Zsz15bfC6tePErjfMXGeYk"
{"text":"'NEW COMMENT'","user":1,"video":null,"parent":146}


curl -X PUT -d "text=YET ANOTHER AWESOME NEW COMMENT" http://127.0.0.1:8000/api2/comment/147/ -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImptaXRjaGVsMyIsInVzZXJfaWQiOjEsImVtYWlsIjoiY29kaW5nZm9yZW50cmVwcmVuZXVyc0BnbWFpbC5jb20iLCJleHAiOjE0MjU0NTc1ODV9.5aA5mTmyuoMI0BhMYPL03qI-vwnE-pSzWe-14yDMnS8"

curl -X DELETE http://127.0.0.1:8000/api2/comment/147/ -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImptaXRjaGVsMyIsInVzZXJfaWQiOjEsImVtYWlsIjoiY29kaW5nZm9yZW50cmVwcmVuZXVyc0BnbWFpbC5jb20iLCJleHAiOjE0MjU0NTc1ODV9.5aA5mTmyuoMI0BhMYPL03qI-vwnE-pSzWe-14yDMnS8"


curl -X POST -d "text=YEAHH IT's working&user=1&video=23" http://127.0.0.1:8000/api2/comment/create/ -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImptaXRjaGVsMyIsInVzZXJfaWQiOjEsImVtYWlsIjoiY29kaW5nZm9yZW50cmVwcmVuZXVyc0BnbWFpbC5jb20iLCJleHAiOjE0MjU0NTc1ODV9.5aA5mTmyuoMI0BhMYPL03qI-vwnE-pSzWe-14yDMnS8"




