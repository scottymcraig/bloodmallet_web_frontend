from django.contrib import messages
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _

from general_website.forms import UserLoginForm, SignUpForm, UserUpdateForm, ProfileUpdateForm

import logging

logger = logging.getLogger(__name__)


def login(request):
    """View to allow users to log in with their inpage account.

    Arguments:
        request {[type]} -- [description]

    Returns:
        form -- login form
    """

    logger.debug('login')

    # if login is attempted
    if request.method == 'POST':
        login_form = UserLoginForm(request=request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                n = 'index'
                return redirect(n)
            else:
                messages.warning(request, _("Couldn't log in. Please check your input."))

        else:
            pass
    else:
        login_form = UserLoginForm()
        pass
    return render(request, 'general_website/login.html', {'login_form': login_form})


@login_required
def logout(request):
    """Logs out the user and returns him to the front page.

    Arguments:
        request {[type]} -- [description]

    Returns:
        [type] -- [description]
    """

    auth_logout(request)
    return redirect('index')


def signup(request):
    """View to create a user account.

    Arguments:
        request {[type]} -- [description]

    Returns:
        [type] -- [description]
    """

    if request.method == 'POST':
        logger.info('Someone tried to sign up!')
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.success(request, _("Account created."))
            return redirect('index')
        else:
            messages.warning(request, _("Account creation failed."))
    else:
        signup_form = SignUpForm()
    return render(request, 'general_website/signup.html', {'signup_form': signup_form})


@login_required
def profile(request):
    if request.method == 'POST':
        profile_form = ProfileUpdateForm(request.POST, instance=request.user)
        if profile_form.is_valid():

            profile_form.save()
            messages.success(request, _("Profile was updated!"))

            return redirect('profile')

    else:
        user_form = UserUpdateForm(user=request.user)
        profile_form = ProfileUpdateForm(instance=request.user)

    content = {'user_form': user_form, 'profile_form': profile_form}

    return render(request, 'general_website/profile.html', content)


@login_required
def change_password(request):
    """Receives UserUpdateForm as POST.
    Changes user password if valid.
    Redirects to 'profile'
    """

    if request.method != 'POST':
        pass
    else:
        user_form = UserUpdateForm(request.user, request.POST)
        if user_form.is_valid():
            user = user_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, _("Password was updated!"))
        else:
            messages.error(request, _("Password update failed. Check your input."))
    return redirect('profile')


def settings(request):
    return render(request, 'general_website/settings.html', {})
