# Файл: theater-scholl-app/courses/models.py
from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    TYPE_CHOICES = [
        ('individual', 'Персональное'),
        ('pair', 'Парное'),
    ]
    course_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    available = models.BooleanField(default=True)  # Новое поле

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    STATUS_CHOICES = [
        ('waiting', 'Ожидание'),
        ('confirmed', 'Подтверждено'),
        ('completed', 'Завершено'),
        ('declined', 'Отклонено'),
    ]
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # Используем атрибут класса Course, а не переменную course
    enrollment_type = models.CharField(max_length=20, choices=Course.TYPE_CHOICES)
    selected_start_date = models.DateField()
    selected_end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='waiting')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.course.title} - {self.student.username}"

class Portfolio(models.Model):
    # Используем стандартную модель User вместо кастомного профиля
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    image = models.ImageField(upload_to="portfolio/", blank=True, null=True, verbose_name="Фото")
    video_link = models.URLField(blank=True, null=True, verbose_name="Ссылка на видео")

    def __str__(self):
        return f"{self.user.username} - {self.title}"
    
class Review(models.Model):
    STATUS_CHOICES = [
        ('pending', 'На модерации'),
        ('approved', 'Одобрено'),
        ('rejected', 'Отклонено'),
    ]
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField(default=5)  # можно ограничить диапазон через валидаторы
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.student.username} for {self.course.title}"
