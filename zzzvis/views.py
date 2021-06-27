from django.contrib.auth import authenticate,login,logout
from zzzvis.models import *
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from vistaarsss.settings import EMAIL_HOST_USER
from django.template.loader import get_template
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def Home(request):
    if request.method == "POST":
        d = request.POST
        coname = d['nam']
        comob = d['mob']
        coenquirey = d['enquirey']
        cmemail = d['emai']
        cmsub = d['subje']
        comessag =d['msge']

        email = "vistaarwebx@gmail.com"
        subject = coname,cmsub
        content = comessag,coname,"send this message for",coenquirey,"his e mail and mobile no is",cmemail,comob
        msg = EmailMultiAlternatives(subject, f'{content}', EMAIL_HOST_USER, [f'{email}'])
        e = {'coname': coname, 'comob': comob,'coenquirey':coenquirey,'cmemail':cmemail,'cmsub':cmsub,'comessag':comessag}
        html = get_template('mailwarn.html').render(e)
        msg.attach_alternative (html, 'text/html')
        msg.send()
        
    employee = Team.objects.all()
    cus = customer.objects.all()
    grapi = client_tail.objects.all()
    arti = Articles.objects.all()
    services = SERVICES.objects.all()
    sstory = story_of_vistaar.objects.all()
    d= {"sstory":sstory,"services":services,"employee":employee,"cus":cus,"grapi":grapi,"arti":arti}
    return render(request,'index.html',d)
