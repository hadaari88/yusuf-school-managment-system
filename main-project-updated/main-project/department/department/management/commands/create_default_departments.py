# department/management/commands/create_default_departments.py
from django.core.management.base import BaseCommand
from department.models import Department

class Command(BaseCommand):
    help = 'Creates default departments if they do not exist.'

    def handle(self, *args, **options):
        default_departments = [
            # Academic Departments
            {'name': 'Computer Science', 'code': 'CS', 'category': 'academic', 'description': 'Department of Computer Science'},
            {'name': 'Mathematics', 'code': 'MATH', 'category': 'academic', 'description': 'Department of Mathematics'},
            {'name': 'Physics', 'code': 'PHYS', 'category': 'academic', 'description': 'Department of Physics'},
            # Arts & Creative Departments
            {'name': 'Visual Arts', 'code': 'ARTS', 'category': 'arts', 'description': 'Department of Visual Arts'},
            {'name': 'Performing Arts', 'code': 'PERF', 'category': 'arts', 'description': 'Department of Performing Arts'},
            # Technical & Vocational Departments
            {'name': 'Mechanical Engineering', 'code': 'MECH', 'category': 'technical', 'description': 'Department of Mechanical Engineering'},
            {'name': 'Electrical Engineering', 'code': 'ELEC', 'category': 'technical', 'description': 'Department of Electrical Engineering'},
            # Sports & Physical Education
            {'name': 'Physical Education', 'code': 'PE', 'category': 'sports', 'description': 'Department of Sports and Physical Education'},
            # Administrative Departments
            {'name': 'Administrative Services', 'code': 'ADMIN', 'category': 'administrative', 'description': 'Department of Administrative Services'},
            # Add additional departments as needed.
        ]

        for dept in default_departments:
            department, created = Department.objects.get_or_create(
                name=dept['name'],
                defaults={
                    'code': dept.get('code'),
                    'category': dept.get('category'),
                    'description': dept.get('description')
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created department: {dept['name']}"))
            else:
                self.stdout.write(f"Department already exists: {dept['name']}")
