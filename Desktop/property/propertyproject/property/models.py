from django.db import models
from utils.constants import GENDER_CHOICES, LEASE_DURATION_CHOICES, PAYMENT_TYPE_CHOICES,USER_TYPE_CHOICES,CATEGORY_CHOICES,TYPE_CHOICES



"""
User Model:
this model used to describe users' data
"""
class User(models.Model):
    # this field repersent name of the user is charfield 
    name = models.CharField(max_length=100,null=False,blank = False)
    # this field repersent email of the user is charfield 
    email = models.CharField(max_length=100,null=False,blank = False)
    # this field repersent image of the user is imagefield 
    image = models.ImageField(null=False,blank = False)
    # this field repersent gender of the user refrences the utils model
    gander = models.CharField(max_length=100,choices=GENDER_CHOICES)
    # this field repersent brith data of the user is datefield 
    brith_date = models.DateField(null=False,blank = False)
    # this field repersent password of the user is charfield 
    password = models.CharField(max_length=50,null=False,blank = False)
    # this field repersent phone number of the user is charfield 
    phone_number = models.CharField(max_length=10,null=False,blank = False)
    # this field repersent user type of the user depends the utils model
    user_type  = models.CharField(max_length=30,choices=USER_TYPE_CHOICES)
    
    def __str__(self):
        return self.name

"""
Property Model:
this model used to describe property' data
"""
class Property(models.Model):
    # this field repersent description of the property is textfield 
    description = models.TextField(verbose_name='Description',null=False,blank=False)
    # this field repersent category of the property is charfield refrences the utils model
    category = models.CharField(max_length=20,choices=CATEGORY_CHOICES)
    # this field repersent lesae duration of the property is charfield refrences the utils model
    lesae_duration = models.CharField(max_length=50,choices=LEASE_DURATION_CHOICES)
    # this field repersent type of the property is charfield refrences the utils model
    type = models.CharField(max_length=20,choices=TYPE_CHOICES)
    # this field repersent location of the property is charfield
    location = models.CharField(max_length=200,null=False,blank = False)
    # this field repersent area of the property is integerfield
    area = models.IntegerField(null=False,blank = False)
    # this field repersent payment type of the property is charfield refrences the utils model
    payment_type = models.CharField(max_length=50,choices=PAYMENT_TYPE_CHOICES)
    # this field repersent price of the property is integerfield
    price = models.IntegerField(null=False,blank = False)
    # this field repersent status of the property is charfield
    status = models.CharField(max_length=100,null=False,blank=False)
    # this field repersent advanced_price of the property is integerfield
    advanced_price = models.IntegerField(null=False,blank = False)
    # this field repersent rooms of the property is integerfield
    rooms = models.IntegerField(null=False,blank = False)
    #city_id = models.ForeignKey(City,on_delete=models.CASCADE)
    available_until = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.description

"""
Property_image Model:
this model used to describe property_image' data
"""
class Property_image(models.Model):
    # this field repersent defult imageof the property image is boolean field
    is_defult_image = models.BooleanField(verbose_name='Defult_Image', default=False, null=False, blank=False,)
    # this field repersent image of the user is imagefield 
    image = models.ImageField(null=False,blank = False)
    # this field is a forign key refrences the property model
    property_id = models.ForeignKey(Property,on_delete=models.CASCADE)

    def __str__(self):
        return self.image

"""
Country Model:
this model used to describe country' data
"""
class Country(models.Model):
    # this field repersent name of the country is charfield
    name = models.CharField(max_length=100,null=False,blank = False)
    # this field repersent location of the country is charfield
    location = models.CharField(max_length=100,null=False,blank = False)
    def __str__(self):
        return self.name

"""
State Model:
this model used to describe state' data
"""      
class State(models.Model):
     # this field repersent name of the state is charfield
    name = models.CharField(max_length=100,null=False,blank = False)
    # this field repersent location of the state is charfield
    location = models.CharField(max_length=100,null=False,blank = False)
    # this field is a forign key refrences the country model
    country_id = models.ForeignKey(Country,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

"""
City Model:
this model used to describe cities' data
"""
class City(models.Model):
    # this field is a forign key refrences the state model
    state_id = models.ForeignKey(State,on_delete=models.CASCADE)
    # this field repersent name of the city is charfield
    name = models.CharField(max_length=100,null=False,blank = False)
    # this field repersent location of the city is charfield
    location = models.CharField(max_length=100,null=False,blank = False)
    def __str__(self):
        return self.name







    
    