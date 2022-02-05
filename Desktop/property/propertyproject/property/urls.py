from . import views
from django.db import router
from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserViewset,PropertyViewset,Property_imageViewset,CountryViewset,StateViewset,CityViewset 




  



router = DefaultRouter()
router.register('user',UserViewset),
router.register('property',PropertyViewset),
router.register('property_image',Property_imageViewset),
router.register('country',CountryViewset),
router.register('state',StateViewset),
router.register('city',CityViewset),
urlpatterns = [
    #viewsets url
    path('user/viewset/',include(router.urls)),
    path('property/viewset/',include(router.urls)),
    path('property_image/viewset/',include(router.urls)),
    path('country/viewset/',include(router.urls)), 
    path('state/viewset/',include(router.urls)),
    path('city/viewset/',include(router.urls)),
    #rest auth url
    path('api-auth',include('rest_framework.urls')),
    #api-token-auth
    path('api-token-auth', obtain_auth_token),
    #access api/token
    path('api/token/',jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    #refresh/api/token
    path('api/token/refresh/',jwt_views.TokenRefreshView.as_view(),name ='token_refresh'),
    
]

urlpatterns_dashboard = [

    #dashboard
    path('dashboard', views.dashboard, name='dashboard'),
    #homepage
    path("", views.homepage, name="homepage"),
    #Register
    path("register/", views.register_request, name="register"),
    #Login
    path("login/", views.login_request, name="login"),
    #contact
    path("contact", views.contact, name="contact"),
    #logout
    path("logout", views.logout_request, name= "logout"),
    #Template
    path("login2/", views.login2, name="login2"),
    path("register2/", views.register2, name="register2"),
    path('all-users', views.allusers, name='all-users'),
    path('all-property',views.allproperty, name='all-property'),
]