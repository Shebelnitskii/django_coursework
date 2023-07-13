from django.core.management import BaseCommand
from django.contrib.auth.management.commands.createsuperuser import Command as CreateSuperuserCommand
from users.models import User


### Создание администратора
class Command(CreateSuperuserCommand):
    def handle(self, *args, **options):
        user = User.objects.create_superuser(
            email='admin@test.com',
            password='123456789',
            is_staff=True,
            is_active=True,
        )
        user.save()


### Создание модератора
class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='moderator@test.com',
            is_staff=True,
            is_active=True,
        )
        user.set_password('123456789')
        user.save()
