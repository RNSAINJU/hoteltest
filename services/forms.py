from django import forms
from services.models import Enquiry

class NewEnquiryForm(forms.ModelForm):
    name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
        attrs={'class':"form-control",'placeholder': 'Your Name'}
        )
    )

    email = forms.EmailField(
        max_length=254,
        widget=forms.TextInput(
        attrs={'class':"form-control",'placeholder': 'Email'}
        )
    )

    mobilenumber = forms.CharField(
        max_length=14,
        widget=forms.TextInput(
        attrs={'class':"form-control",'placeholder': 'Phone'}
        )
    )

    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(
        attrs={'rows':2, 'cols':30,'class':"form-control",'placeholder': 'Message'}
        )
    )


    class Meta:
        model=Enquiry
        fields=['name','email','mobilenumber','message',]
