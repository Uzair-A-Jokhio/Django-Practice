# Generated by Django 5.0.1 on 2024-01-25 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MenuItemAPI', '0002_rename_invetory_listmenu_inventory'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ListMenu',
            new_name='MenuItem',
        ),
    ]
