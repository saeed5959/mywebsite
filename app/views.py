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

def projects(request):
    t = loader.get_template('projects.html')
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
def panel_credit_pay(request):
    t = loader.get_template('panel_credit_pay.html')
    return HttpResponse(t.render({}, request))

from django.urls import reverse
from azbankgateways import bankfactories, models as bank_models, default_settings as settings

@login_required(login_url='/accounts/login')
def go_to_gateway_view(request):
    # خواندن مبلغ از هر جایی که مد نظر است
    amount = request.POST["price"]
    # تنظیم شماره موبایل کاربر از هر جایی که مد نظر است
    user_mobile_number = '+989112221234'  # اختیاری

    factory = bankfactories.BankFactory()
    bank = factory.create()  # or factory.create(bank_models.BankType.BMI) or set identifier
    bank.set_request(request)
    bank.set_amount(amount)
    # یو آر ال بازگشت به نرم افزار برای ادامه فرآیند
    bank.set_client_callback_url(reverse('callback-gateway'))
    bank.set_mobile_number(user_mobile_number)  # اختیاری

    # در صورت تمایل اتصال این رکورد به رکورد فاکتور یا هر چیزی که بعدا بتوانید ارتباط بین محصول یا خدمات را با این
    # پرداخت برقرار کنید.
    bank_record = bank.ready()

    # هدایت کاربر به درگاه بانک
    return bank.redirect_gateway()


import logging

from django.http import HttpResponse, Http404
from django.urls import reverse

from azbankgateways import bankfactories, models as bank_models, default_settings as settings

@login_required(login_url='/accounts/login')
def callback_gateway_view(request):
    tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
    if not tracking_code:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    try:
        bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
    except bank_models.Bank.DoesNotExist:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    # در این قسمت باید از طریق داده هایی که در بانک رکورد وجود دارد، رکورد متناظر یا هر اقدام مقتضی دیگر را انجام دهیم
    if bank_record.is_success:
        # پرداخت با موفقیت انجام پذیرفته است و بانک تایید کرده است.
        # می توانید کاربر را به صفحه نتیجه هدایت کنید یا نتیجه را نمایش دهید.
        return HttpResponse("پرداخت با موفقیت انجام شد.")

    # پرداخت موفق نبوده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.
    return HttpResponse("پرداخت با شکست مواجه شده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.")


# import logging
# from azbankgateways import bankfactories, models as bank_models, default_settings as settings
#
# factory = bankfactories.BankFactory()
#
# # غیر فعال کردن رکورد های قدیمی
# bank_models.Bank.objects.update_expire_records()
#
# # مشخص کردن رکوردهایی که باید تعیین وضعیت شوند
# for item in bank_models.Bank.objects.filter_return_from_bank():
# 	bank = factory.create(bank_type=item.bank_type, identifier=item.bank_choose_identifier)
# 	bank.verify(item.tracking_code)
# 	bank_record = bank_models.Bank.objects.get(tracking_code=item.tracking_code)
# 	if bank_record.is_success:
# 		logging.debug("This record is verify now.", extra={'pk': bank_record.pk})


@login_required(login_url='/accounts/login')
def panel_comment(request):
    t = loader.get_template('panel_comment.html')
    return HttpResponse(t.render({}, request))