from rest_framework import serializers
from .models import User,Property,Property_image,Country,State,City



#User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'email',
            'image',
            'gander',
            'brith_date',
            'password',
            'phone_number',
            'user_type',
        )
        
        
#Property serializer
class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = (
             'description',
             'category',
             'lesae_duration',
             'type',
             'location',
             'area',
             'payment_type',
             'price',
             'status',
             'advanced_price',
             'rooms',
             #'city_id',
             'available_until',
        )
    #def get_property(self,obj):
    #   return str(obj.User.Property)
             
#Property image serializer
class Property_imageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property_image
        fields = (
            'is_defult_image',
            'image',
            'property_id',
        )
        
#Country serializer
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = (
            'name',
            'location',
        )
        
#State serializer 
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = (
            'country_id',
            'name',
            'location',
        )

#City serializer
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = (
            'state_id',
            'name',
            'location',
        )
        

