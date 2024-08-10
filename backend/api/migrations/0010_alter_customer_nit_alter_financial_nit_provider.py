# Generated by Django 5.0.2 on 2024-07-13 21:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_financial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='nit',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='financial',
            name='nit_provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provider', to=settings.AUTH_USER_MODEL, to_field='nit'),
        ),
    ]
