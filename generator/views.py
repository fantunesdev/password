from django.shortcuts import render, redirect
from django.utils.datetime_safe import datetime

from generator.entities.password import Password
from generator.forms import password_form
from generator.forms.gerenal_form import ExclusionForm
from generator.repositories import password_repository, access_repository
from generator.services import password_service, access_service

# Create your views here.

template_tags = {
    'ano_atual': datetime.today().year
}


def create_password(request):
    if request.method == 'POST':
        form_password = password_form.PasswordForm(request.POST)
        if form_password.is_valid():
            new_password = Password(
                value=form_password.cleaned_data['value'],
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
    password = password_repository.increment_view(id)
    access_repository.register_access(request, password)
    template_tags['password'] = password
    if password.value:
        return render(request, 'password/password_details.html', template_tags)
    else:
        template_tags['today'] = datetime.today()
        return render(request, 'password/expired.html', template_tags)


def view_access(request, id):
    password = password_service.get_password_id(id)
    access = access_service.get_access_password(password)
    # access = access_service.get_access()
    template_tags['password'] = password
    template_tags['access'] = access
    return render(request, 'password/password_details.html', template_tags)


def delete_password(request, id):
    password = password_service.get_password_id(id)
    if request.POST.get('confirmation'):
        password_service.delete_password(password)
        return redirect('get_passwords')
    template_tags['password'] = password
    template_tags['exclusion_form'] = ExclusionForm()
    return render(request, 'password/exclusion_confirmation.html', template_tags)


def delete_expirated(request):
    passwords = password_service.get_expirated_passords()
    if request.POST.get('confirmation'):
        for password in passwords:
            password_service.delete_password(password)
        return redirect('get_passwords')
    template_tags['passwords'] = passwords
    template_tags['exclusion_form'] = ExclusionForm()
    return render(request, 'password/get_passwords.html', template_tags)
