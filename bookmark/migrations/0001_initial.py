# Generated by Django 4.2.14 on 2024-07-10 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=100)),
                ('url', models.URLField(verbose_name='Site URL')),
            ],
        ),
    ]
