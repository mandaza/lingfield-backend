from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
      #API Overview
      path('', views.apiOverview, name='apioverview'),
      #LIST CREATE ROUTES
      path('primary/add/', views.PostPrimaryStudents.as_view(), name='listcreatprimary'),
      path('highschool/add/', views.PostHighSchoolStudents.as_view(), name='listcreatehigschool'),
      path('highschool/feespayments/add/', views.PostHighSchoolFeesPayments.as_view(), name='listcreatehigschoolfeespayments'),
      path('primary/feespayments/add/',views.PostPrimaryFeesPayments.as_view(), name='listcreatprimaryfeespayment'),
      path('primary/fees/add/', views.PostPrimaryFees.as_view(), name ='listcreateprimaryfees'),
      path('highschool/fees/add/', views.PostHighschoolFees.as_view(), name= 'listcreatehighschoolfees'),
      #LIST ROUTES
      path('primary/list/<int:pk>/', views.ListPrimaryStudents.as_view(), name='listprimary'),
      path('highschool/list/<int:pk>/', views.ListHighSchoolStudents.as_view(), name='listhigschool'),
      path('primary/feespayments/list/<int:pk>/', views.ListPrimarySchoolFeesPayments.as_view(), name='listprimaryfeespayments'),
      path('highschool/feespayments/list/<int:pk>/', views.ListHighschoolFeesPayments.as_view(), name='listhighschoolfeespayments'),
      path('primary/fees/list/<int:pk>/', views.ListPrimaryFees.as_view(), name='listprimaryfees'),
      path('highschool/fees/list/<int:pk>/', views.ListPrimaryFees.as_view(), name='listhighschoolfees'),
]

