from django.contrib import admin
from baseapp.models import Tasks, SubTasks1, Properties, Questions, Profile


# Register your models here.
admin.site.register(Tasks),
admin.site.register(SubTasks1),
admin.site.register(Properties),
admin.site.register(Questions),

admin.site.register(Profile),



#from django.contrib.auth.admin import UserAdmin

#@admin.register(Tasks)
#class TasksAdmin(admin.ModelAdmin):
#   task_display = ('task_name','creator')