# Generated by Django 4.2.7 on 2023-12-25 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userbankaccount',
            old_name='account_Type',
            new_name='Acctp',
        ),
    ]
