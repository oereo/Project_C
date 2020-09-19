from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group

# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display = ['email', 'nickname', 'business_number']

admin.site.register(User, userAdmin)

admin.site.unregister(Group)