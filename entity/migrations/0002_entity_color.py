# Generated by Django 3.1.7 on 2022-03-24 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='color',
            field=models.CharField(default='#FFFFFF', max_length=10),
        ),
    ]
