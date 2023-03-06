from django import forms
from .models import Reviews , Food,Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
	
# Create your forms here.
	
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class Newreviews(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = '__all__'

class Newfood(forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'
        
class Newcusto(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        