from django.contrib import admin
from . models import UserDetails

# Register your models here.
@admin.register(UserDetails)
class AdminUserDetails(admin.ModelAdmin):
    list_display = ('Username','Password')
    # search_fields = ('Username','email', 'Password')
    # class Meta:
    #     model = UserDetails

# admin.site.register(UserDetails)