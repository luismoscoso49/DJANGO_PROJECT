# Generated by Django 4.1.1 on 2022-09-18 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team14App', '0008_alter_historia_signos_fecha'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historia_signos',
            old_name='id_history',
            new_name='id',
        ),
    ]
