# Generated by Django 5.2.3 on 2025-06-21 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='is_admin_user',
            field=models.BooleanField(default=False),
        ),
    ]
