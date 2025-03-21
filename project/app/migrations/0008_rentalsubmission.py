# Generated by Django 5.1.5 on 2025-03-18 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentalSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField()),
                ('license', models.CharField(max_length=10)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('persons', models.IntegerField()),
                ('driver_needed', models.CharField(max_length=10)),
            ],
        ),
    ]
