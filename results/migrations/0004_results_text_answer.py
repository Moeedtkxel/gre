# Generated by Django 2.2.2 on 2020-04-24 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0003_marks'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='text_answer',
            field=models.CharField(max_length=255, null=True),
        ),
    ]