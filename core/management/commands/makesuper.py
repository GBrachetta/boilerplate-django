from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = (
        "Creates a superuser with the following details: "
        "username: admin, password: admin, email: admin@domain.com"
    )

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@domain.com", "admin")
            self.stdout.write(
                self.style.SUCCESS("Success: admin user has been created.")
            )
        else:
            self.stdout.write(
                self.style.ERROR("Error: admin user already exists.")
            )
