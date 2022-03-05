# Generated by Django 4.0.2 on 2022-02-26 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_remove_weapon_rarity_case_has_weapon_rarity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='case_has_weapon',
            old_name='case_id',
            new_name='case',
        ),
        migrations.RenameField(
            model_name='case_has_weapon',
            old_name='weapon_id',
            new_name='weapon',
        ),
        migrations.RenameField(
            model_name='weapon',
            old_name='collection_id',
            new_name='collection',
        ),
        migrations.RenameField(
            model_name='weapon',
            old_name='color_id',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='weapon',
            old_name='type_id',
            new_name='type',
        ),
    ]
