# Generated by Django 3.1.1 on 2021-02-03 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailmessage',
            name='subject',
            field=models.CharField(default='This is a title', max_length=150),
            preserve_default=False,
        ),
    ]
