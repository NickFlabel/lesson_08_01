# Generated by Django 5.0.1 on 2024-01-22 13:56

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('d5feec26-9c92-460a-8fce-1a98499e63a3'), editable=False, primary_key=True, serialize=False),
        ),
    ]