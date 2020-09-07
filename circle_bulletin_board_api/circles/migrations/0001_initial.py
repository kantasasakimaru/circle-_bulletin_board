# Generated by Django 2.1 on 2020-09-07 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Circles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'circles',
                'managed': False,
            },
        ),
    ]