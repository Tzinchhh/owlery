from django.shortcuts import render_to_response
from .forms import SendLetter
from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import redirect
from alltables.forms import (
    RegistrationForm,
    EditProfileForm)
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def account(request):
    return render_to_response('pages/account.html', {'username': auth.get_user(request).username})

def letters(request):
    try:
        if request.method == "GET":
            return render(request, "pages/letters.html")
        if request.method == 'POST':
            form = SendLetter(request.POST or None)
            if form.is_valid():
                form.save()
                return render_to_response("pages/thanks.html")
    except Exception as e:
        print(e)
        return render_to_response("pages/ups.html")

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account/profile')
    else:
        form = RegistrationForm()
        args = {'form':form}
        return render(request, 'pages/reg_form.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/account/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'pages/edit_profile.html', args)

def view_profile(request):
    args = {'user': request.user}
    return render(request, 'pages/view_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile')
        else:
            redirect('/account/change-password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'pages/change_password.html', args)

def login_redirect(request):
    return redirect('/account/login')