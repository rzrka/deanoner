# Generated by Django 3.1.3 on 2020-12-05 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vk_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, verbose_name='имя')),
                ('profile_link', models.CharField(max_length=128, unique=True, verbose_name='ссылка на профиль')),
            ],
        ),
    ]
