# Generated by Django 3.1.2 on 2020-12-04 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opros', '0003_auto_20201204_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Дата публикации'),
        ),
    ]
