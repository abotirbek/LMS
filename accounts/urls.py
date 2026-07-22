from django.urls import path
from accounts import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('', views.show_home, name='home'),

    path('teacher_list/', views.get_teacher, name='teacher_list'),
    path('create_teacher/', views.create_teacher, name='create_teacher'),
    path('read_teacher/<int:pk>/', views.read_teacher, name='read_teacher'),
    path('update_teacher/<int:pk>/', views.update_teacher, name='update_teacher'),
    path('delete_teacher/<int:pk>/', views.delete_teacher, name='delete_teacher'),

    path('student_list/', views.get_student, name='student_list'),
    path('create_student/', views.create_student, name='create_student'),
    path('read_student/<int:pk>/', views.read_student, name='read_student'),
    path('update_student/<int:pk>/', views.update_student, name='update_student'),
    path('delete_student/<int:pk>/', views.delete_student, name='delete_student'),
]