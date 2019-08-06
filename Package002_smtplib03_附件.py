#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header



sender = 'likun.jiang@oumeng.com.cn'
receivers = ['likun.jiang@oumeng.com.cn','thankyoulaojiang@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEMultipart()# 注意修改成multipart

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] =  Header("测试", 'utf-8')

#添加附件
att1 = MIMEText(open('/bioinfo/metagenome/projects/0059_20190802_0059PI_1250-1285_Seperate/Mail.zip', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="text.zip"'
message.attach(att1)


try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
