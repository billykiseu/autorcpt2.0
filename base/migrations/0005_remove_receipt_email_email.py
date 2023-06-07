# Generated by Django 4.2.1 on 2023-06-05 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_receipt_pending'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipt',
            name='email',
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.EmailField(max_length=254)),
                ('receipt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.receipt')),
            ],
        ),
    ]
