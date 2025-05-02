# Файл: theater-scholl-app/courses/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Enrollment

@receiver(post_save, sender=Enrollment)
def send_enrollment_confirmation(sender, instance, created, **kwargs):
    """
    Отправляет email студенту после создания записи на курс.
    """
    if created:
        subject = f"Подтверждение записи на курс: {instance.course.title}"
        message = (
            f"Здравствуйте, {instance.student.username}!\n\n"
            f"Вы успешно записались на курс \"{instance.course.title}\".\n"
            f"Период курса: {instance.selected_start_date} - {instance.selected_end_date}\n\n"
            "Спасибо, что выбрали наш театр-школу!"
        )
        recipient_list = [instance.student.email]
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
