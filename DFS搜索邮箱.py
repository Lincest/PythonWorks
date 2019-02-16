import re
import urllib
import urllib.request

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


def DFS(urlstr):
    visitlist = [] #代表已经访问过的url，防止深度遍历出现死循环
    urlstack=[]         #栈
    urlstack.append(urlstr)
    while len(urlstack)!=0:
        url = urlstack.pop()
        print(url)  #打印url链接
        if url not in visitlist:
            pagedata = getdata(url)
            emaillist = getallemail(pagedata)
            if len(emaillist)!=0:
                for email in emaillist:
                    print(email)
            newurllist = geteveryurl(pagedata)
            if len(newurllist)!=0:
                for urlstr in newurllist :
                    if urlstr not in urlstack:
                        urlstack.append(urlstr)
            visitlist.append(url)


DFS(input("请输入你想爬取的最初页面"))

#提取数据容易出现广度遍历
#深度遍历容易出现死循环


