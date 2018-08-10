from django.shortcuts import render
from .models import Images

# Create your views here.

def gallery_view(request):

	images = Images.objects.all()

	return render(request, 'gallery/gallery.html', {'images':images})
