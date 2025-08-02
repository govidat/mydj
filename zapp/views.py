from django.shortcuts import render

# Create your views here.
from django.shortcuts import render # new
from django.views.generic import TemplateView


class HomeZappView(TemplateView):
    template_name = 'zapp/homezapp.html'


def home_zapp_fbv(request): # new
    return render(request, 'zapp/homezapp.html')