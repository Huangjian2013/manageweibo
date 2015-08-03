#~/usr/bin/env python
#coding=utf8

try:
	import time
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

	http_headers = {'User-Agent':'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0', 'Referer':'http://weibo.com/u/5648162302', 'X-Requested-With':'XMLHttpRequest', 'Origin':'http://www.weibo.com', 'Content-Type':'application/x-www-form-urlencoded', 'Accept-Language':'zh-CN,zh;q=0.8', 'Accept':'*/*', 'Accept-Encoding':'gzip, deflate'}
	

	req  = urllib2.Request(
		url = url,
	        data = data,
        	headers = http_headers
	)


#	opener = urllib2.build_opener(req, httpHandler, httpsHandler)
#	response = opener.open(req, data)
#	req = urllib2.urlopen(url, httpHandler, httpsHandler)
	result = urllib2.urlopen(req)
	return result.read()
	

