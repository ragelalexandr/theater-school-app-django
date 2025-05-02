# Файл: theater-scholl-app/theater-scholl-app/urls.py
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core import views  # Исправлено: убрали дублирующийся импорт
from courses import views as courses_views  # Импорт представлений из 'courses'
from django.contrib import admin


urlpatterns = [
    path('', include('core.urls')),  # Подключение маршрутов из core

    path('accounts/', include('django.contrib.auth.urls')),

    path('admin/', admin.site.urls),  # Добавляем маршрут для админ-панели
    path("", views.index, name="home"),
    path("courses/", views.courses, name="courses"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    
    # Авторизация и регистрация
    path("login/", auth_views.LoginView.as_view(template_name="core/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),
    path("register/", views.register, name="register"),

    # Восстановление пароля
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="core/password_reset.html"), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="core/password_reset_done.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="core/password_reset_confirm.html"), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name="core/password_reset_complete.html"), name="password_reset_complete"),

    # Настройки профиля
    path("profile/", views.profile, name="profile"),

    # Маршруты для курсов
    path("courses/", include("courses.urls")),  # Подключаем маршруты для курсов
]
