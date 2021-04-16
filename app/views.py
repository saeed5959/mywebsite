from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from app.forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from app.models import user_info


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

@login_required(login_url='/accounts/login')
def panel(request):
    t = loader.get_template('panel.html')
    return HttpResponse(t.render({}, request))

@login_required(login_url='/accounts/login')
def panel_info(request):

    firstname = ""
    lastname = ""
    email = ""


    if user_info.objects.filter(username=request.user.username):
        if request.method == "POST":
            p = user_info.objects.filter(username=request.user.username).update(firstname=request.POST['firstname'],
                          lastname=request.POST['lastname'], email=request.POST['email'])


        object = user_info.objects.get(username=request.user.username)
        firstname = object.firstname
        lastname = object.lastname
        email = object.email

    else:
        if request.method == "POST":
            p = user_info(username=request.user.username, firstname=request.POST['firstname'],
                          lastname=request.POST['lastname'], email=request.POST['email'])
            p.save()


    t = loader.get_template('panel_info.html')
    return HttpResponse(t.render({"firstname":firstname,"lastname":lastname,"email":email,}, request))

@login_required(login_url='/accounts/login')
def panel_credit(request):
    t = loader.get_template('panel_credit.html')
    return HttpResponse(t.render({}, request))


@login_required(login_url='/accounts/login')
def panel_comment(request):
    t = loader.get_template('panel_comment.html')
    return HttpResponse(t.render({}, request))