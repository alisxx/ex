from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    #return HttpResponse("index")
    return render(request, 'cpages/index.html')

def home(request):
    #return HttpResponse("index")
    return render(request, 'cpages/index.html')

def contact(request):
    #return HttpResponse("contact")
    return render(request, 'cpages/contact.html')


def careers(request):
    #return HttpResponse("careers")
    return render(request, 'cpages/careers.html')

def service(request):
    #return HttpResponse("careers")
    return render(request, 'cpages/index.html/service')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            full_nm = form.cleaned_data['full_nm']
            org_nm = form.cleaned_data['org_nm']
            ph_nbr = form.cleaned_data['ph_nbr']
            msg_text = form.cleaned_data['msg_text']
            try:
                message = msg_text
                subject = full_nm + " " + org_nm + " " + ph_nbr
                send_mail(subject, message, from_email, ['salma.ali@exponentify.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()
        
    return render(request, 'cpages/contact.html', { 'form': form })

def successView(request):
    return HttpResponse('Success! Thank you for your message.')