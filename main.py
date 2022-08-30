import smtplib
import os
from email.mime.text import MIMEText


class MailSender:
    def __init__(self, mail_sender='89175955650@mail.ru', mail_receiver='89175955650@mail.ru',
                 letter_subject='Тестовая тема письма'):
        self.mail_sender = mail_sender
        self.mail_receiver = mail_receiver
        self.letter_subject = letter_subject

    def send_mail(self):
        with open('email_password.txt', 'r', encoding='utf-8') as password:
            pswd = password.read()

        server = smtplib.SMTP("smtp.mail.ru", 587)
        server.starttls()

        try:
            with open("email_template.html") as html_file:
                template = html_file.read()
                html_result = "All right, 'email_template.html' were found."
        except IOError:
            html_result = "The template file doesn't found!"

        print(html_result)

        try:
            server.login(self.mail_sender, pswd)
            msg = MIMEText(template, "html")
            msg["From"] = self.mail_sender
            msg["To"] = self.mail_receiver
            msg["Subject"] = self.letter_subject
            server.sendmail(self.mail_sender, self.mail_receiver, msg.as_string())
            result_text = "The letter was sent successfully!"

        except Exception as _ex:
            result_text = f"{_ex}\nCheck your login or password, please!"

        print(result_text)

        return result_text

    def main(self):
        MailSender.send_mail(MailSender())


if __name__ == '__main__':
    mail_sender_object = MailSender()
    mail_sender_object.main()
