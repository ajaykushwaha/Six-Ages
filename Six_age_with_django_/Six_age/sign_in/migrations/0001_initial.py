# Generated by Django 2.0 on 2018-10-10 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=10)),
                ('Email', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'User_Details',
            },
        ),
    ]
