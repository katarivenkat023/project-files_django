# Generated by Django 3.0.2 on 2020-10-11 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=50)),
                ('esalary', models.FloatField()),
                ('eaddress', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProxyEmployee1',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('proxyapp.employee',),
        ),
        migrations.CreateModel(
            name='ProxyEmployee2',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('proxyapp.employee',),
        ),
    ]
