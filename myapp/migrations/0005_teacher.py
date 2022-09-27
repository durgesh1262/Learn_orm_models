# Generated by Django 4.1.1 on 2022-09-27 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_student_marks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('emp_id', models.IntegerField()),
                ('salaty', models.IntegerField()),
                ('join_date', models.DateField()),
            ],
        ),
    ]
