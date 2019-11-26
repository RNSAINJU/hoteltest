from django.shortcuts import render,redirect
from django.views.generic import TemplateView, ListView, DetailView

from .models import Package, Hotel, Review
from home.models import Imageslider, Backgroundimage, AboutContent
from .forms import NewEnquiryForm

class HomeView(TemplateView):
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['backgroundimage'] = Backgroundimage.objects.get(name="background")
		context['imagesliders']=Imageslider.objects.all()
		context['packages'] = Package.objects.filter(is_featured=True)
		context['hotels'] = Hotel.objects.filter(is_featured=True)
		context['recommended'] = Hotel.objects.filter(is_recommended=True)
		context['reviews_list'] = Review.objects.all()
		return context


# class PackagesListView(ListView):
# 	template_name = 'services/packages-list.html'
# 	queryset = Package.objects.filter(is_active=True).order_by('is_featured')
# 	context_object_name = 'packages'
# 	paginate_by = 10




# class PackagesDetailView(DetailView):
# 	template_name = 'services/packages-detail.html'
# 	context_object_name = 'package'

# class ServiceListView(ListView):
# 	template_name='services.html'
# 	queryset=Package.objects.filter(is_featured=True)
# 	context_object_name='services'
# 	paginate_by=5

# class ContactView(TemplateView):
# 	template_name='contactus.html'

# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		context['backgroundimage'] = Backgroundimage.objects.get(name="background")
# 		context['form']=NewEnquiryForm()
# 		return context

# 	def post(self,request):
# 		form=NewEnquiryForm(request.POST)
# 		if form.is_valid():
# 			enquiry=form.save(commit=False)
# 			enquiry.save()
# 			return redirect('contactus')
# 		else:
# 			form=NewEnquiryForm()
# 		return render(request,self.template_name,{'form':form})

# class AboutView(TemplateView):
# 	template_name='aboutus.html'

# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		context['backgroundimage'] = Backgroundimage.objects.get(name="background")
# 		context['aboutus'] = AboutContent.objects.filter(is_active=True)
# 		return context


