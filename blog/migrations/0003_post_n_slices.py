# Generated by Django 2.0.8 on 2018-11-02 03:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_n_pies'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='n_slices',
            field=models.PositiveSmallIntegerField(blank=True, help_text='How many slices should this pie be cut into?', null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='number of slices'),
        ),
    ]
