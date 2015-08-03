#~/usr/bin/env python
#coding=utf8

try:
	import urllib
	import urllib2
except ImportError:
	print >> sys.stderr, "Import ERROR"
	sys.exit(1)


def get_mid():
	user_page = urllib2.urlopen('http://www.weibo.com/5648162302').read()

	midIndex = user_page.find('mid=\\\"')
	startIndex = midIndex + 6
	midEndIndex = user_page.find('\\\"', startIndex)
	mid = user_page[startIndex : midEndIndex]
	
	return mid

def like_mid(mid):
	url = 'http://www.weibo.com/aj/v6/like/add?ajwvr=6'
	data = {'version':'mini', 'qid':'heart', 'loc':'profile','location':'page_100505_home'}
	data['mid'] = mid
	data = urllib.urlencode(data)
	print data
	http_headers = {'User-Agent':'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0'}
	req  = urllib2.urlopen(
		url = url,
	        data = data,
#        	headers = http_headers
	)

#	httpHandler = urllib2.HTTPHandler(debuglevel=1)
#	httpsHandler = urllib2.HTTPSHandler(debuglevel=1)

#	opener = urllib2.build_opener(httpHandler, httpsHandler)
#	response = opener.open(req, data)
	return req.read()
	
	

