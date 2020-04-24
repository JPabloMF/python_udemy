import requests

r = requests.get('http://www.google.com.co')
print("Status:",r.status_code)

f = open("E:\\Desarrollo\\PROGRAMMING COURSES\\PYTHON\\UDEMY\\Essential Module-Requests\\page.html","w+")
f.write(r.text)
