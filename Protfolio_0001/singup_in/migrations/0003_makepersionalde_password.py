# Generated by Django 4.2.7 on 2023-12-13 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singup_in', '0002_makepersionalde'),
    ]

    operations = [
        migrations.AddField(
            model_name='makepersionalde',
            name='password',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]