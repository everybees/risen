from django.urls import path
from . import views


urlpatterns = [
    path('create_native', views.create_page),
    path('view_all_natives', views.get_all_natives, name='natives'),
    path('view_one_native', views.create_page),
    path('delete_one_native', views.create_page),
    path('update_a_native', views.create_page),
]
