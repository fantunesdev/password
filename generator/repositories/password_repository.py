import re
import string
from datetime import datetime
from random import choice

from generator.entities.password import Password
from generator.services import password_service


def increment_view(id):
    old_password = password_service.get_password_id(id)
    new_password = Password(
        value=old_password.value,
        expiration_date=old_password.expiration_date,
        maximum_views=old_password.maximum_views,
        views=old_password.views
    )
    if old_password.views >= old_password.maximum_views or old_password.expiration_date < datetime.today().date():
        new_password.value = None
    else:
        new_password.views += 1
    return password_service.edit_password(old_password, new_password)
