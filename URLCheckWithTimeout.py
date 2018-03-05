import urllib
from socket import timeout
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

url = 'http://www.foo.net/'

try:
    response = urllib.request.urlopen(url, timeout=10).read().decode('utf-8')
except (HTTPError, URLError) as error:
    print('Data of %s not retrieved because %s\nURL: %s', name, error, url)
except timeout:
    print('socket timed out - URL %s', url)
else:
    print('Access successful.')