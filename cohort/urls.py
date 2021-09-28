from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_all_cohorts, name='cohorts'),
    path('create_cohort', views.create_cohort, name='create_cohort'),
    path('view_details_of_a_cohort', views.hello_world),
    path('<int:pk>', views.get_a_cohort),
    path('remove_a_native_from_cohort', views.hello_world),
    path('delete_a_cohort', views.hello_world),
    path('update_a_cohort', views.hello_world),
]
