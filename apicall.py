#API call to get personal connection details //python2
from urllib2 import Request, urlopen, URLError

request = Request('http://ipinfo.io/json')
try:
    response = urlopen(request)
    clientdetails = response.read()
    print "Details of this machine: \n" + clientdetails
except URLError, error:
    print 'Error retrieving client details', error
