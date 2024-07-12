from rest_framework.routers import DefaultRouter

from django.urls import path,include
from .views import SerializerView

router=DefaultRouter() 

router.register('',SerializerView)

urlpatterns = [
    path('',include(router.urls)),
]
