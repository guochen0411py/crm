# Generated by Django 2.1.5 on 2019-01-12 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_remove_homeworkrecord_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeworkrecord',
            name='content',
            field=models.FileField(default=1, upload_to='student_work/', verbose_name='作业内容'),
            preserve_default=False,
        ),
    ]
