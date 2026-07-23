from django.urls import path
from . import views

app_name = 'attendance'

urlpatterns = [
    path('', views.get_attendance, name='attendance_list'),
    path('create/', views.create_attendance, name='create_attendance'),
    path('<int:pk>/', views.read_attendance, name='read_attendance'),
    path('<int:pk>/update/', views.update_attendance, name='update_attendance'),
    path('<int:pk>/delete/', views.delete_attendance, name='delete_attendance'),
]