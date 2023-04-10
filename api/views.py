from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from app import models
from . import serializers


#API Overview
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        #List Create
        'List Create Primary School Students:':'http://127.0.0.1:8000/api/primary/add/',
        'List Create High School Students:':'http://127.0.0.1:8000/api/highschool/add/',
        'List Create Primary School Fees:':'http://127.0.0.1:8000/api/primary/fees/add/',
        'List Create High School Fees:':'http://127.0.0.1:8000/api/higschool/fees/add/',
        'List Create Primary School Fees Payments:':'http://127.0.0.1:8000/api/primary/feespayments/add/',
        'List Create High School Fees Payments:':'http://127.0.0.1:8000/api/highschool/feespayments/add/',
        #List Details
        'Retrieve Update Destroy Primary School:':'http://127.0.0.1:8000/api/primary/list/1/',
        'Retrieve Update Destroy High School:':'http://127.0.0.1:8000/api/highschool/list/1/',
        'Retrieve Update Destroy Primary School Fees Payments:':'http://127.0.0.1:8000/api/primary/feespayments/list/1/',
        'Retrieve Update Destroy High School Fees Payments:':'http://127.0.0.1:8000/api/highschool/feespayments/list/1/',
        'Retrieve Update Destroy Primary School Fees:':'http://127.0.0.1:8000/api/primary/fees/list/1/',
        'Retrieve Update Destroy High School Fees:':'http://127.0.0.1:8000/api/highschool/fees/list/1/',
        
        

        
    }
    return Response(api_urls)

# Post Views
class PostHighSchoolStudents(generics.ListCreateAPIView):
    queryset = models.HighSchoolStudent.objects.all()
    serializer_class = serializers.PostHighSchoolStudentsSerializer

class PostPrimaryStudents(generics.ListCreateAPIView):
    queryset = models.PrimaryStudent.objects.all()
    serializer_class = serializers.PostPrimaryStudentsSerializer

class PostPrimaryFeesPayments(generics.ListCreateAPIView):
    queryset = models.PrimaryFeesPayment.objects.all()
    serializer_class = serializers.PostPrimaryFeesPaymentSerializer

class PostHighSchoolFeesPayments(generics.ListCreateAPIView):
    queryset = models.HighschoolFeesPayment.objects.all()
    serializer_class = serializers.PostHighSchoolFeesPaymentSerializer

class PostPrimaryFees(generics.ListCreateAPIView):
    queryset = models.PrimaryFee.objects.all()
    serializer_class = serializers.PostPrimaryFeesSerializer

class PostHighschoolFees(generics.ListCreateAPIView):
    queryset = models.HighschoolFee.objects.all()
    serializer_class = serializers.PostHighschoolFeesSerializer



# List Views
class ListPrimaryStudents(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PrimaryStudent.objects.all()
    serializer_class = serializers.PostPrimaryStudentsSerializer

class ListHighSchoolStudents(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.HighSchoolStudent.objects.all()
    serializer_class = serializers.PostHighSchoolStudentsSerializer

class ListPrimarySchoolFeesPayments(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PrimaryFeesPayment.objects.all()
    serializer_class = serializers.PostPrimaryFeesPaymentSerializer

class ListHighschoolFeesPayments(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.HighschoolFeesPayment.objects.all()
    serializer_class = serializers.PostHighSchoolFeesPaymentSerializer

class ListPrimaryFees(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PrimaryFee.objects.all()
    serializer_class = serializers.PostPrimaryFeesSerializer