import requests
req = requests.get('https://www.w3resource.com/python-exercises/web-scraping/web-scraping-exercise-1.php')
if req.status_code == 200:
  print('Page found')
else:
  print('404 Page not found')
