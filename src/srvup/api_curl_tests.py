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



curl -X POST -d "text='NEW CHILD COMMENT'&user=1&parent=135" http://127.0.0.1:8000/api/comments/.json -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImptaXRjaGVsMyIsInVzZXJfaWQiOjEsImVtYWlsIjoiY29kaW5nZm9yZW50cmVwcmVuZXVyc0BnbWFpbC5jb20iLCJleHAiOjE0MjQ5NDI4MjV9.9H5fKOiOzN7-kCOjYaaYeLn0MvI0HrkujCwyb5l-R5E"
{"url":"http://127.0.0.1:8000/api/comments/136/.json","id":136,"children":[],"user":1,"video":null,"text":"'Some text'"}


curl -X POST -d "text='NEW CHILD COMMENT'&user=1&parent=http://127.0.0.1:8000/api/comments/135/" http://127.0.0.1:8000/api/comments/.json -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImptaXRjaGVsMyIsInVzZXJfaWQiOjEsImVtYWlsIjoiY29kaW5nZm9yZW50cmVwcmVuZXVyc0BnbWFpbC5jb20iLCJleHAiOjE0MjQ5NDI4MjV9.9H5fKOiOzN7-kCOjYaaYeLn0MvI0HrkujCwyb5l-R5E"
{"url":"http://127.0.0.1:8000/api/comments/139/.json","id":139,"children":[],"parent":"http://127.0.0.1:8000/api/comments/135/.json","user":1,"video":null,"text":"'NEW CHILD COMMENT'"}






