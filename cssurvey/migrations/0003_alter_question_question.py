# Generated by Django 4.0 on 2022-01-06 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cssurvey', '0002_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.TextField(),
        ),
    ]
