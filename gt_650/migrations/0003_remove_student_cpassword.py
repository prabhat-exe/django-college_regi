# Generated by Django 5.0.3 on 2024-04-11 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gt_650', '0002_alter_student_cpassword_alter_student_fname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='cpassword',
        ),
    ]
