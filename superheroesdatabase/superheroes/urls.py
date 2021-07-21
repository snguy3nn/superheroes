from django.urls import path
from . import views


app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:superhero_id>/', views.details, name='details'),
    path('new_superhero/', views.create, name='create_superhero'),
    path('edit_superhero<int:id>/', views.edit, name='edit_superhero'),
]