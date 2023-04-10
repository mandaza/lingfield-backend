# Generated by Django 4.0.4 on 2022-05-11 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HighschoolFee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boading', models.IntegerField(null=True)),
                ('day', models.IntegerField(null=True)),
                ('createdAt', models.DateField(auto_now=True)),
                ('updatedAt', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HighSchoolStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('middlename', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('prefname', models.CharField(max_length=100, null=True)),
                ('dob', models.DateField()),
                ('nationality', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=50)),
                ('form', models.CharField(choices=[('form 1', 'Form 1'), ('form 2', 'Form 2'), ('form 3', 'Form 3'), ('form 4', 'Form 4'), ('form 5', 'Form 5'), ('form 6', 'Form 6')], max_length=30)),
                ('facility', models.CharField(choices=[('boarding', 'Boarding'), ('day', 'Day')], max_length=30)),
                ('nationalid', models.CharField(max_length=100, null=True)),
                ('languages', models.CharField(max_length=255, null=True)),
                ('religion', models.CharField(max_length=100, null=True)),
                ('denomination', models.CharField(max_length=100, null=True)),
                ('medical_condition', models.CharField(max_length=255, null=True)),
                ('approved', models.CharField(max_length=10, null=True)),
                ('createdAt', models.DateField(auto_now=True)),
                ('updatedAt', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PrimaryFee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boading', models.IntegerField(null=True)),
                ('day', models.IntegerField(null=True)),
                ('createdAt', models.DateField(auto_now=True)),
                ('updatedAt', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PrimaryStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100, null=True)),
                ('middlename', models.CharField(max_length=100, null=True)),
                ('surname', models.CharField(max_length=100, null=True)),
                ('prefname', models.CharField(max_length=100, null=True)),
                ('dob', models.DateField()),
                ('nationality', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=50)),
                ('grade', models.CharField(choices=[('ecd', 'ECD'), ('grade 1', 'Grade 1'), ('grade 2', 'Grade 2'), ('grade 3', 'Grade 3'), ('grade 4', 'Grade 4'), ('grade 5', 'Grade 5'), ('grade 6', 'Grade 6'), ('grade 7', 'Grade 7')], max_length=30)),
                ('facility', models.CharField(choices=[('boarding', 'Boarding'), ('day', 'Day')], max_length=30)),
                ('nationalid', models.CharField(max_length=100, null=True)),
                ('languages', models.CharField(max_length=255, null=True)),
                ('religion', models.CharField(max_length=100, null=True)),
                ('denomination', models.CharField(max_length=100, null=True)),
                ('medical_condition', models.CharField(max_length=255, null=True)),
                ('approved', models.CharField(max_length=10, null=True)),
                ('createdAt', models.DateField(auto_now=True)),
                ('updatedAt', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PrimaryFeesPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invNo', models.CharField(max_length=100)),
                ('purpose', models.CharField(choices=[('levy', 'Levy'), ('tuition', 'Tuition')], max_length=100)),
                ('currency', models.CharField(choices=[('usd cash', 'USD Cash'), ('zwl cash', 'ZWL Cash'), ('usd bank', 'USD Bank'), ('rtgs bank', 'RTGS Bank')], max_length=30)),
                ('year', models.DateTimeField(auto_now=True)),
                ('terms', models.CharField(choices=[('term 1', 'Term 1'), ('term 2', 'Term 2'), ('term 3', 'Term 3')], max_length=30)),
                ('payment', models.IntegerField(null=True)),
                ('balance', models.IntegerField(null=True)),
                ('createdAt', models.DateField(auto_now=True)),
                ('updatedAt', models.DateField(auto_now_add=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.primarystudent')),
            ],
        ),
        migrations.CreateModel(
            name='HighschoolFeesPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invNo', models.CharField(max_length=100)),
                ('purpose', models.CharField(choices=[('levy', 'Levy'), ('tuition', 'Tuition')], max_length=100)),
                ('currency', models.CharField(choices=[('usd cash', 'USD Cash'), ('zwl cash', 'ZWL Cash'), ('usd bank', 'USD Bank'), ('rtgs bank', 'RTGS Bank')], max_length=30)),
                ('year', models.DateTimeField(auto_now=True)),
                ('terms', models.CharField(choices=[('term 1', 'Term 1'), ('term 2', 'Term 2'), ('term 3', 'Term 3')], max_length=30)),
                ('payment', models.IntegerField(null=True)),
                ('balance', models.IntegerField(null=True)),
                ('createdAt', models.DateField(auto_now=True)),
                ('updatedAt', models.DateField(auto_now_add=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.highschoolstudent')),
            ],
        ),
    ]
