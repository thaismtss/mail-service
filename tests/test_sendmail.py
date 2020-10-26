import pytest
from mail_service.sendmail import SendMail, send_mail_sendgrid
from unittest import mock

mail= {'''
    "from_email":"fromemail@email.com",
    "to_emails": "toemails@email.com",
    "subject": "subject",
    "plain_text_content":"plain_test_html",
    "html_content":"<strong>html content </strong>" 
'''}

@mock.patch('mail_service.sendmail.SendMail.send_mail', return_value=mail)
def test_send_mail(mocker):
    SendMail.send_mail(mail)
    mocker.assert_called_once_with(mail)

