from django.contrib import admin
from .models import CustomUser, UserProfile, Property, Unit, Tenant

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)
admin.site.register(Property)
admin.site.register(Unit)
admin.site.register(Tenant)