# Generated by Django 4.0.2 on 2022-02-04 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_description_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='is_special',
            field=models.CharField(choices=[('0', 'Regular case'), ('1', 'Special case')], default='0', max_length=1),
        ),
    ]
