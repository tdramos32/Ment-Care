# Generated by Django 4.0.10 on 2023-04-10 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('user', models.CharField(max_length=100)),
                ('mood', models.IntegerField()),
            ],
        ),
    ]
