import re
import urllib
import urllib.request
from collections import deque

def getallemail(data):  #邮箱的正则表达式获取所有的邮箱
    try:
        mailregex = re.compile(r"([A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4})", re.IGNORECASE)
        mylist = mailregex.findall(data)
        return mylist
    except:
        return []


def getdata(url):   #用utf-8编码读取url返回网页源代码
    try:
        data = urllib.request.urlopen(url).read().decode("utf-8")
        return data
    except:
        return ""


def geteveryurl(data):  #获得网页所有的url
    alllist = []
    mylist1 = getallhttp(data)
    mylist2 = []
    if len(mylist1)>0:
        mylist2 = getabsurl(mylist1[0],data)    #mylist[0]作用是提取元素
    alllist.extend(mylist1)
    alllist.extend(mylist2)
    return alllist


def gethostname(httpstr):
    try:
        mailregex = re.compile(r"(http://\S*?)/",re.IGNORECASE) #预编译提取主机名的regex
        mylist = mailregex.findall(httpstr)
        if len(mylist)==0:
            return None
        else:
            return mylist[0]
    except:
        return None


def getabsurl(url,data):
    try:
        regex = re.compile("href=\"(.*?)\"",re.IGNORECASE) #预编译提取href正则表达式
        httplist = regex.findall(data)
        newhttplist = httplist.copy()  #进行一次深拷贝，以进行后面的删除行为
        for data in newhttplist:
            if data.find("http://")!=-1:  #如果其中包含http
                httplist.remove(data) #在原list中remove此data
            if data.find("javascript")!=-1:
                httplist.remove(data) #同理
        hostname = gethostname(url)
        if hostname!=None:
            for i in range(len(httplist)):
                httplist[i] = hostname + httplist[i]
        return httplist
    except:
        return []


def getallhttp(data):#找到所有的http
    try:
        mailregex = re.compile(r"(http://\S*?)[\"|>|)]",re.IGNORECASE)
        mylist = mailregex.findall(data)
        return mylist
    except:
        return[]


def BFS(urlstr):
    urlqueue = deque([]) #新建一个队列
    urlqueue.append(urlstr) #队列中加入最初的url
    while len(urlqueue)!=0: #判断队列是否为空
        url = urlqueue.popleft()  #队列弹出的数据（url）
        print(url)  #打印url连接
        pagedata = getdata(url)  #获取网页源代码
        emaillist = getallemail(pagedata)  #提取邮箱到列表
        if len(emaillist)!=0:       #若邮箱列表不为空
            for email in emaillist:
                print(email)        #打印所有的邮箱
        newurllist = geteveryurl(pagedata) #抓取该网页的所有的url
        if len(newurllist)!=0:      #若列表不为空
            for urlstr in newurllist:
                if urlstr not in urlqueue:
                    urlqueue.append(urlstr)     #若url不在该队列中，则将该url加入队列中

BFS(input("请输入你想爬取的最初页面"))





