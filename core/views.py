from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.utils.translation import gettext, get_language

class HomeCoreView(TemplateView):
    template_name = 'core/index.html'


#def home_core_fbv(request): # core
#    return render(request, 'core/index.html')

#def home_core_fbv(request): # core i18n
#    current_language = request.LANGUAGE_CODE
#    context = {'current_language': current_language}
#    return render(request, 'core/index.html', context)