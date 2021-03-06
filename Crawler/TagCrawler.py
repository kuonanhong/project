#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2016年6月9日

@author: kazimir
'''
import requests
from bs4 import BeautifulSoup
import time
import re
from Requester import Requester
class TagCrawler(Requester) :
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.\
                94 Safari/537.36'
               }
    def __init__(self , url) :          #設定TagCrawler建構子
        self.url = url                  #啟動url
                        
    def allsubCraw(self):
        soup = super(TagCrawler,self).req(self.url)
        root ={}
        for url in soup.select('.more a'):  
            root[url.text] = url['href']
        return  root 
    def leafCraw(self,bigUrl):
        soup = super(TagCrawler,self).req(bigUrl)
        leafUrl = []
        rg = 'leaf'
        for url in soup.select('.title'):            
            isLeaf=re.search(rg,url['href'])
            try:
                isLeaf.group()              #y拍的小項網址裡面會有leaf這個字，利用這點濾掉不是小項的網址
                leafUrl.append(url['href'])
            except:
                   continue
        return leafUrl
    def startCraw(self):
        tc = TagCrawler('https://tw.bid.yahoo.com/tw/0-all.html?.r=1465414707')    
        root = tc.allsubCraw()
        leafUrl=[]    
        for url in root:
            leafUrl.extend(tc.leafCraw(root[url]))
        print len(leafUrl)
    # if main 裡面是單獨測試碼，直接執行可以得到測試結果                          
if __name__ == '__main__':
    tc = TagCrawler('https://tw.bid.yahoo.com/tw/0-all.html?.r=1465414707')    
    root = tc.allsubCraw()
    leafUrl=[]    
    for url in root:
        leafUrl.extend(tc.leafCraw(root[url]))
    print len(leafUrl)
    
    