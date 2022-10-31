from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Company
admin.site.site_header = "PataJob Admin"
admin.site.site_title = "PataJob Admin Dashboard"
admin.site.index_title = "Welcome to PataJob Admin Dashboard"
admin.site.unregister(User)
admin.site.unregister(Group)
# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'established_date', 'location',
                    'corporation_type', 'company_size')
    list_filter = ('established_date', 'location',
                   'corporation_type', 'company_size')
    sortable_by = ('name', 'established_date', 'location',
                   'corporation_type', 'company_size')
    search_fields = ('name', 'established_date', 'location')
    ordering = ('name', 'established_date', 'location')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(created_by=request.user.id)


admin.site.register(Company, CompanyAdmin)
