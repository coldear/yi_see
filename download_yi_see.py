#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import re
import time

def StartDownload(startUrl, output):
    """ start to download from yi-see from startUrl """
    link = startUrl
    while True:        
        print "downloading " + link
        html = GetHtml(link)
        if html == None:
            break
        print "downloaded " + link
        GetText(html, output)
        newLink = GetNext(link, html)
        if (newLink == None):
            break
        link = newLink
        time.sleep(1)
    print "finish"
    

def GetHtml(url):
    sock = urllib.urlopen(url)
    html = sock.read()
    sock.close()
    return html

def GetText(html, output):
    pa = re.compile(r'td class=art>(.*?)<div class=FL>', re.U | re.I | re.S)
    ma = pa.search(html)
    if ma == None:
        return None
    text = ma.group(1).replace(r'<br>', ' ')
    f = open(output, 'a+')
    f.write(text)
    f.write("\r\n")
    f.close()
    print "text extracted.."
    return text

def GetNext(base, html):
    ma = re.search(r'href=.([^\']*)\'>下一页</a>', html, re.U | re.S |re.I)
    if ma == None:
        return None
    return urllib.basejoin(base, ma.group(1))
    
if __name__=="__main__":
    StartDownload("http://www.yi-see.com/read_139860_8237.html", "d:\\output.txt")
