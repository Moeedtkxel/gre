# Generated by Django 2.2.2 on 2020-04-11 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions_detail', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_time', models.IntegerField(choices=[(1, 'Normal TIme'), (2, '1.5x time'), (3, 'Double Time'), (4, 'Full time')], default=1)),
                ('time_left', models.FloatField(max_length=255)),
                ('test_id', models.IntegerField()),
                ('test_taker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='timerId', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_id', models.IntegerField(null=True)),
                ('answer', models.CharField(max_length=255, null=True)),
                ('custom_answer', models.CharField(max_length=255, null=True)),
                ('isActive', models.BooleanField(default=True)),
                ('question_detail', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answersId', to='questions_detail.Questions_detail')),
                ('test_taker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='testtakerId', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
