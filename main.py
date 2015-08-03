#~/usr/bin/env python
#coding=utf8

try:
	import weibo_login
	import weibo_zan

	import time
	import urllib2

except ImportError:
	print >> sys.stderr, "Import ERROR"
	sys.exit(1)


if __name__ == '__main__':


    username =''
    pwd = ''
    cookie_file = 'weibo_login_cookies.' + username + '.dat'

    if weibo_login.login(username, pwd, cookie_file):
        print 'Login WEIBO succeeded'
        #if you see the above message, then do whatever you want with urllib2, following is a example for fetch Kaifu's Weibo Home Page
        #Trying to fetch Kaifu Lee's Weibo home page
	time.sleep(10)
        home_page = urllib2.urlopen('http://www.weibo.com').read()
        #print home_page
	time.sleep(10)

	mid = weibo_zan.get_mid()
	print mid	

	likeResponse = weibo_zan.like_mid(mid)
	print likeResponse
    else:
        print 'Login WEIBO failed'

