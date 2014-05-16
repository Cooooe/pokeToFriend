# -*- coding:utf-8 -*-

import mechanize
import sys
import signal

class Poke : 
	def __init__(self) :
		self.c = 0;
		pass

	def startPoke(self) :
		browser = mechanize.Browser()
		browser.set_handle_robots(False)
		cookies = mechanize.CookieJar()

		browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US)     AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
		browser.open("http://m.facebook.com/")
		browser.select_form(nr=0)

		user = sys.argv[1]
    		passw = sys.argv[2]

    		browser.form['email'] = user
    		browser.form['pass'] = passw

    		response = browser.submit()

    		self.poking(browser)
	def signal_handler(*args):
		print '\nYou pressed Ctrl+C!'
		sys.exit(0)
		
    	def poking(self, br) : 
    		while True : 
    			try : 
				br.open("https://m.facebook.com/pokes/")
				br._factory.is_html = True

				for link in br.links(text_regex="나도 콕 찔러보기"):
					br.follow_link(link)
					br._factory.is_html = True

					print "POKE! - " + str(self.c)
					self.c = self.c + 1
			except KeyboardInterrupt : 
				pass;


if __name__ == "__main__" : 
	poke = Poke()
	signal.signal(signal.SIGINT, poke.signal_handler)
	poke.startPoke()
