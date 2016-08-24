#!/usr/bin/python

import os, sys, zipfile

if __name__=="__main__":
	if len(sys.argv)<3:	
		print "Usage: unzip.py {zipfile} {encoding}"
		sys.exit(1)

	zip_filename = sys.argv[1]
	encoding = sys.argv[2]

	zf = zipfile.ZipFile(zip_filename, "r")
	for f in zf.infolist():
		#print f.filename
		localname = f.filename.decode(encoding).encode("utf-8")
		print localname
		if localname.endswith("/"):
			os.makedirs(localname)
		else:
			with open(localname, "wb") as fh:
				fh.write(zf.read(f))
	zf.close()
		

