# Generated by Django 5.1.1 on 2025-02-16 08:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0005_remove_teacher_user_alter_teacher_department_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='department',
            field=models.CharField(choices=[('Computer Science', 'Computer Science'), ('Mathematics', 'Mathematics'), ('Physics', 'Physics')], default='Computer Science', max_length=50),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='teachers/'),
        ),
    ]
