# Generated by Django 4.0.2 on 2022-02-26 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_rename_case_id_case_has_weapon_case_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='description',
            old_name='weapon_id',
            new_name='weapon',
        ),
    ]
