# Generated by Django 4.0 on 2022-01-06 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0002_alter_task_date_of_completion'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='detailed_description',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='Детальное Описание'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(max_length=200, verbose_name='Описание'),
        ),
    ]
