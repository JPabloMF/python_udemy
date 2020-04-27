import requests

params = {"q": "pizza"}
r = requests.get('https://www.bing.com/search', params=params)
print("Status:",r.status_code)

f = open("E:\\Desarrollo\\PROGRAMMING COURSES\\PYTHON\\UDEMY\\Essential Module-Requests\\page.html","w+")
f.write(r.text)
