# Generated by Django 4.2.1 on 2023-06-05 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_receipt_email_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='email',
            old_name='address',
            new_name='email',
        ),
    ]
