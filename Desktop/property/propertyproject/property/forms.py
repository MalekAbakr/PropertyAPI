from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from utils.constants import GENDER_CHOICES,USER_TYPE_CHOICES


# Create your forms here.

class NewUserForm(UserCreationForm):
	gander = forms.ChoiceField(choices=GENDER_CHOICES)
	email = forms.EmailField(required=True)
	brith_date = forms.DateField()
	phone_number = forms.CharField(max_length=10)
	user_type  = forms.ChoiceField(choices=USER_TYPE_CHOICES)
	image = forms.ImageField()
	

	class Meta:
		model = User
		fields = ("username", "email", "gander","brith_date","phone_number","user_type","image","password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class ContactForm(forms.Form):
	first_name = forms.CharField(max_length = 50)
	last_name = forms.CharField(max_length = 50)
	email_address = forms.EmailField(max_length = 150)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)