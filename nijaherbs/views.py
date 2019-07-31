# Create your views here.
from django.views.generic import ListView, DetailView
from django.db.models import Q

from . models import Herb, Category

class HerbsListView(ListView):
    model = Herb
    template_name = 'home.html'



class HerbDetailView(DetailView):
    model = Herb
    template_name = 'herb.html'


class SearchResultsView(ListView):
    model = Herb
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Herb.objects.filter(
            Q(local_Name__icontains=query) | Q(english_Name__icontains=query) | Q(botanical_Name__icontains=query)
        )

        return object_list

class EdibleView(ListView):
    model = Herb
    template_name = 'edible.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Herb.objects.filter(category__name__icontains='edible')

        return object_list

class MedicinalView(ListView):
    model = Herb
    template_name = 'medicinal.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Herb.objects.filter(category__name__icontains='medicinal')

        return object_list