from django.core import mail

# https://pytest-django.readthedocs.io/en/latest/helpers.html#mailoutbox
# https://pytest-django.readthedocs.io/en/latest/helpers.html#settings


def test_send_email_should_succeed(mailoutbox, settings) -> None:
    settings.EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
    assert len(mailoutbox) == 0

    # Send message
    mail.send_mail(
        subject='Test Subject here',
        message='Test Here is the message.',
        from_email='testemail@gmail.com',
        recipient_list=['testemail2@gmail.com'],
        fail_silently=False,
    )

    # Test that one message has been sent.
    assert len(mailoutbox) == 1

    # Verify that the subject of the first message is correct.
    assert mailoutbox[0].subject == 'Test Subject here'
