import smtplib

sender = 'admin@example.com'
receivers = ['user1@example.com']

message = """
From: Admin <admin@example.com>
To: User <user1@example.com>
Subject: Тестирование почты в Python

Это тестовое сообщение, пожалуйста не отвечайте на него.
"""

try:

    email = smtplib.SMTP('localhost')
    email.sendmail(sender, receivers, message)
    print("Успешно отправлено")

except smtplib.SMTPException:

    print("Ошибка при отправке сообщения")

#https://myrusakov.ru/python-send-email.html