from rest_framework.routers import DefaultRouter
from .views import AppointmentViews
from django.urls import path,include

router=DefaultRouter()

router.register("",AppointmentViews)


urlpatterns = [
    path('',include(router.urls))
]
