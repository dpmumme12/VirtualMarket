# Generated by Django 3.2.7 on 2021-12-04 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VirMarket_CS', '0004_user_roles'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user_roles',
            options={'managed': False, 'permissions': [('User_Admin', 'Has access to the entire application'), ('Basic_Customer_User', 'Has basic access to the application')]},
        ),
    ]
