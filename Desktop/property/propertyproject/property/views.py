from urllib import request
from rest_framework import viewsets
from django.contrib import messages
from django.http import HttpResponse
from .forms import NewUserForm,ContactForm
from django.shortcuts import  render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django_filters.rest_framework import DjangoFilterBackend
from .models import User,Property,Property_image,Country,State,City
from .serializers import (UserSerializer,PropertySerializer,
Property_imageSerializer,CountrySerializer,StateSerializer,CitySerializer)






# Create your views here.     
#Viewsets 
class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
  
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','email']

class PropertyViewset(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
	
class Property_imageViewset(viewsets.ModelViewSet):
    queryset = Property_image.objects.all()
    serializer_class = Property_imageSerializer
    
class CountryViewset(viewsets.ModelViewSet): 
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class StateViewset(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer       

class CityViewset(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

#Template
def dashboard(request):
    return render(request, 'dashboard.html')

def allusers(request):
	return render(request,'all-users.html')

def allproperty(request):
	return render(request,'all-property.html')

def login2(request):
	return render(request,'login2.html')

def register2(request):
	return render(request,'register2.html')

#Register view
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful.")
			return redirect("homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

#Login view
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

#Logout view
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("homepage")

def homepage(request):
	return render(request, "home.html")

#Contact view
def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("homepage")
      
	form = ContactForm()
	return render(request, "templates/contact.html", {'form':form})


