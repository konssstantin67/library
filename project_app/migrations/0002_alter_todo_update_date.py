# Generated by Django 4.1.5 on 2023-01-24 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='update_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
