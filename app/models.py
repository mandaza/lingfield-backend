from turtle import update
from django.db import models
from django.contrib.auth.models import User

# Primary School Students--------------
class PrimaryStudent(models.Model):
    grades = (
        ('ecd', 'ECD'),
        ('grade 1', 'Grade 1'),
        ('grade 2', 'Grade 2'),
        ('grade 3', 'Grade 3'),
        ('grade 4', 'Grade 4'),
        ('grade 5', 'Grade 5'),
        ('grade 6', 'Grade 6'),
        ('grade 7', 'Grade 7'),
    )
    facilities = (
        ('boarding', 'Boarding'),
        ('day', 'Day'),
    )
    sex = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    firstname = models.CharField(max_length=100, null=True)
    middlename = models.CharField(max_length=100, null=True)
    surname = models.CharField(max_length=100,null=True)
    prefname = models.CharField(max_length=100, null=True)
    dob = models.DateField()
    nationality = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=50, choices=sex )
    grade = models.CharField( max_length=30, choices=grades)
    facility = models.CharField( max_length=30, choices=facilities)
    nationalid = models.CharField(max_length=100, null=True)
    languages = models.CharField(max_length=255, null=True)
    religion = models.CharField(max_length=100, null=True)
    denomination = models.CharField(max_length=100, null=True)
    medical_condition = models.CharField(max_length=255, null= True)
    approved = models.CharField(max_length= 10, null=True)
    createdAt = models.DateField(auto_now=True)
    updatedAt = models.DateField(auto_now_add=True)

    def __str__(self):
        return  self.firstname

#High School Students --------------------------------
class HighSchoolStudent(models.Model):

    forms = (
        ('form 1', 'Form 1'),
        ('form 2', 'Form 2'),
        ('form 3', 'Form 3'),
        ('form 4', 'Form 4'),
        ('form 5', 'Form 5'),
        ('form 6', 'Form 6'),
    )
    facilities = (
        ('boarding', 'Boarding'),
        ('day', 'Day'),
    )
    sex = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    firstname = models.CharField(max_length=100 )
    middlename = models.CharField(max_length=100 )
    surname = models.CharField(max_length=100)
    prefname = models.CharField(max_length=100, null=True)
    dob = models.DateField()
    nationality = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=50, choices=sex)
    form = models.CharField( max_length=30, choices=forms )
    facility = models.CharField( max_length=30, choices=facilities )
    nationalid = models.CharField(max_length=100, null=True)
    languages = models.CharField(max_length=255, null=True)
    religion = models.CharField(max_length=100, null=True)
    denomination = models.CharField(max_length=100, null=True)
    medical_condition = models.CharField(max_length=255, null= True)
    approved = models.CharField(max_length= 10, null=True)
    createdAt = models.DateField(auto_now=True)
    updatedAt = models.DateField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return  self.firstname

#Primary School Fees --------------------------------------
class PrimaryFee(models.Model):
    boading = models.IntegerField(null=True)
    day = models.IntegerField(null=True)
    createdAt = models.DateField(auto_now=True)
    updatedAt = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.boading

#High School Fees -------------------------------------------
class HighschoolFee(models.Model):
    boading = models.IntegerField(null=True)
    day = models.IntegerField(null=True)
    createdAt = models.DateField(auto_now=True)
    updatedAt = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.id

#Primary School Fees Payments--------------------------------
class PrimaryFeesPayment(models.Model):
    options = (
        ('levy', 'Levy'),
        ('tuition', 'Tuition'),
    )
    currencys = (
        ('usd cash', 'USD Cash'),
        ('zwl cash', 'ZWL Cash'),
        ('usd bank', 'USD Bank'),
        ('rtgs bank', 'RTGS Bank'),
    )
    terms = (
        ('term 1', 'Term 1'),
        ('term 2', 'Term 2'),
        ('term 3', 'Term 3'),
    )
    student_id = models.ForeignKey(
        PrimaryStudent, on_delete=models.CASCADE
    )
    invNo = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100, choices=options)
    currency = models.CharField( max_length=30, choices=currencys)
    year = models.DateTimeField(auto_now=True)
    terms = models.CharField( max_length=30, choices=terms)
    payment = models.IntegerField(null= True)
    balance = models.IntegerField(null=True)
    createdAt = models.DateField(auto_now=True)
    updatedAt = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.invNo

