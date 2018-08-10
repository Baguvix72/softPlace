# Generated by Django 2.1 on 2018-08-10 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=300)),
                ('discription', models.TextField()),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('datePublic', models.DateTimeField(auto_now=True)),
                ('categorys', models.ManyToManyField(to='Post.Category')),
            ],
        ),
    ]
