#Using urllib.request to get url source code
import urllib.request

response = urllib.request.urlopen("http://edition.cnn.com")
response.read()
