# Generated by Django 4.2.7 on 2023-12-04 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cheakTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ids', models.IntegerField()),
                ('name', models.CharField(max_length=25)),
                ('dep', models.CharField(max_length=3)),
                ('code', models.IntegerField()),
            ],
        ),
    ]
