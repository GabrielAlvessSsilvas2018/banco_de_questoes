# Generated by Django 2.0.7 on 2018-10-18 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bancodequestoes', '0002_auto_20181018_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questao',
            name='answer',
            field=models.CharField(max_length=100, verbose_name='alternativa correta'),
        ),
    ]
