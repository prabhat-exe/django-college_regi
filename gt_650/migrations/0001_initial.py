# Generated by Django 5.0.3 on 2024-04-11 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('fname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField()),
                ('password', models.CharField(max_length=30)),
                ('cpassword', models.CharField(max_length=30)),
            ],
        ),
    ]
