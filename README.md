# up9-traffic-api


### Build and Run
```bash
> docker build . -t traffic-api

> docker run -p 5000:80 -t traffic-api
```

### Example Use


```python
import requests

url = "http://localhost:5000/traffic"

querystring = {"start_date":"2021-03-08 01:04:51+00:00","end_date":"2021-03-10 01:04:52+00:00","service":"carts.sock-shop","token":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJqSEZ0R1dybjJpY084VnpDYXpaZWUyakpFc2drY1k5ZzhpN2FTbGtielRnIn0.eyJleHAiOjE2MTUyNTMyMjcsImlhdCI6MTYxNTI1MjYyNywiYXV0aF90aW1lIjoxNjE1MTI5MTAwLCJqdGkiOiJhMmJlZjM5NS0zZTg5LTRjMTItOWIzNy03YWRhYmM5MmJkOTgiLCJpc3MiOiJodHRwczovL2F1dGguc3RnLnRlc3RyLmlvL2F1dGgvcmVhbG1zL3Rlc3RyIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6Ijg4Y2RhNGE0LTgwYTYtNDk5Mi04ODQ0LTg2OTAxOTY4OGJjZCIsInR5cCI6IkJlYXJlciIsImF6cCI6InJlYWN0LWNsaWVudCIsIm5vbmNlIjoiNTNmZDUzZTUtYjEwYS00ODE2LTljZTYtYmU2Njc4NTg0NzdiIiwic2Vzc2lvbl9zdGF0ZSI6ImY2NDQwOTAxLTczZTItNDdhZi1hYWJjLTMzZjM5MDdiZTBmMiIsImFjciI6IjAiLCJhbGxvd2VkLW9yaWdpbnMiOlsiaHR0cHM6Ly9zdGcudGVzdHIuaW8iLCJjaHJvbWUtZXh0ZW5zaW9uOi8vbmFkZ2VsamVtbWJna2xkaGNwYWZqbXBtYXBpcGdsY20iLCJodHRwOi8vbG9jYWxob3N0OjMwMDAiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbIm1hbmFnZUZlYXR1cmVGbGFncyIsIm9mZmxpbmVfYWNjZXNzIiwiaW1wZXJzb25hdGVHcm91cCIsInJhd0VkaXQiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJncm91cF9tZW1iZXJzaGlwIjpbImFhYWFhYWFhLWFhYWEtYWFhYS1hYWFhLWFhYWFhYWFhYWFhYSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwibmFtZSI6IlNlbHRvbiBGaXV6YSIsInByZWZlcnJlZF91c2VybmFtZSI6InNlbHRvbkB1cDkuY29tIiwiZ2l2ZW5fbmFtZSI6IlNlbHRvbiIsImZhbWlseV9uYW1lIjoiRml1emEiLCJncm91cF9zdWJkb21haW4iOiJ1cDkiLCJlbWFpbCI6InNlbHRvbkB1cDkuY29tIiwiZ3JvdXBfbGljZW5zZSI6InBybyIsImZlYXR1cmVGbGFncyI6eyJnZW5lc2lzIjp0cnVlLCJjYWxpYnJhdGUiOnRydWV9fQ.I2HrC6_I_QOQ8E_tBO2lVQ-d56EDyZbvPxUcyuSsf08zhQtDodGFXeSM69c5D4UIPfTANwB7BJa1tIZtrugmSy1EYInjeV_61VoU0LyQlu5fjhElKzMD0eq6gjAW7a9xJ5xVJkyk3oGiNCOhaDJIhXys1vEcqzo3vXv4sJNzOKiAB1remq9Unu84kh6N6AVpq-QlCRod-OArVzUNwiwF7VSjLrLd9Hiu6D9Nysw5C5_7QDF8fNq5Kt5sc775BIs1khuSQvflqwGp2UNuQdU-4tKsHfGO4_ad_Lm-QKI7sOlFDxT4b1dCm10wUW0IpMRit0lmWYkpOTpxs-ESLnU6Vw","workspace":"selton-weavesocks"}

payload = {
    "start_date": "2021-03-08 11:57:56+0000",
    "end_date": "2021-03-10 11:59:56+0000",
    "workspace": "selton-weavesocks",
    "service": "carts.sock-shop",
    "token": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJqSEZ0R1dybjJpY084VnpDYXpaZWUyakpFc2drY1k5ZzhpN2FTbGtielRnIn0.eyJleHAiOjE2MTUyOTI4NjksImlhdCI6MTYxNTI5MjI2OSwiYXV0aF90aW1lIjoxNjE1MTI5MTAwLCJqdGkiOiI1OTYyMGFmZi1lNjJhLTRlNjEtYjVlNC01M2M5NTJlZmEzNDMiLCJpc3MiOiJodHRwczovL2F1dGguc3RnLnRlc3RyLmlvL2F1dGgvcmVhbG1zL3Rlc3RyIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6Ijg4Y2RhNGE0LTgwYTYtNDk5Mi04ODQ0LTg2OTAxOTY4OGJjZCIsInR5cCI6IkJlYXJlciIsImF6cCI6InJlYWN0LWNsaWVudCIsIm5vbmNlIjoiMjJkYzE3YTYtMjRiZi00ZDM5LTg1YTEtZjU1ODI0NDA2YTc4Iiwic2Vzc2lvbl9zdGF0ZSI6ImY2NDQwOTAxLTczZTItNDdhZi1hYWJjLTMzZjM5MDdiZTBmMiIsImFjciI6IjAiLCJhbGxvd2VkLW9yaWdpbnMiOlsiaHR0cHM6Ly9zdGcudGVzdHIuaW8iLCJjaHJvbWUtZXh0ZW5zaW9uOi8vbmFkZ2VsamVtbWJna2xkaGNwYWZqbXBtYXBpcGdsY20iLCJodHRwOi8vbG9jYWxob3N0OjMwMDAiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbIm1hbmFnZUZlYXR1cmVGbGFncyIsIm9mZmxpbmVfYWNjZXNzIiwiaW1wZXJzb25hdGVHcm91cCIsInJhd0VkaXQiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJncm91cF9tZW1iZXJzaGlwIjpbImFhYWFhYWFhLWFhYWEtYWFhYS1hYWFhLWFhYWFhYWFhYWFhYSJdLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwibmFtZSI6IlNlbHRvbiBGaXV6YSIsInByZWZlcnJlZF91c2VybmFtZSI6InNlbHRvbkB1cDkuY29tIiwiZ2l2ZW5fbmFtZSI6IlNlbHRvbiIsImZhbWlseV9uYW1lIjoiRml1emEiLCJncm91cF9zdWJkb21haW4iOiJ1cDkiLCJlbWFpbCI6InNlbHRvbkB1cDkuY29tIiwiZ3JvdXBfbGljZW5zZSI6InBybyIsImZlYXR1cmVGbGFncyI6eyJnZW5lc2lzIjp0cnVlLCJjYWxpYnJhdGUiOnRydWV9fQ.J-cTSeyQMdXZ8nzUjDOyt4G9UGiDYDR1N-cYzmKOA7L0WEHjEfOpQestBGi-8KpT-nE9D-1jjXEpc_h-noDRYcBB-JLhJV0p4DHJtWeCDKzylJBi2meiQeiq8cxdWGUGcyldhkM5c5cHuFdXC5DBAghPPpWUaN4TS_TuEQ9-S15fDnPgLhjXjzwygxaR_JqTFQUqj6BLKFQR4DcWdMXqTZKxM_LO97s1bP9XXvb_bBUWcVIhnecnCM-GraqKrAuSZwXV_IMB9LejZFfxaY5t2jjpJOS9m6IxYM5uxupPz7JmvFYpFfm4ntwifwo7v6w1_h71kvrDcO5YN3XG62bzbw"
}
headers = {"Content-Type": "application/json"}

response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

print(response.text)
```
