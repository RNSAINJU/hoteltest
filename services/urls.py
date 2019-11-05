from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
	path('', TemplateView.as_view(template_name='landing.html'), name='landing'),
	path('home/', views.HomeView.as_view(), name='home'),
	path('home/v2', views.HomeView2.as_view(), name='home2'),
	path('about',views.AboutView.as_view(),name='about'),
	path('home/', views.HomeView.as_view(), name='services'),
	path('home/', views.HomeView.as_view(), name='contactus'),
]