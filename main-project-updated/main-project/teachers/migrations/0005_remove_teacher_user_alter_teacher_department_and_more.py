# Generated by Django 5.1.5 on 2025-02-15 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("teachers", "0004_remove_teacher_date_joined_remove_teacher_email_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="teacher",
            name="user",
        ),
        migrations.AlterField(
            model_name="teacher",
            name="department",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="first_name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="last_name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="profile_image",
            field=models.ImageField(
                blank=True, null=True, upload_to="teacher_profiles/"
            ),
        ),
    ]
