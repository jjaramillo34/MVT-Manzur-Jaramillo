# Generated by Django 4.0.4 on 2022-05-18 20:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('family_members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=25),
            preserve_default=False,
        ),
    ]