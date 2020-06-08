from .main import send_mail

send_mail(
    subject='hello',
    body='hello world',
    to='jimmy_lin@chief.com.tw',
    cc='jimmy_lin@chief.com.tw',
    attachments=[
        r'C:\Users\jimmy_lin\Envs\pyol\pyol\testexcel.xlsx',
        r'C:\Users\jimmy_lin\Envs\pyol\pyol\testword.docx',
    ]
)