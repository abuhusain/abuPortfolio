from django.shortcuts import render

from .models import Job

# home is function. use this function in urls.py
def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})
    
