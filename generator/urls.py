from django.urls import path

from generator.views import *

urlpatterns = [
    path('create/', create_password, name='create_password'),
    path('', get_passwords, name='get_passwords'),
    path('<str:id>/', get_password_id, name='get_password_id'),
    path('edit/<int:id>/', edit_password, name='edit_password'),
    path('delete/<int:id>/', delete_password, name='delete_password'),
]
