from django.urls import path
from .views import HerbsListView, HerbDetailView
urlpatterns = [
    path('', HerbsListView.as_view(), name='home'),
    path('herb/<int:pk>/', HerbDetailView.as_view(), name='herb'),
]   