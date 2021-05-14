import sys
import urllib2
import base64

username = "admin"
password = "abscde45"
url = 'http://192.168.1.25:4516/deployit/server/state'

request = urllib2.Request(url)
b64auth = base64.standard_b64encode("%s:%s" % (username,password))
request.add_header("Authorization", "Basic %s" % b64auth)
result = urllib2.urlopen(request)

status=result.read()

print(status)

if (status.find("RUNNING") == -1):
   sys.exit(1)

