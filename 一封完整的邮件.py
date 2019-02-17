from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr,formataddr
import smtplib


def _format_addr(s):    # 用于格式化一个邮件地址
    """
    s: XXX: <xxx@xx.xx>  -->  a,b = parseaddr(s)  -->   formataddr((Header(a,'utf-8').encode(),addr))
    """
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))     # 返回一个元组类型


def AddPicture(msg):    # 发送一个图片
    with open('','rb')as f: # 打开你要发的图片文件
        mime = MIMEBase('image','gif',filename='')
        mime.add_header('Content-ID','<0>')
        mime.add_header('X-Attachment-Id','0')
        # 加上必要的头部信息
        mime.set_payload(f.read())  # 读取附件的内容
        encoders.encode_base64(mime)    # 用Base64编码
        msg.attach(mime)    # 添加到MIMEMultipart



from_addr =  '' # 发件箱
password =  '' # 密码（qq要输入qq邮箱提供的十六位授权码）
to_addr =   '' # 收件箱
smtp_server ='stmp.qq.com' # SMTP服务器地址

# 构造一个msg
msg = MIMEMultipart('alternative')  # 'alternative':html/plain可选
msg['From'] = _format_addr('Python: <%s>' % from_addr)  # 发件人名字
msg['To'] = _format_addr('Antiestablishmentarism：<%s>' % to_addr) # 收件人名字
msg['Subject'] = Header('我是title','utf-8').encode() # 主题
msg.attach(MIMEText('<html><body>Hello I will send with a file</body></html>','html','utf-8'))  # 添加附件
AddPicture(msg)
"""
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))
    将附件的图片插入到正文中
"""

server = smtplib.SMTP(smtp_server,25)   # smtp服务器地址，协议默认端口是25
server.starttls() # 创建安全连接
server.set_debuglevel(1)   # 打印出和smtp服务器交互的所有信息
server.login(from_addr,password)    # 登录
server.sendmail(from_addr,[to_addr],msg.as_string())    # 发送邮件,[to_addr]表示可以发给很多人
server.quit()



