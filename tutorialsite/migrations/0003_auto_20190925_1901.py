# Generated by Django 2.2.4 on 2019-09-25 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorialsite', '0002_comment_approved_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='link',
            new_name='text',
        ),
    ]