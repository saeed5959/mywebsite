from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from app.forms import SignUpForm
from django.http import FileResponse


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = 'registration/signup.html'


def homepage(request):
    t = loader.get_template('homepage.html')
    return HttpResponse(t.render({}, request))

def cv(response):
    pdf = open('/home/saeed/software/python/real/main/app/static/saeed_resume.pdf', 'rb').read()
    return HttpResponse(pdf, content_type='application/pdf')

def blog(request):
    t = loader.get_template('blog.html')
    return HttpResponse(t.render({}, request))

def search(request):
    t = loader.get_template('search.html')
    return HttpResponse(t.render({}, request))


