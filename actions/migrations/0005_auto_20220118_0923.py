# Generated by Django 3.1.7 on 2022-01-18 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0001_initial'),
        ('actions', '0004_action_action_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='action',
            name='entity',
        ),
        migrations.AddField(
            model_name='action',
            name='entity',
            field=models.ManyToManyField(blank=True, related_name='actions_action_entity', to='entity.Entity'),
        ),
    ]
