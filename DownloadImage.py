from bs4 import BeautifulSoup as bs
# from BeautifulSoup import BeautifulSoup as bs
from urllib.parse import urlparse
from urllib.request import urlopen
from urllib.request import urlretrieve
import os
import sys
 
def main(url, out_folder="/test/"):
#    """Downloads all the images at 'url' to /test/"""
    soup = bs(urlopen(url), "html.parser")
    parsed = list(urlparse(url))
   
    for image in soup.findAll("img"):
        #print( "Image: %(src)s" % image)
        filename = image["src"].split("/")[-1]
        parsed[2] = image["src"]
        outpath = os.path.join(out_folder, filename)
        if image["src"].lower().startswith("http"):
            urlretrieve(image["src"], outpath)
        #else:
         #   urlretrieve(url.parse(parsed), outpath)
  
def _usage():
    print( "usage: python dumpimages.py http://example.com [outpath]")
  
if __name__ == "__main__":
    url = "http://dantri.com.vn/van-hoa/trang-phuc-bikini-cua-cac-cuoc-thi-nhan-sac-da-thay-doi-the-nao-20150908121342385.htm"
    out_folder = "C://Test/"
    if not url.lower().startswith("http"):
        _usage()
        sys.exit(-1)
    main(url, out_folder)

print("Done!")