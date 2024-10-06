from django.urls import path

from . import views

app_name = 'assessment'
urlpatterns = [
    path("", views.index, name="index"),
    path('createuser/', views.save, name='save'),
    path('users/', views.results, name='results'),
]