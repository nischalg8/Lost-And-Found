import logging
from .middleware import get_current_ip, get_current_user
import datetime
import os 
from django.conf import settings

LOG_FILE = os.path.join(settings.BASE_DIR, "user_activity.log")
logger = logging.getLogger('user_activity')

def log_user_action(action, item = None):
    
    user = get_current_user()
    username = user.username if user and user.is_authenticated  else "anonymous"
    try: 
        logger.info(
            "",
            extra={
                "username": username,
                "action": action,
                "item": item if item else "None",
                "ip": get_current_ip(),
            },
        )

    except Exception as e:
        print("Logging Error", e)