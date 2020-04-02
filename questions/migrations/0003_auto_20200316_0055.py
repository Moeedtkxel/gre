# Generated by Django 2.2.2 on 2020-03-16 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20200316_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answersId', to='answers.Answers'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='custom_answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='custom_answersId', to='custom_answers.Custom_answers'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imageId', to='images.Images'),
        ),
    ]