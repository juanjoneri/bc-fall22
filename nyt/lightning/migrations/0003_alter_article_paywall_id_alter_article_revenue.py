# Generated by Django 4.1.3 on 2022-11-27 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lightning', '0002_purchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='paywall_id',
            field=models.CharField(default='2AA6BgQGksioyzvwBTdwLP', max_length=200),
        ),
        migrations.AlterField(
            model_name='article',
            name='revenue',
            field=models.IntegerField(default=0),
        ),
    ]