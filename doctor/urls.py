from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import DoctorView,AvailableTimeView,DesignationView,SpecializationView,ReviewView


router=DefaultRouter()

router.register('list',DoctorView)
router.register('designation',DesignationView)
router.register('specialization',SpecializationView)
router.register('available_time',AvailableTimeView)
router.register('review',ReviewView)


urlpatterns = [
    path("",include(router.urls))
]
