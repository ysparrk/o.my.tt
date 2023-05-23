# Generated by Django 3.2.12 on 2023-05-23 03:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0003_remove_ott_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='ott',
            name='ott_user',
            field=models.ManyToManyField(related_name='ott_user', to=settings.AUTH_USER_MODEL),
        ),
    ]