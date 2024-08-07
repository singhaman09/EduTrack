# Generated by Django 4.2.13 on 2024-07-27 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_number', models.PositiveIntegerField()),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=100)),
                ('field_of_study', models.CharField(max_length=50)),
                ('gpa', models.FloatField()),
            ],
        ),
    ]
