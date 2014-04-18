from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response,render
from django.template.defaulttags import csrf_token
from myproject.contact.forms import ContactForm
def contact(request):
    errors = []
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
        
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email','noreply@example.com'),
                ['magicaljyy@gmail.com'],
            )
            return  HttpResponseRedirect('/contact/thanks')
    else:
        form = ContactForm(initial={'subject':'I love Jiang Yueyang'})
    return render(request,'contact_form.html',{'form':form})