# Generated by Django 2.2.5 on 2019-09-20 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190920_0914'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='registration',
            table='accounts_registration',
        ),
    ]
