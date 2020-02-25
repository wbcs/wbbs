from django.views.generic import View
from django.http import HttpResponse



class LoginView(View):

  def get(self, *args, **kwargs):
    return HttpResponse('fuck you')

