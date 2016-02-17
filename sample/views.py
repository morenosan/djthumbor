from django.views.generic import ListView
from .models import Image


class ImageListView(ListView):
    model = Image
