# Generated by Django 2.2.4 on 2019-09-24 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorialsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='approved_comment',
            field=models.BooleanField(default=False),
        ),
    ]
