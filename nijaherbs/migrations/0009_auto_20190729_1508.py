# Generated by Django 2.1 on 2019-07-29 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nijaherbs', '0008_auto_20190729_1506'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='herb',
            options={'ordering': ('created_on',)},
        ),
    ]
