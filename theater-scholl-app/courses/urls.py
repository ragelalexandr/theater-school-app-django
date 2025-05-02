# Файл: theater-scholl-app/courses/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.courses_list, name="courses_list"),
    path('admin/moderate_reviews/', views.moderate_reviews, name='moderate_reviews'),
    path('admin/update_review_status/<int:review_id>/<str:new_status>/', views.update_review_status, name='update_review_status'),
    path('courses/enroll/<int:courses_id>/', views.enroll_courses, name='enroll_courses'),
    path('course/<int:course_id>/add_review/', views.add_review, name='add_review'),
    path('enrollments/', views.enrollment_history, name='enrollment_history'),
    path('enroll/<int:course_id>/', views.enroll, name='enroll'),
    path('enroll/<int:courses_id>/', views.enroll, name="enroll"),
    path('list/', views.courses_list, name='courses_list'),
    path("portfolio/", views.portfolio_list, name="portfolio_list"),
    path("portfolio/add/", views.add_portfolio, name="add_portfolio"),
    path('schedule/', views.courses_schedule, name='courses_schedule'),
    path("schedule/", views.courses_schedule, name="courses_schedule"),
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('teacher/enrollment/<int:enrollment_id>/<str:new_status>/', views.update_enrollment_status, name='update_enrollment_status'),
]


    


    

