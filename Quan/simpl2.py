import smtplib
from email.mime.text import MIMEText

#QQ邮箱提供的SMTP服务器
mail_host = 'smtp.qq.com'
#服务器端口
port = 465
send_by = 'ayang818@qq.com'
password = '开启SMTP服务后，QQ邮箱自动生成的16位密码'
send_to = '1614345603@qq.com'

def send_email(title,content,):
	#创建了MIMEText类，相当于在写邮件内容，是plain类型
    message = MIMEText(content,'plain','utf-8')
    message["From"] = send_by
    message['To'] = send_to
    message['Subject'] = title
    try:
        #注意第三个参数，设置了转码的格式(我不设的时候会报解码错误)
        smpt = smtplib.SMTP_SSL(mail_host, port, 'utf-8')
        smpt.login(send_by,password)
        smpt.sendmail(send_by, send_to,message.as_string())
        print("发送成功")
    except:
        print("发送失败")


title = '测试文件'
content = '执行自动化单元测试'
send_email(title,content)