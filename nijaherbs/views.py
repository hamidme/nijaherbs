# Create your views here.
from django.views.generic import ListView, DetailView

from . models import Herb

class HerbsListView(ListView):
    model = Herb
    template_name = 'home.html'


class HerbDetailView(DetailView):
    model = Herb
    template_name = 'herb.html'