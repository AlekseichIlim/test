from django.core.management import BaseCommand

from main.models import Student


class Command(BaseCommand):

    def handle(self, *args, **options):
        student_list = [
            {'last_name': 'Петров', 'first_name': 'Петя'},
            {'last_name': 'Иванов', 'first_name': 'Вася'},
            {'last_name': 'Сидоров', 'first_name': 'Илья'},
            {'last_name': 'Первый', 'first_name': 'Илюха'},
            {'last_name': 'Второй', 'first_name': 'Витек'},
            {'last_name': 'Третий', 'first_name': 'Женя'},
        ]

        stud_for_create = []
        for item in student_list:
            stud_for_create.append(
                Student(**item)
            )

        Student.objects.bulk_create(stud_for_create)