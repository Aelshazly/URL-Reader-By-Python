import urllib.request

webUrl = urllib.request.urlopen('https://s-m.com.sa/tr/v.html')

print("result code: " + str(webUrl.getcode()))

data = webUrl.read()
print(data)
