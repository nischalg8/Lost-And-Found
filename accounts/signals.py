from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from core.logger import log_user_action

@receiver(user_logged_in)
def log_login(sender, request, user, **kwargs):
    log_user_action("LOGIN")


@receiver(user_logged_out)
def log_logout(sender, request, user, **kwargs):
    log_user_action("LOGOUT")