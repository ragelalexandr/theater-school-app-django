# Файл: theater-scholl-app/core/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Администратор'),
        ('instructor', 'Преподаватель'),
        ('student', 'Студент'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='core_user_groups',  # Изменяем related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='core_user_permissions',  # Изменяем related_name
        blank=True
    )

class Review(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    text = models.TextField()
    approved = models.BooleanField(default=False)  # Поле для модерации

class TheatricalPerformance(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()

class Instructor(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ФИО", default="Без имени")
    name = models.CharField(max_length=255)    
    specialization = models.CharField(max_length=255, verbose_name="Специализация")
    password = models.CharField(max_length=255, verbose_name="Пароль")

class Course(models.Model):
    title = models.CharField(max_length=255)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, default=1)  # Укажи ID существующего преподавателя
    schedule = models.TextField()

class Student(models.Model):
    name = models.CharField(max_length=255)
    profile_data = models.TextField()

class UserProfile(AbstractUser):
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True, verbose_name="Фото профиля")
    contact_info = models.CharField(max_length=255, blank=True, null=True, verbose_name="Контактная информация")  # ✅ Убедись, что это поле существует

    groups = models.ManyToManyField(
        "auth.Group", related_name="userprofile_groups", blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission", related_name="userprofile_permissions", blank=True
    )

    def __str__(self):
        return self.username

