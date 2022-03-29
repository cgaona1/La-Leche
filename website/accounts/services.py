from django.core.mail import send_mail, BadHeaderError

from datetime import timedelta
from django.utils import timezone
from django_q.tasks import async_task, schedule
from django_q.models import Schedule

def send_email_task(to, subject, message):
    try:
        print("About to send_mail")

        #send email right away
        async_task(send_mail,
            subject,
            message,
            'gaon4805@bears.unco.edu',
            [to],
            fail_silently=False)

        #send email 5 minutes later
        schedule('django.core.mail.send_mail',
            'This is a Follow Up',
            message,
            'gaon4805@bears.unco.edu',
            [to],
            fail_silently=False,
            schedule_type=Schedule.ONCE,
            next_run=timezone.now()+timedelta(minutes=3))

    except BadHeaderError:
        print("BadHeaderError")

    except Exception as e:
        print(e)