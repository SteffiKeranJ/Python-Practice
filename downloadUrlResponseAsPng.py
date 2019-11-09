import requests
url = 'https://en.wikipedia.org/robots.txt'
r = requests.get(url) 
with open('result.png', 'wb') as f:
  f.write(r.content)
