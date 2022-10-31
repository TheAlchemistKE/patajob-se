from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('apply/', include('application.urls')),
    path('applicants/', include('applicant.urls')),
    path('jobs/', include('job.urls')),
    path('companies/', include('company.urls')),
    path('contact/', include('contact.urls'))

]
