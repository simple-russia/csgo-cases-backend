# Generated by Django 4.0.2 on 2022-02-04 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_case_is_special'),
    ]

    operations = [
        migrations.AddField(
            model_name='weapon',
            name='statrak',
            field=models.CharField(choices=[('0', 'Can be stattrak'), ('1', 'Cannot be statrak')], default='0', max_length=1),
        ),
    ]
