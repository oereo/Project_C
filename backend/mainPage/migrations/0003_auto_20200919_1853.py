# Generated by Django 2.1.1 on 2020-09-19 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='safe_percent',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
