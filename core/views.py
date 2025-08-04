from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.utils.translation import gettext, get_language
from django.utils.timezone import localtime, now

class HomeCoreView(TemplateView):
    template_name = 'core/index.html'
# for adding some additional context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['counts'] = [1,2]
        context['current_time'] = localtime(now())
        return context


#def home_core_fbv(request): # core
#    return render(request, 'core/index.html')

#def home_core_fbv(request): # core i18n
#    current_language = request.LANGUAGE_CODE
#    context = {'current_language': current_language}
#    return render(request, 'core/index.html', context)