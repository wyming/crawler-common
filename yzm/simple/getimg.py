#coding=utf-8
#2015/04/24
#author@shibin

#import urllib2
#import urllib

import requests
import time

Mainurl='http://www.sccredit.gov.cn'
Host='www.sccredit.gov.cn'
Imgurl='http://www.sccredit.gov.cn/getYzm.do'

img_header={
    "Accept":"image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, sdch",
    "Accept-Language":'en-US,en;q=0.8',
    "Connection":"keep-alive",
    "Cookie":"JSESSIONID=V2ZFs9TNx2yTdj5SJT3B7RL7DhlhVT7vjTQv4tQlkRppwLNBMn7x!-836272584; cck_lasttime=1430182306281; cck_count=2",
    "Host":"www.sccredit.gov.cn",
    "Referer":"http://www.sccredit.gov.cn/queryInfo.do?behavior=enterSearch&panel=corp",
    "User-Agent":"MoHozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/41.0.2272.76 Chrome/41.0.2272.76 Safari/537.36" 
    }

IMGPATH='./test_data/'

def get_imgdata():
    try:
        resp=requests.get(Imgurl,headers=img_header)
        return resp.content
    except:
        return None

def main():
    for i in range(100,1000):
        imgdata=get_imgdata()
        if imgdata==None:
            time.sleep(3)
            continue
        f=open(IMGPATH+str(i)+'.jpg','w')
        f.write(imgdata)
        f.close()
        print i
        time.sleep(0.7)

if __name__ == '__main__':
    main()
