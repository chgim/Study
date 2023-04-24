# smtp: 메일 전송 프로토콜
import os
import smtplib #메일을 보내기 위한 SMTP관련 모듈
from email import encoders
from email.utils import formataddr
from email.mime.base import MIMEBase
from email.mime.text import MIMEText # SMTP 가 사용하는 양식에 맞춰서 내용을 써주는 클래스
from email.mime.multipart import MIMEMultipart # SMTP 가 사용하는 양식에 맞춰서 내용을 써주는 클래스
# SMTP 접속을 위한 서버, 계정 설정
SMTP_SERVER='smtp.naver.com' #  SMTP 서버 주소: 메일 보내는 서버 주소
SMTP_PORT=465 # SMTP 서버 포트: SMTP 주소로 갈 때 쓸 길 번호 • 465: SSL(보안 연결)• 587: 일반 연결
# 본인 계정 사용
SMTP_USER='아이디'
SMTP_PASSWORD='비밀번호'

def send_mail(name, addr, attachment=None):
        # 메시지 기본 형태 만들기
    msg = MIMEMultipart('alternative')# 텍스트 파일이구나. 알려줌 MIMEMultipart를 활용하여 필요한 데이터 양식을 가져옴  alernative: 텍스트 메일을 보낼때 필요한 양식
    if attachment:
        msg = MIMEMultipart('mixed')# 섞여있다 알려줌. 첨부파일이 있는 애구나. 알려줌.
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
    # ‣ 내용의 경우 MIMEText를 활용하고, attach라는 함수로 추가

    if attachment:
        file_data = MIMEBase('application', 'octet-stream')
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
    smtp.close()
    #   • 앞서 설정한 SMTP 서버, 포트 정보로 서버에 연결
    #   • 앞서 설정한 계정 정보로 서버에 로그인
    #   • 보내는 메일주소, 내 메일을 받을 메일 주소, 메시지 정보로 sendmail
    #   • close를 통해 서버와의 연결을 닫음
send_mail('김찬호', 'chgim1128@gmail.com', 'test.txt')
