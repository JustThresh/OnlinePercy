# Generated by Django 2.2.7 on 2019-11-12 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191112_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodel',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False, verbose_name='主键id'),
        ),
    ]
