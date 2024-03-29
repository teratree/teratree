# Generated by Django 2.2.3 on 2019-08-02 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('experiment', '0010_auto_20190802_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experiencecomment',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='experiencecomment',
            name='poster',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='parents',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='poster',
        ),
        migrations.RemoveField(
            model_name='experimentcomment',
            name='experiment',
        ),
        migrations.RemoveField(
            model_name='experimentcomment',
            name='poster',
        ),
        migrations.RemoveField(
            model_name='experimentrelatedexperience',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='experimentrelatedexperience',
            name='experiment',
        ),
        migrations.RenameField(
            model_name='experimentpagecomment',
            old_name='author',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='experimentpage',
            name='poster',
        ),
        migrations.RemoveField(
            model_name='experimentpagecomment',
            name='date',
        ),
        migrations.AddField(
            model_name='experimentpage',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='experiment_pages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='experimentpagecomment',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254),
        ),
        migrations.AddField(
            model_name='experimentpagecomment',
            name='posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='experimentpagecomment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='experiment_page_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Experience',
        ),
        migrations.DeleteModel(
            name='ExperienceComment',
        ),
        migrations.DeleteModel(
            name='Experiment',
        ),
        migrations.DeleteModel(
            name='ExperimentComment',
        ),
        migrations.DeleteModel(
            name='ExperimentRelatedExperience',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
