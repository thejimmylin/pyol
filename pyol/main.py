from win32com import client
import schedule
import time

def send_mail(subject, body, to, cc='', bcc='', attachments=[], just_show=False):
    """
    The method of sending Email by outlook.
    """
    olMailItem = 0x0
    outlook_client = client.Dispatch("Outlook.Application")
    mail = outlook_client.CreateItem(olMailItem)
    mail.Subject = subject
    mail.Body = body
    mail.To = to
    if cc:
        mail.CC = cc
    if bcc:
        mail.BCC = bcc
    if attachments:
        for attachment in attachments:
            mail.Attachments.Add(attachment)
    if just_show:
        mail.display()
    else:
        mail.Send()

def mail_job():
    """
    Customize your mail job here.
    Here comes an exmaple.
    Note that when you use this on a windows PC, 
    the format of attachments should be a list containing r-string like
    [r'path1', r'path2'].
    """
    send_mail(
        subject='hello',
        body='hello world',
        to='b00502013@gmail.com',
        cc='b00502013@gmail.com',
        attachments=[
            r'C:\Users\jimmy_lin\repos\pyol\pyol\testexcel.xlsx',
            r'C:\Users\jimmy_lin\repos\pyol\pyol\testword.docx',
        ]
    )

schedule.every(5).seconds.do(mail_job)
"""
This sends the Email every 5s.
For more schedule example:
https://github.com/dbader/schedule
"""

while True:
    schedule.run_pending()
    time.sleep(1)
