from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import ContactusViews

router=DefaultRouter()  # eta holo router

router.register('',ContactusViews)  # eta holo antena

urlpatterns = [
    path('',include(router.urls))
]
