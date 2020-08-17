from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.template.loader import render_to_string
from .token import account_activation_token
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.utils.encoding import force_text
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .forms import InputForm, SignUpForm, EnterpriseReg
from django.shortcuts import render
from django.views.generic.base import TemplateView
#Unused
from django.core.mail import send_mail

# Create your views here

testbanner = """
    ====================================================
                      AFTER TESTING                     
    ====================================================
    """


class home(TemplateView):
    template_name = "starter/homepage.html"


def home_view(request):
    return render(request, 'starter/homepage.html')


def activation_sent_view(request):
    return render(request, 'registration/activation_sent.html')

def logout_view(request):
    return render(request, 'registration/logout.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.signup_confirmation = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'activation_invalid.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Please Activate Your Account'
            message = render_to_string('registration/activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            # print('This is from message' + '\n' + user.email(subject, message))
            print(testbanner)
            print(user.profile.email)   

            #Test Not working 13-08-YYYY
            send_mail(
                subject,
                message,
                '#######',
                [user.profile.email],
                fail_silently=False
            )
            # send_mail(
            #     'subject',
            #     'message',
            #     'ce_curtismensah@outlook.com',
            #     ['dev.picotechnology@gmail.com'],
            #     fail_silently=False, auth_user='ce_curtismensah@outlook.com', auth_password='###########', connection=None
            # )



            return redirect('activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form,  'datalist':['username', 'Firstname', 'Lastname', 'Email', 'Password', 'Confirm Password']})

# fix Junk with the signup view
def EntSignup(request):
    if request.method == 'POST':
        # comp_form = EnterpriseReg(request.POST)
        # register = SignUpForm(request.POST, prefix='register')
        comp_form = EnterpriseReg(request.POST, prefix='profile')
        if comp_form.is_valid():
            comp_form = comp_form.save()
            comp_form.refresh_from_db()
            comp_form.profile.CompanyName = comp_form.cleaned_data.get('company_name')
            comp_form.profile.location = comp_form.cleaned_data.get('location')
            comp_form.profile.email = comp_form.cleaned_data.get('email')
            comp_form.profile.type_of_business = comp_form.cleaned_data.get(
                'type_of_business')
            comp_form.is_active = False
            comp_form.save()
            current_site = get_current_site(request)
            subject = 'Please Activate Your Account'
            message = render_to_string('registration/activation_request.html', {
                'user': comp_form,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            comp_form.email_user(subject, message)
            # print('This is from message' + '\n' + user.email(subject, message))
            print(testbanner)
            print(user.profile.email)   

            #Test Not working 13-08-YYYY
            send_mail(
                subject,
                message,
                'dev.picotechnology@gmail.com',
                [user.profile.email],
                fail_silently=False
            )
            # send_mail(
            #     'subject',
            #     'message',
            #     'ce_curtismensah@outlook.com',
            #     ['dev.picotechnology@gmail.com'],
            #     fail_silently=False, auth_user='ce_curtismensah@outlook.com', auth_password='###########', connection=None
            # )



            return redirect('activation_sent')
    else:
        comp_form = EnterpriseReg()
    return render(request, 'registration/compsignup.html', {'form': comp_form})
