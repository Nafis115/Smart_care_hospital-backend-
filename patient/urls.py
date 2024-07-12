from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import PatientView,UserRegistrationApiView,activate,UserLoginView,UserLogoutView


router=DefaultRouter()

router.register('list',PatientView)


urlpatterns = [
    path("",include(router.urls)),
    path("register/", UserRegistrationApiView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path('active/<uid64>/<token>/',activate,name='activate'),
    
]
