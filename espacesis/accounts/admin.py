from django.contrib import admin

from .models import UserModel

@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
   # prepopulated_fields = {'slug' : ('username',)}
    pass
