# Generated by Django 2.1 on 2019-03-25 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_yqn', '0017_auto_20190312_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xmlfeed',
            name='source',
            field=models.IntegerField(choices=[(1, 'Blog'), (2, 'Podcast'), (3, 'News')], help_text="The 'source' or category for this feed", verbose_name='Category'),
        ),
    ]
