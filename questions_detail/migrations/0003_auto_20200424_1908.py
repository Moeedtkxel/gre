# Generated by Django 2.2.2 on 2020-04-24 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions_detail', '0002_auto_20200424_1634'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='questions',
            table='questions',
        ),
        migrations.AlterModelTable(
            name='questions_detail',
            table='question_details',
        ),
    ]
