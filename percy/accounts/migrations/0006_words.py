# Generated by Django 2.2.7 on 2019-11-13 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20191112_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(default='', verbose_name='广告提示语')),
            ],
            options={
                'verbose_name': '广告提示语',
                'verbose_name_plural': '广告提示语',
            },
        ),
    ]