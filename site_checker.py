import urllib.request as urllib

def check(url):
    try:
        response = urllib.urlopen(url)
        print(response.getcode())
    except Exception as e:
        print("Connection-failed:")
        print(e)
check("https://www.googli.com")