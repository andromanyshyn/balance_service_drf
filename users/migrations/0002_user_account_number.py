# Generated by Django 4.2 on 2023-05-27 08:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='account_number',
            field=models.UUIDField(default=uuid.UUID('6176e09f-9cda-484e-9b99-c3f25e1fcfc3')),
        ),
    ]
