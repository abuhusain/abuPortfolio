from django.contrib import admin

# Register your models here.
# Import Job from .model of job
from .models import Blog

# now register this Job to admin site
admin.site.register(Blog)