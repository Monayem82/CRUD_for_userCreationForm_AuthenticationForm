# Generated by Django 4.2.7 on 2023-12-12 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singup_in', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='makePersionalDe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('department', models.CharField(max_length=3)),
                ('dep_code', models.IntegerField()),
            ],
        ),
    ]
