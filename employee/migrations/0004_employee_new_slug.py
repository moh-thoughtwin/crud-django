# Generated by Django 4.1.1 on 2022-09-15 05:30

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_employee_employee_ename_361546_idx'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='new_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='ename', unique=True),
        ),
    ]
