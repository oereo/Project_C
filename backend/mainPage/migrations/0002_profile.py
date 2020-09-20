# Generated by Django 2.1.1 on 2020-09-19 09:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainPage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worker_number', models.TextField(blank=True, max_length=500)),
                ('instrument_number', models.CharField(blank=True, max_length=30)),
                ('safe_percent', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profileUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]