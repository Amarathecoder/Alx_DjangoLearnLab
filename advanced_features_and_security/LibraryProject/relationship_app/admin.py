from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Fields to display in the admin list view
    list_display = (
        'username', 'email', 'first_name', 'last_name',
        'date_of_birth', 'is_staff'
    )

    # Filters on the right sidebar
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')

    # Fields grouped into sections on the edit page
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )

    # Fields shown when creating a new user via the admin
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )

    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
