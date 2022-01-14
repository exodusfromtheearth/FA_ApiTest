# -*- coding: utf-8 -*-
# Author:xtgao
# Filename:sendEmail.py
# Time:2021/1/20 8:13 下午

"""
封装发送邮件的方法

"""
import smtplib
import time
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pytest
from common.filepublic import filepath


# @pytest.fixture()
# def get_ini(pytestconfig):
#     '''读取ini配置信息'''
#     sender = pytestconfig.getini('sender')
#     receivers = pytestconfig.getini('receiver')
#     toclause = receivers.split(',')
#     receiverslist = ",".join(toclause)
#     smtp = pytestconfig.getini('smtp_server')
#     port = pytestconfig.getini('port')
#     psw = pytestconfig.getini('emailpsw')
#     return sender,receiverslist,smtp,port,psw


class EmailHandler:
    def __init__(self):
        self.sender = 'tlq13@qq.com'  # 发件人邮箱账号
        # self.psw = 'UAGIOTYRBVGPBZSC'  # 发件人163邮箱密码
        self.psw = 'wtmnfnaacqwebejd'  # 发件人qq邮箱密码
        self.receivers = ['15611360995@163.com']  # 收件人邮箱账号
        self.smtp = 'smtp.qq.com'
        self.port = '465'

    def send_email(self):
        mail_msg = """
        <p>本邮件由系统自动发出，无需回复！</p>
        <p>各位同事，大家好，以下为inX系统项目接口自动化测试报告，点击链接可以直接查看</p>
        <p><a href="http://www.runoob.com">Jenkins项目首页</a></p>
        <p><a href="http://www.runoob.com">Jenkins项目测试报告</a></p>
        """
        message = MIMEText(mail_msg, 'html', 'utf-8')
        # message['From'] = Header("测试组", 'utf-8')
        # message['To'] = Header("研发部", 'utf-8')
        # subject = 'Python SMTP 邮件测试'
        # message['Subject'] = Header(subject, 'utf-8')

        # message = MIMEMultipart()
        # # 读取html文件内容
        # f = open(report_file, 'rb')
        # mail_body = f.read()
        # f.close()
        # # stress_body = Consts.STRESS_LIST
        # # result_body = Consts.RESULT_LIST
        # # body2 = 'Hi，all\n本次接口自动化测试报告如下：\n   接口响应时间集：%s\n   接口运行结果集：%s' % (stress_body, result_body)
        # msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        message['Subject'] = Header("API测试报告"+"_"+tm, 'utf-8')
        message['From'] = Header("测试组", 'utf-8')
        message['To'] = Header("研发部", 'utf-8')
        #
        # message.attach(msg)

        try:
            smtp163 = smtplib.SMTP()
            smtp163.connect(self.smtp, 25)
            # smtp163 = smtplib.SMTP_SSL(self.smtp, 465)
            smtp163.login(self.sender, self.psw)
            smtp163.sendmail(self.sender, self.receivers, message.as_string())
        except Exception as e:
            print(e)
            print("发送失败")

        else:
            print("发送成功")
        finally:
            smtp163.quit()


# if __name__ == '__main__':
#     case_report_dir = filepath("report", "report.html")
#     EmailHandler().send_email()



