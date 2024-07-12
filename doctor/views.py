from django.shortcuts import render
from .models import Doctor,Specialization,Designation,Review,AvailableTime
from rest_framework import viewsets
from .serializers import DoctorSerializer,ReviewSerializer,AvailableTimeSerializer,SpecializationSerializer,DesignationSerializer
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters, pagination

# Create your views here.

class DoctorPagination(pagination.PageNumberPagination):
    page_size = 1 # items per page
    page_size_query_param = page_size
    max_page_size = 100


class DoctorView(viewsets.ModelViewSet):
    queryset=Doctor.objects.all()
    serializer_class=DoctorSerializer
    filter_backends = [filters.SearchFilter]
    pagination_class=DoctorPagination
    
class SpecializationView(viewsets.ModelViewSet):
    queryset=Specialization.objects.all()
    serializer_class=SpecializationSerializer
    
    
class DesignationView(viewsets.ModelViewSet):
    queryset=Designation.objects.all()
    serializer_class=DesignationSerializer
    
    
class ReviewView(viewsets.ModelViewSet):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    

class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        doctor_id = request.query_params.get("doctor_id")
        if doctor_id:
            return query_set.filter(doctor = doctor_id)
        return query_set

    
class AvailableTimeView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset=AvailableTime.objects.all()
    serializer_class=AvailableTimeSerializer
    filter_backends = [AvailableTimeForSpecificDoctor]