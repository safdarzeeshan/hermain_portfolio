from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def home(request):
    template = 'home.html'
    return render(request, template)


def mail(request):

    print 'here'

    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    message = request.POST.get('message')

    print name

    send_mail('Website Contact Form' + name, message + phone, settings.EMAIL_HOST_USER, email, fail_silently=False)
