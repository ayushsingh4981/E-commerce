from django.contrib import admin

# Register your models here.
from userauths.models import User

class Useradmin(admin.ModelAdmin):
    list_display = ['username','email','first_name', 'last_name','bio']
    
admin.site.register(User,Useradmin)
