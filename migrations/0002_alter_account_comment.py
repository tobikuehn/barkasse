# Generated by Django 3.2.7 on 2021-09-30 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barkasse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='comment',
            field=models.TextField(null=True),
        ),
    ]
