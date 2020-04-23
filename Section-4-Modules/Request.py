import requests

r = requests.get("https://www.facebook.com/")

print(r.status_code)

print(r.headers)

print(r.headers["date"])

print(r.text)

# HTTP status code
# 200 - ok
# 403 - Forbidden
# 404 - Not Found