import json, re

from django.views import View
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password

from wbbs.models import User

from wbbs.utils.validate import ValidateSignUpParams

class SignUpView(View):

  def new_user(self, request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    password = request.POST.get('password')

    try:
      exist_user = User.objects.get(phone_number=phone)
    except Exception:
      exist_user = None

    if exist_user:
      return phone + ' is exist.'

    user = User(
      name=name,
      phone_number=phone,
      password=make_password(password),
    )
    user.save()

  def get(self, request):
    return HttpResponse('only post method is supported.')

  def post(self, request):
    phone = request.POST.get('phone')
    verification_code = request.POST.get('verification_code')
    is_validate = ValidateSignUpParams(request)
    if type(is_validate) == str:
      content = json.dumps({
        'code': 1,
        'msg': is_validate
      })
    elif phone == '18729573517':
      err_msg = self.new_user(request)
      content = json.dumps({
        'code': 0,
        'msg': err_msg if err_msg else 'sign up success.'
      })
    else:
      content = json.dumps({
        'code': 1,
        'msg': 'Incorrect verification code.'
      })
    return HttpResponse(content, content_type='text/json')


class VerificationCodeView(View):

  def get(self, request):
    return HttpResponse('only post method is supported.')

  def post(self, request):
    phone = request.POST.get('phone')
    print(phone)
    return HttpResponse(json.dumps({
      'code': 0,
      'msg': 'send success.',
    }), content_type='text/json')

