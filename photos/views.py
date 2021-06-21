from django.shortcuts import render, redirect
from .models import Photo
from .forms import PhotoForm


# Create your views here.

def home(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PhotoForm()
        images = Photo.objects.all()
        context = {
            'form': form,
            'images': images
        }
        return render(request, 'home.html', context)
