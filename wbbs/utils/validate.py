import re

def ValidateSignUpParams(request):
  require_list = ['phone', 'password', 'name']

  for _, val in enumerate(require_list):
    item = request.POST.get(val)
    if not item:
      return val + ' is empty'
    elif val == 'phone' and (not re.match(r'^[\d]{11}$', item)):
      return 'Incorrect phone number'

  return True

