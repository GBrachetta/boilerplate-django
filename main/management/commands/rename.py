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
            "boilerplate/settings/common.py",
            "boilerplate/settings/development.py",
            "boilerplate/settings/production.py",
            "manage.py",
            ".gitignore",
        ]
        folder_to_rename = "boilerplate"

        for f in files_to_rename:
            with open(f, "r") as file:
                filedata = file.read()

            filedata = filedata.replace("boilerplate", new_project_name)

            with open(f, "w") as file:
                file.write(filedata)

        delete_main_from = "boilerplate/settings/common.py"

        with open(delete_main_from, "r") as main:
            main_delete = main.read()

        main_delete = main_delete.replace('    "main",', "")

        with open(delete_main_from, "w") as main:
            main.write(main_delete)

        os.rename(folder_to_rename, new_project_name)

        self.stdout.write(
            self.style.SUCCESS(
                "Project has been renamed to %s" % new_project_name
            )
        )
