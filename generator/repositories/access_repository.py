from datetime import datetime

from ipware import get_client_ip

from generator.entities.access import Access
from generator.services import access_service


def register_access(request, password):
    access = Access(
        password=password,
        date=datetime.now(),
        ip=get_client_ip(request)[0]
    )
    access_service.create_access(access)
