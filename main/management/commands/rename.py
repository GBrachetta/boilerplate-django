import os

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Renames a Django project"

    def add_arguments(self, parser):
        parser.add_argument(
            "new_project_name", type=str, help="The new Django project name"
        )

    def handle(self, *args, **kwargs):
        new_project_name = kwargs["new_project_name"]
        files_to_rename = [
            "boilerplate/wsgi.py",
            "boilerplate/asgi.py",
            "boilerplate/settings/components/common.py",
            "boilerplate/settings/environments/development.py",
            "boilerplate/settings/environments/production.py",
            "manage.py",
            ".gitignore"
        ]
        folder_to_rename = "boilerplate"

        for f in files_to_rename:
            with open(f, "r") as file:
                filedata = file.read()

            filedata = filedata.replace("boilerplate", new_project_name)

            with open(f, "w") as file:
                file.write(filedata)

        os.rename(folder_to_rename, new_project_name)

        self.stdout.write(
            self.style.SUCCESS(
                "Project has been renamed to %s" % new_project_name
            )
        )