import urllib
import urllib2

url = 'http://voyager.gsfc.nasa.gov/cgi-bin/heliopause_all'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:15.0) Gecko/20100101 Firefox/15.0.1'
values = {
		  'average' : '6hour',
    	  'syear' : '9999',
		  'smonth' : '9999',
		  'sday' : '9999',
		  'eyear' : '9999',
		  'emonth' : '9999',
		  'eday' : '9999',
          'sat' : '1',
          'mnemonic' : '%3E+70+MeV%2Fnuc+Ions',
          'duration' : '3-months',
          'outputType' : 'list',
          'timeFormat' : 'ISO'
          }
headers = { 'User-Agent' : user_agent }

data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
the_page = response.read()          

	