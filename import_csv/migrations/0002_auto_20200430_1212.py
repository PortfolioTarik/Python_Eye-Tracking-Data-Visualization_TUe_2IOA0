# Generated by Django 3.0.5 on 2020-04-30 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('import_csv', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fixationdata',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='fixationdata',
            table='Fixation_data',
        ),
    ]