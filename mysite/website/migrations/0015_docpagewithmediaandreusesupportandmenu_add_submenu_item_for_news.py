# Generated by Django 3.0.10 on 2020-09-24 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_auto_20200924_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='docpagewithmediaandreusesupportandmenu',
            name='add_submenu_item_for_news',
            field=models.BooleanField(default=False),
        ),
    ]
