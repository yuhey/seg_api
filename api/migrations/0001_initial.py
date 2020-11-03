# Generated by Django 3.1.3 on 2020-11-03 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Greeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('time', models.CharField(max_length=255, verbose_name='time')),
            ],
            options={
                'verbose_name': 'greeting',
                'verbose_name_plural': 'greeting',
            },
        ),
    ]
