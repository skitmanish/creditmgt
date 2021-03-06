# Generated by Django 2.1.5 on 2020-08-12 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('image', models.ImageField(upload_to='images/')),
                ('number', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=70)),
                ('credits', models.IntegerField(default=500)),
            ],
        ),
    ]
