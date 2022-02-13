from django.core.management.base import BaseCommand
from student.models import Student

class Command(BaseCommand):
    help = 'Run seeding for student app.'

    def handle(self, *args, **options):
        Student.objects.bulk_create([
            Student(
                name = 'Zain Alwan Wima Irfani',
                major = 'Power Plant Engineering',
                email = 'zainalwan4@gmail.com'
            ),
            Student(
                name = 'John',
                major = 'Informatics Engineering',
                email = 'john@john.com'
            ),
            Student(
                name = 'Steve',
                major = 'Mechanical Engineering',
                email = 'steve@steve.com'
            ),
            Student(
                name = 'Park',
                major = 'Mechanical Engineering',
                email = 'park@park.com'
            ),
            Student(
                name = 'Doe',
                major = 'Electrical Engineering',
                email = 'doe@doe.com'
            ),
        ])

        print("Student table has been added for five records.")