#High School Fees Payments--------------------------------
class  HighschoolFeesPayment(models.Model): 
    options = (
        ('levy', 'Levy'),
        ('tuition', 'Tuition'),
    )
    currencys = (
        ('usd cash', 'USD Cash'),
        ('zwl cash', 'ZWL Cash'),
        ('usd bank', 'USD Bank'),
        ('rtgs bank', 'RTGS Bank'),
    )
    terms = (
        ('term 1', 'Term 1'),
        ('term 2', 'Term 2'),
        ('term 3', 'Term 3'),
    )
    student_id = models.ForeignKey( HighSchoolStudent, on_delete=models.CASCADE)
    invNo = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100, choices=options)
    currency = models.CharField(max_length=30, choices=currencys)
    year = models.DateTimeField()
    terms = models.CharField(max_length=30, choices=terms)
    payment = models.IntegerField(null= True)
    balance = models.IntegerField(null= True)
    createdAt = models.DateField(auto_now=True)
    updatedAt = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.invNo

#Miscellaneous Payments-------------------------------

class MiscellaneousPaymentsPrimary(models.Model):
    currencys = (
        ('usd cash', 'USD Cash'),
        ('zwl cash', 'ZWL Cash'),
        ('usd bank', 'USD Bank'),
        ('rtgs bank', 'RTGS Bank'),
    )
    options = (
        ('transport','Transport'),
        ('meals', 'Meals'),
        ('uniforms', 'Uniforms'),
    )
    years = (
        ('2020','2020'),
        ('2021','2021'),
        ('2022','2022'),
        ('2023','2023'),
        ('2024','2024'),
        ('2025','2025'),
    )
    months = (
        ('january', 'January'),
        ('february', 'February'),
        ('march', 'March'),
        ('April', 'April'),
        ('may', 'May'),
        ('june', 'June'),
        ('july', 'July'),
        ('august', 'August'),
        ('september', 'September'),
        ('october', 'October'),
        ('november', 'November'),
        ('december', 'December'),
    )
    student_id = models.ForeignKey(PrimaryStudent, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, choices=options)
    currency = models.CharField(max_length=30, choices=currencys)
    year = models.CharField(max_length=30, choices=years)
    month = models.CharField(max_length=50, choices=months)
    payment = models.IntegerField(null=True)
    createdAt = models.DateField(auto_now=True)
    updateAt = models.DateField(auto_now_add=True)


    #Miscellaneous Highschool Payments


class MiscellaneousPaymentsHighschool(models.Model):
    currencys = (
        ('usd cash', 'USD Cash'),
        ('zwl cash', 'ZWL Cash'),
        ('usd bank', 'USD Bank'),
        ('rtgs bank', 'RTGS Bank'),
    )
    options = (
        ('transport','Transport'),
        ('meals', 'Meals'),
        ('uniforms', 'Uniforms'),
    )
    years = (
        ('2020','2020'),
        ('2021','2021'),
        ('2022','2022'),
        ('2023','2023'),
        ('2024','2024'),
        ('2025','2025'),
    )
    months = (
        ('january', 'January'),
        ('february', 'February'),
        ('march', 'March'),
        ('April', 'April'),
        ('may', 'May'),
        ('june', 'June'),
        ('july', 'July'),
        ('august', 'August'),
        ('september', 'September'),
        ('october', 'October'),
        ('november', 'November'),
        ('december', 'December'),
    )
    student_id = models.ForeignKey(HighSchoolStudent, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, choices=options)
    currency = models.CharField(max_length=30, choices=currencys)
    year = models.CharField(max_length=30, choices=years)
    month = models.CharField(max_length=50, choices=months)
    payment = models.IntegerField(null=True)
    createdAt = models.DateField(auto_now=True)
    updateAt = models.DateField(auto_now_add=True)