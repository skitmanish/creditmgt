# Generated by Django 2.1.5 on 2020-08-13 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=70)),
                ('tname', models.CharField(max_length=70)),
                ('amount', models.IntegerField(default=500)),
            ],
        ),
    ]
