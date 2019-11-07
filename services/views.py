from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import Package, Hotel, Review
from .forms import NewEnquiryForm

class HomeView(TemplateView):
	template_name = 'services/index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['services'] = Package.objects.filter(is_featured=True)
		context['hotels'] = Hotel.objects.filter(is_featured=True)
		context['recommended'] = Hotel.objects.filter(is_recommended=True)
		context['reviews_list'] = Review.objects.all()
		return context

class HomeView2(TemplateView):
	template_name = 'services/index2.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['services'] = Package.objects.filter(is_featured=True)
		context['hotels'] = Hotel.objects.filter(is_featured=True)
		context['recommended'] = Hotel.objects.filter(is_recommended=True)
		context['review'] = Review.objects.all()
		return context

class PackagesListView(ListView):
	template_name = 'services/packages-list.html'
	queryset = Package.objects.filter(is_active=True).order_by('is_featured')
	context_object_name = 'packages'
	paginate_by = 10



class PackagesDetailView(DetailView):
	template_name = 'services/packages-detail.html'
	context_object_name = 'package'

class ServiceListView(ListView):
	template_name='services.html'
	queryset=Package.objects.filter(is_featured=True)
	context_object_name='services'
	paginate_by=5

class ContactView(TemplateView):
	template_name='contactus.html'

	def get(self,request):
		form=NewEnquiryForm()

		args={
			'form':form
		}
		return render(request,self.template_name,args)

	def post(self,request):
		form=NewEnquiryForm(request.POST)
		if form.is_valid():
			enquiry=form.save(commit=False)
			enquiry.save()
			return redirect('contact')
		else:
			form=NewEnquiryForm()
		return render(request,self.template_name,{'form':form})

class AboutView(TemplateView):
	template_name='aboutus.html'
	context_object_name = 'about'


