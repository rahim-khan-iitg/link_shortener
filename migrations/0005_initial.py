# Generated by Django 4.2.1 on 2023-06-24 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('link_shortener', '0004_delete_link_db'),
    ]

    operations = [
        migrations.CreateModel(
            name='link_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=1000)),
            ],
        ),
    ]
