# Generated by Django 3.1.1 on 2020-10-30 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tags',
            options={'verbose_name_plural': 'Tags'},
        ),
        migrations.AddField(
            model_name='task',
            name='state',
            field=models.BooleanField(default=True, verbose_name='Estatus'),
        ),
    ]
