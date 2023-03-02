import urllib.request
url = "https://www.python.org"
tomi = urllib.request.urlopen(url).getcode()
if tomi == 200:
    print("Congratulations, the website is on")
else:
    print("Sorry your website is not on")