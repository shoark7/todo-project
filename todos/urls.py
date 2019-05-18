from django.urls import path
from . import views


urlpatterns = [
    path('', views.todos_list, name='todos-list'),
    path('new', views.todos_new, name='todos-new'),
    path('<int:pk>/delete', views.todos_delete, name='todos-delete'),
    path('<int:pk>/solve_toggle', views.solve_toggle, name='solve-toggle'),
    path('<int:pk>/update', views.todos_update, name='todos-update'),
]
