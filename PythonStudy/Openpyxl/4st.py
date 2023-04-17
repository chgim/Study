import os
import smtplib
from email import encoders
from email.utils import formataddr
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# SMTP 접속을 위한 서버, 계정 설정
SMTP_SERVER='smtp.naver.com'
SMTP_PORT=465
# 본인 계정 사용
SMTP_USER='kcho1128'
SMTP_PASSWORD='hokimch2899$$'

def send_mail(name, addr, attachment=None):
    # 메시지 기본 형태 만들기
    msg = MIMEMultipart('alternative')# 텍스트 파일이구나. 알려줌
    if attachment:
        msg = MIMEMultipart('mixed') # 섞여있다 알려줌. 첨부파일이 있는 애구나. 알려줌.
    # 메일 전송을 위한 내용 채우기
    # msg['From'] = SMTP_USER+'@naver.com'
    # msg['From'] = f"Chan ho<{SMTP_USER}@naver.com>"
    msg['From'] = formataddr(('김찬호', SMTP_USER + '@naver.com'))
    msg['To'] = formataddr((name, addr))
    msg['CC'] = formataddr((name, addr))
    msg['Subject'] = name + '님에게 메일 도착'
    contents = '이메일 내용'

    text = MIMEText(_text=contents, _charset='utf-8')
    msg.attach(text)

    if attachment:
        file_data = MIMEBase('application', 'octet-stream') # 디폴트
        with open(attachment, 'rb') as f:
            file_data.set_payload(f.read())
        encoders.encode_base64(file_data)

        filename = os.path.basename(attachment)
        file_data.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', filename))
        msg.attach(file_data)
    # 서버 정보를 가지고 smtp 클래스 변수 생성
    smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
     # 로그인
    smtp.login(SMTP_USER, SMTP_PASSWORD)
    # 메일 전송
    smtp.sendmail(SMTP_USER + '@naver.com', addr, msg.as_string())
    print(msg.as_string())
    # 닫기
    smtp.close()

send_mail('김찬호', 'chgim1128@gmail.com', 'test.txt')
