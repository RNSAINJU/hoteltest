from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
	path('', TemplateView.as_view(template_name='landing.html'), name='landing'),
	path('home/', views.HomeView.as_view(), name='home'),
	# path('aboutUs', views.AboutView.as_view(), name='about'),
	# path('services/', views.ServiceListView.as_view(), name='services'),
	# path('contactUs/', views.ContactView.as_view(), name='contactus'),
]