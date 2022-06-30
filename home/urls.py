from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='home-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('add/new/', PostCreateView.as_view(), name='post-create'),
    path('add/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('add/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
