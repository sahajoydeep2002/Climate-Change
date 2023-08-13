from django.contrib import admin
from blog.models import blogPost


class blogAdimin(admin.ModelAdmin):
    list_display=('author_name','title','content','date_posted')



admin.site.register(blogPost,blogAdimin)
# Register your models here.
