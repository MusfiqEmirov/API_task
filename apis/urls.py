from django.urls import path
from .views import *

app_name = "apis"

urlpatterns = [
    path(
        'books',
        BookAPIView.as_view(),
        name="books"
    ),
    path(
        'books/<int:id>/',
        BookIdDetailView.as_view(),
        name="book-detail"
    ),
    path(
        'book/<slug:slug>/',
        BookSlugDeatil.as_view(),
        name="book-slug-detail"
    )
    
]