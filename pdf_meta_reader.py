"""
To Do:
- Create a gtk-tkinter interface for this
- Create a way to populate metadata for may files at once
- Create a way to read metadata from text or command line argument
"""


import os
import sys
import optparse
from PyPDF2 import PdfFileReader, PdfFileMerger


def get_meta(pdf_file):
    """
    Name: get_meta
    Attributes: pdf_file ( name of pdf file to get data from )
    Description:
    get_meta reads the document meta data and xmp info.
    Only the document info is returned.
    """
    pdfFile = PdfFileReader(file(pdf_file, 'rb'))
    docInfo = pdfFile.getDocumentInfo()
    xmpInfo = pdfFile.getXmpMetadata()
    if xmpInfo:
	print xmpInfo

    return docInfo


def print_meta(pdf_meta):
    """
    Name: print_meta
    Attributes: pdf_meta ( dictionary of meta data)
    Description: 
    Does what it says it does.
    """
    for item in pdf_meta:
		print "{0}: {1}".format(item.encode('utf-8'), pdf_meta[item].encode('utf-8'))


def mod_meta(pdf_meta, pdf_file):
	"""
	Name: mod_meta
	Attributes: dictionary of meta data and pdf file name
	Description:
	mod_meta takes a dictionary of meta data and changes the values.
	A merger object against an existing pdf whose name is passed in to the function.
	The merger object is set to append and the new modified meta data is written to it.
	A new pdf file is created using the contents of the current pdf file and the modified meta data.
	The new file is renamed to the old file to completely replace the old file.
	"""
	merger = PdfFileMerger()
	meta_fields = [x for x in pdf_meta ]
	new_data = ' ' * len(meta_fields)
	meta_data = dict(zip(meta_fields,new_data))
	with open(pdf_file, 'rb') as f0:
	    merger.append(f0)
	merger.addMetadata(meta_data)

	with open('test.pdf','wb') as f1:
	    merger.write(f1)

	os.rename('test.pdf',pdf_file)


def main():
    parser = optparse.OptionParser()
    parser.add_option('-f', '--file', dest='fn', help="PDF file to scan.")
    (options, args) = parser.parse_args()

    if not options.fn:
        parser.print_help()
        sys.exit(1)
    fn = options.fn
    #print "Old meta data: "
    print "meta data: "
    print_meta(get_meta(fn))
    #mod_meta(get_meta(fn), fn)
    #print "\nNew meta data: "
    #print_meta(get_meta(fn))


if __name__ == "__main__":
    main()
