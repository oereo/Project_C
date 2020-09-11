# Generated by Django 2.1.1 on 2020-09-11 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='business_number',
            field=models.CharField(choices=[('blue', 'blue'), ('red', 'red')], max_length=30, null=True, unique=True),
        ),
    ]