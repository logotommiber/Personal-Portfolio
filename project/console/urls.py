from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('home/', views.index, name='home'),
    path('', RedirectView.as_view(url='home/', permanent=False)),
    path('portfolio-details/', views.details, name='details'),
    path('service-details/', views.service, name='service'),
]
