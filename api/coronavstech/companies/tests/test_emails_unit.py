import json
from unittest.mock import patch

from django.core import mail
from django.test import Client
from django.test import TestCase


# https://docs.djangoproject.com/en/4.1/topics/email/

class EmailUnitTest(TestCase):
    def test_send_email_should_succeed(self) -> None:
        with self.settings(
            EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend'
        ):
            self.assertEqual(len(mail.outbox), 0)

            # Send message
            mail.send_mail(
                subject="Test Subject here",
                message="Test Here is the message.",
                from_email="testemail@gmail.com",
                recipient_list=["testemail2@gmail.com"],
                fail_silently=False,
            )

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, 'Test Subject here')

    def test_send_email_without_arguments_should_send_empty_email(self) -> None:
        client = Client()
        with patch(
            'companies.views.send_email'
        ) as mocked_send_mail_function:
            response = client.post(path='/send-email')
            response_content = json.loads(response.content)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response_content['status'], 'success')
            self.assertEqual(response_content['info'], 'email sent successfully')

            mocked_send_mail_function.assert_called_with(
                subject=None,
                message=None,
                from_email="israeltechlayoffs@gmail.com",
                recipient_list=["israeltechlayoffs@gmail.com"],
            )
