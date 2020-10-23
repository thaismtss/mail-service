from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dynaconf import settings

def send_mail_sendgrid(from_email, to_emails, subject, plain_text_content, html_content):
    message = Mail(
    from_email= from_email,
    to_emails= to_emails,
    subject= subject,
    plain_text_content= plain_text_content,
    html_content= html_content )
    try:    
        sg=SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
        response = sg.send(message)
        print(message)
        print("email enviado")
    except Exception as e:
        print(str(e.body))
    return message


def send_mail_sns(from_email, to_emails, subject, plain_text_content, html_content):
    pass

class SendMail:
    def __init__(self,from_email, to_emails, subject, plain_text_content, html_content, send_mail):
        self._from_email = from_email
        self._to_emails = to_emails
        self._subject = subject
        self._plain_text_content = plain_text_content
        self._html_content = html_content
        self._send_mail = send_mail
    
    def send_mail(self):
        return self._send_mail(
             from_email=self._from_email,
             to_emails= self._to_emails,
             subject= self._subject,
             plain_text_content= self._plain_text_content,
             html_content= self._html_content)
   








