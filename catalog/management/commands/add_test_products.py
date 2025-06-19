from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Products, Category


class Command(BaseCommand):
    help = "Add test products to the database"

    def handle(self, *args, **kwargs):
        Products.objects.all().delete()
        Category.objects.all().delete()

        call_command("loaddata", "catalog.json")
        self.stdout.write(self.style.SUCCESS("Successfully loaded data from fixture"))
