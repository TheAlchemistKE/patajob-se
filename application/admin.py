from django.contrib import admin
from .models import Application


# Register your models here.
@admin.action(description='Accept selected applications')
def accept_users(modeladmin, request, queryset):
    queryset.update(decision_status=1)


@admin.action(description='Reject selected applications')
def reject_users(modeladmin, request, queryset):
    queryset.update(decision_status=2)


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('job_id', 'applicant_id', 'applied_date', 'applicant_match_score',
                    'decision_status', 'decision_date')
    list_filter = ('job_id', 'applicant_id', 'applied_date','applicant_match_score',
                   'decision_status', 'decision_date')
    sortable_by = ('job_id', 'applicant_id', 'applied_date',
                   'decision_status', 'decision_date')
    search_fields = ('job_id', 'applicant_id', 'applied_date',
                     'decision_status', 'decision_date')
    ordering = ('job_id', 'applicant_id', 'applied_date',
                'decision_status', 'decision_date')
    actions = [accept_users, reject_users]


admin.site.register(Application, ApplicationAdmin)
