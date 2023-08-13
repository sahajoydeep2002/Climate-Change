from django.contrib import admin
from contributers.models import contributersDetails


class contributerAdmin(admin.ModelAdmin):
    list_display = ('c_name', 'c_image', 'c_bio')


admin.site.register(contributersDetails, contributerAdmin)
# Register your models here.
