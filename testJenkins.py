import sys
import urllib2
import base64

username = releaseVariables['user']
password = releaseVariables['password']
url = releaseVariables['url']

request = urllib2.Request(url)
b64auth = base64.standard_b64encode("%s:%s" % (username,password))
request.add_header("Authorization", "Basic %s" % b64auth)

try:
 result = urllib2.urlopen(request)
 status=result.read()
 print(status)
 if (status.find("RUNNING") == -1):
   sys.exit(1)
except urllib2.HTTPError as e :
 print e.code
 sys.exit(1)
