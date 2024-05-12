# Generated by Django 3.2.23 on 2024-05-12 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], max_length=10)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student', verbose_name='classattendence')),
            ],
        ),
    ]
