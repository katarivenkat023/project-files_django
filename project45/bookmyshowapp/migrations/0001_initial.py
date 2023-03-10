# Generated by Django 3.0.2 on 2020-09-27 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moviename', models.CharField(max_length=50)),
                ('hero', models.CharField(max_length=50)),
                ('heroine', models.CharField(max_length=50)),
                ('releasedate', models.DateField()),
                ('rating', models.IntegerField()),
                ('director', models.CharField(max_length=50)),
                ('timing', models.TimeField()),
                ('language', models.CharField(max_length=50)),
            ],
        ),
    ]
