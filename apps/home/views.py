from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def home(request):
    title = 'ONEKKOM'
    return render(request, 'home.html', {'title': title})