from django.contrib import admin
from userprofiledetails.models import Profile


class userprofileAdmin(admin.ModelAdmin):
    list_display=('user','profile_image')
    




admin.site.register(Profile,userprofileAdmin)
# Register your models here.
