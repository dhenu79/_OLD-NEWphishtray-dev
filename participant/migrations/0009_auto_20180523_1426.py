# Generated by Django 2.0.5 on 2018-05-23 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0005_auto_20180523_1338'),
        ('participant', '0008_auto_20180523_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participantprofile',
            name='key',
        ),
        migrations.AddField(
            model_name='participantprofile',
            name='key',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='exercise.ExerciseKey'),
            preserve_default=False,
        ),
    ]