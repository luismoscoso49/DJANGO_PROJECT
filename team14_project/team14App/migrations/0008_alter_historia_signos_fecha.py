# Generated by Django 4.1.1 on 2022-09-18 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team14App', '0007_alter_historia_signos_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historia_signos',
            name='fecha',
            field=models.CharField(max_length=50),
        ),
    ]
