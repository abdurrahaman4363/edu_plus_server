# Generated by Django 5.0.6 on 2024-05-12 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_remove_teacher_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, upload_to='teachers/image/'),
        ),
    ]