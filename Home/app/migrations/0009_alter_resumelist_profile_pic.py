# Generated by Django 4.1.7 on 2023-02-21 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_resumelist_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumelist',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='Picture/'),
        ),
    ]
