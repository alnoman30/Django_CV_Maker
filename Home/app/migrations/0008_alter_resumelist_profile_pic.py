# Generated by Django 4.1.7 on 2023-02-21 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_resumelist_job_details_01_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumelist',
            name='profile_pic',
            field=models.ImageField(blank=True, default='Picture/default.jpg', null=True, upload_to='Picture/'),
        ),
    ]
