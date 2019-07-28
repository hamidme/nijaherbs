# Generated by Django 2.1 on 2019-07-26 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a herb category (e.g. Medicinal)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Herb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='herb-images/')),
                ('summary', models.TextField(help_text='Enter a brief description of the herb', max_length=1000)),
                ('localName', models.CharField(max_length=200)),
                ('englishName', models.CharField(max_length=200)),
                ('botanicalName', models.CharField(max_length=200)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nijaherbs.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a region (e.g. Yoruba)', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='herb',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nijaherbs.Region'),
        ),
    ]