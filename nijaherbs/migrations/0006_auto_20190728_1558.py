# Generated by Django 2.1 on 2019-07-28 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nijaherbs', '0005_auto_20190728_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='herb',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]