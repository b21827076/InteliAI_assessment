from django.shortcuts import render
from .forms import UploadForm
from .models import User

def index(request):
    print(request)
    return render(request, 'assessment/index.html')

def results(request):
    users = User.objects.all()
    context = {"usersList" : users}
    return render(request, 'assessment/results.html', context)

def save(request):
    if request.POST:
        form = UploadForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
        return render(request,"assessment/index.html")
    return render(request,'assessment/save.html',{"form": UploadForm})
