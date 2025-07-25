from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render
from .models import UserProfile

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


@user_passes_test(is_admin)
@login_required
def admin_dashboard(request):
    return render(request, 'admin_view.html')

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
