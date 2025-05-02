# Файл: theater-scholl-app/core/urls.py
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core import views
from courses import views as courses_views
from . import views
from core.views import delete_account, profile
from core.views import courses_list  # Убедись, что это представление существует
from core.views import courses_schedule  # Убедись, что представление существует
from django.contrib.auth.views import PasswordResetDoneView, LoginView
from .views import (
    create_course, edit_course, delete_course,
    home, courses, about, contacts, admin_dashboard,
    create_performance, edit_performance, delete_performance,
    edit_course, delete_course, create_course,
    create_instructor, edit_instructor, delete_instructor,
    create_student, edit_student, delete_student,
    approve_review, delete_review,  instructor_dashboard, student_dashboard
)


urlpatterns = [
    path("login/", LoginView.as_view(template_name="core/login.html"), name="login"),

    path('', home, name='home'),
    path("", views.courses_list, name="courses_list"),
    
    path('about/', about, name='about'),    

    path('admin/course/create/', create_course, name='create_course'),
    path('admin/course/edit/<int:id>/', edit_course, name='edit_course'),
    path('admin/course/delete/<int:id>/', delete_course, name='delete_course'),
    path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),

    path('admin/instructor/create/', create_instructor, name='create_instructor'),
    path('admin/instructor/edit/<int:id>/', edit_instructor, name='edit_instructor'),
    path('admin/instructor/delete/<int:id>/', delete_instructor, name='delete_instructor'),

    path('admin/performance/edit/<int:id>/', edit_performance, name='edit_performance'),
    path('admin/performance/delete/<int:id>/', delete_performance, name='delete_performance'),
    path('admin/performance/create/', create_performance, name='create_performance'),
    path('admin/performance/edit/<int:id>/', edit_performance, name='edit_performance'),
    path('admin/performance/delete/<int:id>/', delete_performance, name='delete_performance'),

    path('admin/review/approve/<int:id>/', approve_review, name='approve_review'),
    path('admin/review/delete/<int:id>/', delete_review, name='delete_review'),

    path('admin/student/create/', create_student, name='create_student'),
    path('admin/student/edit/<int:id>/', edit_student, name='edit_student'),
    path('admin/student/delete/<int:id>/', delete_student, name='delete_student'),

    path('contacts/', contacts, name='contacts'),
    path('courses/', courses, name='courses'),

    path("delete_account/", views.delete_account, name="delete_account"),    
    path('delete_account/', delete_account, name='delete_account'),

    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path("login/", auth_views.LoginView.as_view(template_name="core/login.html"), name="login"),
    # path("logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    
    path('instructor/dashboard/', instructor_dashboard, name='instructor_dashboard'),

    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="core/password_reset.html"), name="password_reset"),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name="core/password_reset_done.html"), name='password_reset_done'), 
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(template_name="core/password_change.html"),
        name="password_change"
    ),
    path(
        "password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(template_name="core/password_change_done.html"),
        name="password_change_done"
    ),
    path("profile/", views.profile, name="profile"),
    path('profile/', profile, name='profile'),

    path("register/", views.register, name="register"),

    path("schedule/", views.courses_schedule, name="courses_schedule"),
    path('student/dashboard/', student_dashboard, name='student_dashboard'),
]
