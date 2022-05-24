from django.shortcuts import render, redirect
from django.utils.datetime_safe import datetime

from generator.entities.password import Password
from generator.forms import password_form
from generator.repository import password_repository
from generator.services import password_service

# Create your views here.

template_tags = {
    'ano_atual': datetime.today().year
}


def create_password(request):
    if request.method == 'POST':
        form_password = password_form.PasswordForm(request.POST)
        if form_password.is_valid():
            repository_password = password_repository.PasswodRepository(12)
            new_password = Password(
                value=repository_password.generate_password(),
                expiration_date=form_password.cleaned_data['expiration_date'],
                maximum_views=form_password.cleaned_data['maximum_views'],
                views=0
            )
            password_service.create_password(new_password)
            return redirect('get_passwords')
    else:
        form_password = password_form.PasswordForm()
    template_tags['form_password'] = form_password
    return render(request, 'password/form_password.html', template_tags)


def get_passwords(request):
    passwords = password_service.get_passwords()
    template_tags['passwords'] = passwords
    return render(request, 'password/get_passwords.html', template_tags)


def get_password_id(request, id):
    template_tags['password'] = password_service.get_password_id(id)
    return render(request, 'password/password_details.html', template_tags)


def edit_password(request, id):
    return render(request, 'password/form_password.html', template_tags)


def delete_password(request, id):
    return render(request, 'password/confirm_deletion.html', template_tags)
