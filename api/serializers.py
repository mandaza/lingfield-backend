from dataclasses import fields
from rest_framework import serializers
from app import models

class PostHighSchoolStudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HighSchoolStudent
        fields = '__all__'

class PostPrimaryStudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PrimaryStudent
        fields = '__all__'

class PostPrimaryFeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PrimaryFee
        fields = '__all__'

class PostHighschoolFeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HighschoolFee
        fields = '__all__'
        
class PostHighSchoolFeesPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HighschoolFeesPayment
        fields = '__all__'

class PostPrimaryFeesPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PrimaryFeesPayment
        fields = '__all__'