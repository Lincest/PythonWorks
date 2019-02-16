import requests
from urllib.request import urlretrieve
import re
import time

def geturl(url):
    requ = requests.get(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'})
    req = requ.text
    regexname = re.compile(r'_shd\.mp4\?(.*?)</a>')
    regexgetname=re.compile(r'cb550>(.*)')
    regexmp4 = re.compile(r'href=(.*_shd?.mp4)')
    prename = regexname.findall(req)
    name=[]
    list=[]
    for i in prename:
        name += regexgetname.findall(i)
    load = regexmp4.findall(req)
    for i in range(len(name)):
        list +=(name[i],load[i])
    print(list)
    return list


def download(list):
    filename= r'C:\Users\47461\Desktop\DownloadVedio\\'
    for i in range(0,len(list),2):
        name=list[i]
        url=list[i+1]
        local = filename+name+'.mp4'
        try:
            print("\""+name+"\""+"已经开始下载")
            urlretrieve(url,local,reporthook=callback)
            print("\""+name+"\""+"已经下载完成")
        except:
            pass


def callback(count,blockSize,totalSize):  #下载进度回调函数，count表示已下载的个数，blocksize为已经下载的大小，totalsize为总大小
    if not count:
        print("开始下载")
    if totalSize<0:
        print("要下载的文件大小为0")
    else:
        per = 100*count*blockSize/totalSize
        if per>100:
            per=100
        print("-----当前已下载："+'%.2f%%' % per + "-----")
        if per==100:
            return True

list = geturl(r'http://www.feemic.cn/mooc/icourse163/1002161029?type=hot')
if list:
    print("开始下载")
    download(list)
    print("下载完成")