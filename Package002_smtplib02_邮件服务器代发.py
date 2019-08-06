# 如果我们本机没有 sendmail 访问，也可以使用其他邮件服务商的 SMTP 访问（QQ、网易、Google等）。

#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
mail_host="smtp.163.com"  #设置服务器
mail_user="thankyoulaojiang@163.com"    #用户名
mail_pass="XXXXXX"   #口令 
 
 
sender = 'thankyoulaojiang@163.com'
receivers = ['429240967@qq.com'，'thankyoulaojiang@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] =  Header("测试", 'utf-8')
 
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
 
 
try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"

# 以上是使用服务商163的 smtp代理
# 目前公司拟用自己邮箱，所以必须要知道的是：邮箱服务器ip地址：***，如果是非加密传输的话一般端口都是25，
# 还有就是邮箱的认证方式，目前我司不需要认证，所以可以省略login这一步（大坑看了半天源码，如果不需要认证的话，login不返回认证方式会报错）

smtp_server = '192.168.13.***'
server = smtplib.SMTP(smtp_server,25)
server.starttls()
server.ehlo()
sender = 'thankyoulaojiang@163.com'
receivers = ['429240967@qq.com'，'thankyoulaojiang@163.com'] 
######删掉  smtpObj.login(mail_user,mail_pass)  
smtpObj.sendmail(sender, receivers, message.as_string())
