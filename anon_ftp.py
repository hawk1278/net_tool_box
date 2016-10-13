#!/usr/bin/env python

import ftplib
from optparse import OptionParser
import sys


def anon_ftp(host, email):
	try:
		ftp = ftplib.FTP(hostname)
		ftp.login("anonymous", email)
		print "\n[*] {0} FTP Anonymous Login Succeeded".format(host)
		ftp.quit()
		return True
	except Exception, e:
		return False

def main():
	parser = optparser.OptionParser()
	parser.add_option("--host", dest="tgtHost", help="Anonymous FTP host")
	parser.add_option("--email", dest="tgtEmail", help="Anonymous FTP email to use.")
	(options, args) = parser.parser_args()
	if not options.tgtHost:
		parser.print_help()
		sys.exit(1)
	elif not options.tgtEmail:
		parser.print_help()
		sys.exit(1)

	anon_ftp(options.tgtHost, options.tgtEmail)


 
