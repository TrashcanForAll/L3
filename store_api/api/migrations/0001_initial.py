# Generated by Django 5.1.3 on 2024-11-30 17:19

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(default=uuid.UUID('de8019bf-9a01-4900-abd3-fc48d1657391'), max_length=36)),
            ],
        ),
    ]