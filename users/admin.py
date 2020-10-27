from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
from users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']
    search_fields = [
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
    ]


class ProfileInline(admin.StackedInline):
    """
        Modelo que permite regsitrar el usuario y perfil directamente en la misma ventana del admin
        Usando el StackInline
    """
    model = Profile
    can_delete = False
    verbose_name = 'Perfil'


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
