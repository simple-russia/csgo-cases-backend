# Generated by Django 4.0.2 on 2022-02-04 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_case_description_case_has_weapon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='language',
            field=models.CharField(choices=[('FR', 'Russin'), ('SO', 'English'), ('JR', 'Spanish'), ('SR', 'Portuguese'), ('GR', 'German')], max_length=2),
        ),
    ]
