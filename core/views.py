from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class HomeCoreView(TemplateView):
    template_name = 'core/index.html'


#def home_core_fbv(request): # core
#    return render(request, 'core/index.html')