from django.contrib.auth.models import User
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_admin_user(sender, **kwargs):
    """ Создание администратора при первом запуске приложения. """
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "375298608038@yandex.ru", "admin")
        print("Создан администратор: admin / admin")
