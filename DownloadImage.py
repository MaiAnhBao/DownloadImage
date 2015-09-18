from bs4 import BeautifulSoup as bs
# from BeautifulSoup import BeautifulSoup as bs
from urllib.parse import urlparse
from urllib.request import urlopen
from urllib.request import urlretrieve
import os
import sys
import gzip
import shutil
import urllib.parse
from time import sleep
 
def main(url, out_folder="/test/"):
#    """Downloads all the images at 'url' to /test/"""
    soup = bs(urlopen(url), "html.parser")
    parsed = list(urlparse(url))
    
    for image in soup.findAll("img"):
        print( "Image: %(src)s" % image)
        filename = image["src"].split("/")[-1]
#        filename = filename[:-4] + str(i) + filename[-4:]
        
#        parsed[2] = image["src"]
        outpath = os.path.join(out_folder, filename)
        outpath = outpath 
#             outpath = outpath[:-4] + str(i) + outpath[-4:]
#             print(outpath)
        if image["src"].lower().startswith("http"):
                urlretrieve(image["src"], outpath)
        #else:
         #   urlretrieve(url.parse(parsed), outpath)
  
def _usage():
    print( "usage: python dumpimages.py http://example.com [outpath]")
  
# if __name__ == "__main__":
#     url = "http://blogtruyen.com/truyen/sweet-guy/chap-" 
#     out_folder = "C://Test//SweetGuy"
#     for i in range(3,30):
#             url1 = url + str(i)
#             outfolder1 = out_folder + str(i)
#             if not os.path.exists(outfolder1):
#                 os.makedirs(outfolder1)
#             if not url1.lower().startswith("http"):
#                 _usage()
#                 sys.exit(-1)
#             main(url1, outfolder1)

#os.listdir("somedirectory")
# params = urlparse('application/rss+xml')
# params = params.encode('utf-8')
#page = urlopen("http://www.dantri.com.vn", "html")

import webbrowser

url = 'http://dantri.com.vn/'

soup = bs(urlopen("http://dantri.com.vn/giai-tri.htm"),"html.parser")

for link in soup.findAll('a'):
    if 'giai-tri' in link['href']:
        webbrowser.open_new_tab(url + link["href"])
        print(link["href"])
        sleep(100)
#, type='application/rss+xml'

# import urllib, urllib2, cookielib
# 
# username = 'myuser'
# password = 'mypassword'
# 
# cj = cookielib.CookieJar()
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
# login_data = urllib.urlencode({'username' : username, 'j_password' : password})
# opener.open('https://projecteuler.net/sign_in', login_data)
# resp = opener.open('https://projecteuler.net/sign_in')
# print resp.read()
print("Done!")