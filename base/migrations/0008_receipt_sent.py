# Generated by Django 4.2.1 on 2023-06-06 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_rename_email_email_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='sent',
            field=models.BooleanField(default=False),
        ),
    ]
