from django.core.mail import send_mail, BadHeaderError

def send_email_task(to, subject, message):
    #print(f"from=gaon4805@bears.unco.edu, {to=}, {subject=}, {message=}")
    
    try:
        print("About to send_mail")
        send_mail(
            subject,
            message,
            'gaon4805@bears.unco.edu',
            [to],
            fail_silently=False
        )
    except BadHeaderError:
        print("BadHeaderError")
    except Exception as e:
        print(e)
    
    '''
    print("About to send_mail")
    send_mail(
        'Subject - This is a test',
        'Message - Test has worked',
        'gaon4805@bears.unco.edu',
        ['gaonachris930@gmail.com'],
        fail_silently=False
    )
    '''