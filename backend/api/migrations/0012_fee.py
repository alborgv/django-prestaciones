# Generated by Django 5.0.2 on 2024-07-16 18:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_customer_nit_provider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('paid', models.CharField(max_length=100)),
                ('fee_num', models.CharField(max_length=100)),
                ('financial_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='financial_id', to='api.financial')),
            ],
        ),
    ]
