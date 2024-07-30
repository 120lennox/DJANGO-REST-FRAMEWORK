from django.urls import path
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetList),
    path('snippets/<int:pk>/', views.SnippetDetail),
]
