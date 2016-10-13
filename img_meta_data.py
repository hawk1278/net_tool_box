import urllib2
from optparse import OptionParser
import sys
from bs4 import BeautifulSoup
import urlparse
import os
from os import path
import urllib
from log_it import log_it
from PIL import Image
from PIL.ExifTags import TAGS
import piexif


def parseMetaData():
    pass

def findImages(u):
    urlContent = urllib2.urlopen(u).read()
    # print urlContent
    soup = BeautifulSoup(urlContent,'html.parser')
    imgTags = soup.findAll('img')
    parser_logger.info('Found {0} images.'.format(len(imgTags)))
    return imgTags


def findFLV(u):
    urlContent = urllib2.urlopen(u).read()
    soup = BeautifulSoup(urlContent, 'html.parser')
    flvTags = soup.findAll('embed')
    flvVars = flvTags[0]['flashvars']
    vidUrl = flvVars.split('amp')[0].split('flv_url=')[1].split('&')[0]
    vidUrl = urllib.unquote(vidUrl)
    vidcontent = urllib2.urlopen(vidUrl).read()
    vidfileName = os.path.basename(vidUrl)
    vidfile = open(vidfileName, 'wb')
    vidfile.write(vidcontent)
    # vidfile.write('test')
    vidfile.close()


def downloadImages(imgTag):
    try:
        imgSrc = imgTag['src']
        imgContent = urllib2.urlopen(imgSrc).read()
        imgFileName = os.path.join(image_repo,os.path.basename(urlparse.urlsplit(imgSrc)[2]))
        imgFile = open(imgFileName, 'wb')
        imgFile.write(imgContent)
        imgFile.close()
        return imgFileName
    except Exception as e:
          return ''
          print e


def testForExif(imgFile):
    try:
	exifData = []
        inf = piexif.load(imgFile)
	#if inf.encode('utf-8'):
        print "Exif Data: "
	print inf.encode('utf-8')
	    #for (tag, value) in inf.items():
            #    print "{0} : {1}".format(tag, value)
    except:
        print "No data found."



def main():
    parser = OptionParser()
    parser.add_option('-u', '--url', dest='url', help='url to be parsed')

    (options, args) = parser.parse_args()

    if not options.url:
        parser.print_help()
        sys.exit(1)


    url = options.url
    parser_logger.info('URL to parse images from is: {0}'.format(url))
    #flvs = findFLV(url)

    for img in findImages(url):
         image_file = downloadImages(img)
	 testForExif(image_file)
    
if __name__ == "__main__":
    image_repo = os.path.join(os.curdir,'images')
    if not os.path.isdir(image_repo):
	os.mkdir(image_repo)

    logger_path = os.curdir
    parser_logger = log_it(logname="parser_log.log", logpath=logger_path, name='Image Metadata Parser Log', rotate='')
    sys.exit(main())
