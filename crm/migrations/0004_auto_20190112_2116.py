# Generated by Django 2.1.5 on 2019-01-12 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_homework_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeworkrecord',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='crm.Student', verbose_name='学生'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='homework',
            name='content',
            field=models.TextField(verbose_name='作业内容'),
        ),
        migrations.AlterField(
            model_name='homeworkrecord',
            name='status',
            field=models.IntegerField(choices=[(1, '待批阅'), (2, '已批阅')], default=1, verbose_name='状态'),
        ),
    ]
