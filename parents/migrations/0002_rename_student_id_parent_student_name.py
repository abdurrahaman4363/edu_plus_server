# Generated by Django 4.2.7 on 2024-05-12 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parents', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parent',
            old_name='student_ID',
            new_name='student_name',
        ),
    ]
