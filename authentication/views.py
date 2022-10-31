from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from applicant.models import Applicant
from users.token import AccountActivationTokenGenerator, token_generator

from .forms import RegisterForm, LoginForm, ResetPasswordForm


def index(request):
    return render(request, 'index.html')


def send_activation_email(request, user):
    current_site = get_current_site(request)
    subject = 'Activate Your Account'
    message = render_to_string(
        'users/activate_account.html',
        {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': token_generator.make_token(user),
        }
    )

    user.email_user(subject, message, html_message=message)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            fullname = first_name + " " + last_name
            resume = request.FILES["resume"]
            headshot = request.FILES["headshot"]
            applicant = Applicant(fullname=fullname, headshot=headshot, )
            send_activation_email(request, user)
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'auth/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.get(email=email)

            # user = authenticate(request, username=email, password=password)
            # print(user)
            login(request, user)
            return redirect('job_listing')

    else:
        form = LoginForm()

    return render(request, 'auth/login.html', {'form': form})


def reset_password(request):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']


def logout_view(request):
    logout(request)
    return redirect('landing_page')
