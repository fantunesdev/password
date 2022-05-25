from generator.models import Password


def create_password(password):
    password_db = Password.objects.create(
        value=password.value,
        expiration_date=password.expiration_date,
        maximum_views=password.maximum_views,
        views=password.views
    )
    return password_db


def get_passwords():
    return Password.objects.all()


def get_expirated_passords():
    return Password.objects.filter(value__isnull=True)


def get_password_id(id):
    return Password.objects.get(id=id)


def edit_password(old_password, new_passowrd):
    old_password.value = new_passowrd.value
    old_password.expiration_date = new_passowrd.expiration_date
    old_password.maximum_views = new_passowrd.maximum_views
    old_password.views = new_passowrd.views
    old_password.save(force_update=True)
    return old_password


def delete_password(password):
    password.delete()
