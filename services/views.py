from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import Package, Hotel, Review


class HomeView(TemplateView):
	template_name = 'services/index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['services'] = Package.objects.filter(is_featured=True)
		context['hotels'] = Hotel.objects.filter(is_featured=True)
		context['review'] = Review.objects.filter(is_featured=True).first()
		return context


class PackagesListView(ListView):
	template_name = 'services/packages-list.html'
	queryset = Package.objects.filter(is_active=True).order_by('is_featured')
	context_object_name = 'packages'
	paginate_by = 10



class PackagesDetailView(DetailView):
	template_name = 'services/packages-detail.html'
	context_object_name = 'package'
