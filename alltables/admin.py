from django.contrib import admin
from alltables.models import UserProfile
from . import models

admin.site.register(models.Characters)
admin.site.register(models.Owls)
admin.site.register(models.Letters)
admin.site.register(models.TestForm)
# admin.site.site_header = 'Administration'
admin.site.site_title = 'Owls'

class UserProfileAdmin(admin.ModelAdmin):
    # how to display colmns in admin
    list_display = ('user', 'description', 'where_from', 'phone')
    # how to change name of column in admin
    def where_from(self, obj):
        return obj.city

    #sort by phone 
    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-phone')
        return queryset
    #if you want user special words for name of column
    where_from.short_description = 'Where'
admin.site.register(UserProfile, UserProfileAdmin)
