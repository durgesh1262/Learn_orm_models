# Generated by Django 4.1.1 on 2022-09-27 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_roll_name_student_roll_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='marks',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
