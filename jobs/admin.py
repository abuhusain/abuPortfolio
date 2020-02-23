from django.contrib import admin

# Import Job from .model of job
from .models import Job

# now register this Job to admin site
admin.site.register(Job)