# Generated by Django 2.1 on 2018-08-11 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0003_auto_20180811_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dateCreation',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='datePublic',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
