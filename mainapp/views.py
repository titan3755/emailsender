import os
import smtplib
from django.shortcuts import render, redirect


def send_email(receiver, subject, body):
    email = 'py.emailweb@gmail.com'
    password = 'Amimuhaimin123'
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(email, password)
        msg = f'Subject: {subject}\n\n{body}'
        smtp.sendmail(email, receiver, msg)


# Create your views here.
def homepage(request, *args, **kwargs):  
    context = {'title': 'Send Email'}
    return render(request, 'mainapp/home.html', context)

def send(request, *args, **kwargs):
    if request.method == 'POST' and request.POST.get('username') != '' and request.POST.get('domain') != '' and request.POST.get('subject') != '' and request.POST.get('body') != '' and request.POST.get('username') != None and request.POST.get('domain') != None and request.POST.get('subject') != None and request.POST.get('body') != None:
        receiver_email_username = request.POST.get('username')
        receiver_email_domain = request.POST.get('domain')
        email_subject = request.POST.get('subject')
        email_body = request.POST.get('body')
        main_email = receiver_email_username + '@' + receiver_email_domain
        send_email(main_email, email_subject, email_body)
        return redirect('/')
    else:
        return render(request, 'mainapp/error.html')