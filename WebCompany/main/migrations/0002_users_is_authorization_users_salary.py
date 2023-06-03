# Generated by Django 4.2.1 on 2023-05-25 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='is_authorization',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='users',
            name='salary',
            field=models.CharField(default='', max_length=250, verbose_name='Зарплата'),
        ),
    ]
