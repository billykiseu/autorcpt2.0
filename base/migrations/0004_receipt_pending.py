# Generated by Django 4.2.1 on 2023-06-01 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_receipt_amount_receipt_date_receipt_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='pending',
            field=models.BooleanField(default=False),
        ),
    ]
