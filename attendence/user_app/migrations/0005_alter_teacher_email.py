# Generated by Django 4.0.1 on 2022-04-04 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0004_alter_department_deptname_remove_teacher_department_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.CharField(max_length=255),
        ),
    ]