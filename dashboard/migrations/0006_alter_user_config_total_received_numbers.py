# Generated by Django 4.0 on 2022-03-03 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_user_config'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_config',
            name='total_received_numbers',
            field=models.IntegerField(default=0),
        ),
    ]