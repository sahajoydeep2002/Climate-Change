from django.contrib import admin
from contactenquiry.models import contactenquiry


class contactQueryAdmin(admin.ModelAdmin):
    list_display = ('contact_name', 'contact_email', 'contact_desc')


admin.site.register(contactenquiry, contactQueryAdmin)


# Register your models here.
