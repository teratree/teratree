# Generated by Django 2.2.3 on 2019-07-28 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0005_remove_experiment_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experiment',
            old_name='experiment',
            new_name='method',
        ),
    ]
