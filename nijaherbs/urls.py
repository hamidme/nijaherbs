from django.urls import path
from .views import HerbsListView, HerbDetailView, SearchResultsView, EdibleView, MedicinalView
urlpatterns = [
    path('', HerbsListView.as_view(), name='home'),
    path('herb/<int:pk>/', HerbDetailView.as_view(), name='herb'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('edible/', EdibleView.as_view(), name='edible'),
    path('medicinal/', MedicinalView.as_view(), name='medicinal'),
]   
