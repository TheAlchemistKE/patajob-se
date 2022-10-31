from django.contrib import admin
from .models import Job

# Register your models here.


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'work_type', 'career_level', 'minimum_salary', 'maximum_salary', 'role')
    list_filter =  ('title', 'work_type', 'career_level', 'minimum_salary', 'maximum_salary', 'role')
    sortable_by =  ('title', 'work_type', 'career_level', 'minimum_salary', 'maximum_salary', 'role')
    search_fields =  ('title', 'work_type', 'career_level', 'minimum_salary', 'maximum_salary', 'role')
    ordering =  ('title', 'work_type', 'career_level', 'minimum_salary', 'maximum_salary', 'role')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(created_by=request.user.id)


admin.site.register(Job, JobAdmin)
