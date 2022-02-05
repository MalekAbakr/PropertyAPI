from django.contrib import admin
from .models import Property_image, User,Property,Country,State,City

# Register your models here.
admin.site.register(User)
admin.site.register(Property)
admin.site.register(Property_image)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)



