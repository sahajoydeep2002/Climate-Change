from django.contrib import admin
from quiz.models import quesModel


class quizAdmin(admin.ModelAdmin):
    list_display = ('ques', 'opt1', 'opt2', 'opt3', 'opt4', 'ans', 'level')


admin.site.register(quesModel, quizAdmin)
# Register your models here.
