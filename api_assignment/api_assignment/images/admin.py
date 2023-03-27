from django.contrib import admin
from images.models import User, Image, Profile


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',)
    search_fields = ('user__email', 'user__first_name', 'user__last_name', '')


admin.site.register(User, UserAdmin)
admin.site.register(Image)
admin.site.register(Profile)
