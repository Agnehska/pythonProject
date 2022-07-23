from django.urls import path
from .views import *

urlpatterns = [
    path('', citizens, name='citizens'),
    # path('', Men.as_view(), name='citizens'),
    path('create', create, name='create'),
    path('<int:pk>', ManDetailView.as_view(), name='show'),
    path('<int:pk>/update', ManUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', ManDeleteView.as_view(), name='delete'),
]