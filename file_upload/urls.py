from django.urls import path
from . import views
from .views import(
    HomeView,
    DocumentListView,
    DocumentCreateView,
    DocumentDeleteView,
)

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('docs/<int:pk>/', views.DocumentDeleteView.as_view(), name='delete_document'),
    path('docs/', views.DocumentListView.as_view(), name='document_list'),
    path('upload/', views.DocumentCreateView.as_view(), name='document_new'),
]