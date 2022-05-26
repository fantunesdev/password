from generator.models import Access


def create_access(access):
    Access.objects.create(
        password=access.password,
        date=access.date,
        ip=access.ip
    )


def get_access():
    return Access.objects.all()


def get_access_password(password):
    return Access.objects.select_related('password').filter(password=password)
