# Generated by Django 3.1 on 2020-08-14 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200814_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mtadminuser',
            name='inventory_enabled',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='mtadminuser',
            name='inventory_role_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mtadminuser',
            name='user_lang',
            field=models.IntegerField(default=0),
        ),
    ]
