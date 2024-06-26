# Generated by Django 3.2.23 on 2024-05-11 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=500)),
                ('last_name', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=50)),
                ('address', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=20)),
                ('date_of_join', models.DateField(auto_now_add=True)),
                ('parent_name', models.CharField(max_length=500)),
            ],
        ),
    ]
