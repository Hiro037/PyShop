# Команда пока не работает
# from django.contrib.auth.models import Permission
# from django.core.management import BaseCommand
# from django.contrib.auth.models import Permission, Group
# from users.models import User
# from django.contrib.contenttypes.models import ContentType
# from products.models import Products
#
# class Command(BaseCommand):
#     help = 'Создает пользователя-модератора с нужными правами'
#
#     def handle(self, *args, **options):
#         email = 'moderator@example.com'
#         password = 'qwerty'
#         group_name = 'Модератор продуктов'
#
#         # Создание или получение пользователя
#         user, created = User.objects.get_or_create(email=email)
#         if created:
#             user.set_password(password)
#             user.is_active = True
#             user.save()
#             self.stdout.write(self.style.SUCCESS(f'Пользователь {email} создан.'))
#         else:
#             self.stdout.write(self.style.WARNING(f'Пользователь {email} уже существует.'))
#
#         # Получаем или создаем группу
#         group, _ = Group.objects.get_or_create(name=group_name)
#
#         # Получаем права
#         try:
#             ct = ContentType.objects.get_for_model(Product)
#             unpublish_perm = Permission.objects.get(codename='can_unpublish_product', content_type=ct)
#             delete_perm = Permission.objects.get(codename='delete_product', content_type=ct)
#         except Permission.DoesNotExist as e:
#             self.stderr.write(self.style.ERROR(f'Ошибка: {e}'))
#             return
#
#         # Добавляем права группе
#         group.permissions.add(unpublish_perm, delete_perm)
#
#         # Добавляем пользователя в группу
#         user.groups.add(group)
#
#         self.stdout.write(self.style.SUCCESS(f'Пользователь {email} добавлен в группу "{group_name}" с нужными правами.'))
