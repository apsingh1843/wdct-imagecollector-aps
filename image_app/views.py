from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageForm
from .models import ImageCollector


# Create your views here.


def index(request):
    img = ImageCollector.objects.all()
    return render(request, 'image_app/index.html', {'img': img})


@login_required(login_url='/authentication/login')
def userform(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img = ImageCollector.objects.all()
            messages.success(request, 'image uploaded successfully.')
            return render(request, 'image_app/index.html', {'img': img})

    form = ImageForm()
    return render(request, 'userform.html', {'form': form})
