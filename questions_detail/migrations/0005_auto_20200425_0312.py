# Generated by Django 2.2.2 on 2020-04-24 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions_detail', '0004_auto_20200425_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='options',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='questions_detail.Options'),
        ),
    ]
