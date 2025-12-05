from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('student/add/', views.add_student, name='add_student'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
    path('student/<int:student_id>/attendance/add/', views.add_attendance, name='add_attendance'),
    path('student/<int:student_id>/marks/add/', views.add_mark, name='add_mark'),
]
