from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from VirMarket_CS.models import User_Finances
from .tasks import send_signup_email_task

@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):

    if created:
        User_Finances.objects.create(User=instance, Current_Balance = 100000.00)
        #send_signup_email_task.delay(instance.username)

