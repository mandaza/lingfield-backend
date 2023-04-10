from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.HighSchoolStudent)
admin.site.register(models.PrimaryStudent)
admin.site.register(models.HighschoolFee)
admin.site.register(models.PrimaryFee)
admin.site.register(models.HighschoolFeesPayment)
admin.site.register(models.PrimaryFeesPayment)