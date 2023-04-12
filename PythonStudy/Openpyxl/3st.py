import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER="smtp.naver.com"
SMTP_PORT=465
USER=""#아이디
PASSWORD=""#비밀번호

def send_mail(name, addr, title, content):
    msg=MIMEMultipart('alternative')# alernative: 텍스트 메일을 보낼때 필요한 양식

    msg['From']=USER+"@naver.com"
    msg['To']=addr
    msg['Subject']=title 
    msg['CC']='test@test.com'

    text=MIMEText(content, _charset="utf-8")
    msg.attach(text)# mime는 모양, smtp는 실제 보내는 양식. mime는 뷰 라고 생각하면 될듯

    smtp=smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)# _SSL: 보안
    smtp.login(USER, PASSWORD)
    smtp.sendmail(USER+"@naver.com",addr, msg.as_string())
    smtp.close()

    

send_mail('김찬호', 'chgim1128@gmail.com', '제목입니다.', '내용입니다.')

