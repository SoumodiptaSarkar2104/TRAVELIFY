# Generated by Django 5.1.5 on 2025-02-10 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('DOB', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Contact', models.IntegerField()),
                ('Place', models.CharField(max_length=100)),
                ('Gender', models.CharField(max_length=100)),
                ('Country', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'userdata',
            },
        ),
    ]
