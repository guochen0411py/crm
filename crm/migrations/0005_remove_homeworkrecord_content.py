# Generated by Django 2.1.5 on 2019-01-12 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_auto_20190112_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homeworkrecord',
            name='content',
        ),
    ]
