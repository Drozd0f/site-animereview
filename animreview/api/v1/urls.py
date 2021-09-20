from django.urls import path

from .views import PostShowView

urlpatterns = [
    path('review', PostShowView.as_view())
]
