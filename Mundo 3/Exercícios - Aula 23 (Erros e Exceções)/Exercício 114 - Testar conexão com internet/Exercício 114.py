import urllib
import urllib.request
from matematico import red, green

try:
    site = urllib.request.urlopen('https://www.youtube.com/')
except:
    red('O site não está acessível')
else:
    green('O site está acessível')
