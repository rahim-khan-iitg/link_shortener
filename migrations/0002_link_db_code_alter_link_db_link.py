# Generated by Django 4.2.1 on 2023-06-23 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link_shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link_db',
            name='code',
            field=models.TextField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='link_db',
            name='link',
            field=models.TextField(max_length=1000),
        ),
    ]
