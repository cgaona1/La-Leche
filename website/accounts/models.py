from django.db import models
#from django_q.models import Schedule

class Notification(models.Model):
    email = models.EmailField()
    #schedule_id = models.IntegerField(default=0)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.email

    """# Function to create a schedule
    def save(self, *args, **kwargs):
        # Create the schedule
        schedule = Schedule.objects.create(
            name = self.__str__(),
            func = "website.services.send_email",
            args = f"'{self.email}'",
            schedule_type = Schedule.ONCE,
        )

        # Save the model with the schedule ID
        self.schedule_id = schedule.pk
        super().save(*args, **kwargs)
    """
