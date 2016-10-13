import mechanize
from optparse import OptionParser
import sys
import cookielib

def viewPage(**kwargs):
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.set_proxies(kwargs['proxy'])
    browser.addheaders = kwargs['agent']
    #cookie_jar = cookielib.LWPCookieJar()
    #browser.set_cookiejar(cookie_jar)
    page = browser.open(kwargs['url'])
    source = page.read()
    print source

def main():
    parser = OptionParser()
    parser.add_option('-u', dest='url', help='URL to browse.')
    (options, args) = parser.parse_args()
    if not options.url:
        parser.print_help()
        sys.exit(1)
    proxy = {'http': '200.29.239.174:3128'}
    #proxy = {'https': '61.187.187.187:80'}
    url = options.url
    user_agent = [('User-agent', 'Mozilla/5.0 (X11; U; Linux 2.4.2-2 i586; en-US; m18) Geck/20010131 Netscape6/6.01')]
    viewPage(proxy=proxy, url=url, agent=user_agent)

if __name__ == "__main__":
    main()
