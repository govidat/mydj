from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeCoreView.as_view(), name='homecore'),
#    path('', views.home_core_fbv, name='homecore'),    
]