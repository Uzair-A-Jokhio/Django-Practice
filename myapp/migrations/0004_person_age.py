# Generated by Django 5.0 on 2024-01-06 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_name_person_person_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]