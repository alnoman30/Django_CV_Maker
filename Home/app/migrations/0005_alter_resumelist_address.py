# Generated by Django 4.1.7 on 2023-02-21 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_resumelist_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumelist',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
