# Generated by Django 5.0 on 2024-04-16 14:30

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0014_alter_ad_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('273a0a1c-955a-49a3-89bf-d0ff74100adb'), editable=False, primary_key=True, serialize=False),
        ),
    ]