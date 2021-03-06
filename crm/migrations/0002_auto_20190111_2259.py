# Generated by Django 2.1.5 on 2019-01-11 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classlist',
            name='tech_teachers',
            field=models.ManyToManyField(blank=True, limit_choices_to={'depart__title__in': ['教质部']}, related_name='teach_classes', to='crm.UserInfo', verbose_name='任课老师'),
        ),
    ]
