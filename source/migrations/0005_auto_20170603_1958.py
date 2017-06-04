# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 00:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0004_auto_20170603_1953'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currency',
            options={'verbose_name_plural': 'currencies'},
        ),
        migrations.AlterField(
            model_name='currency',
            name='currency',
            field=models.CharField(choices=[('GBP', 'GBP'), ('EUR', 'EUR'), ('AUD', 'AUD'), ('JPY', 'JPY'), ('CAD', 'CAD'), ('NOK', 'NOK'), ('CHF', 'CHF'), ('SEK', 'SEK'), ('MXN', 'MXN'), ('NZD', 'NZD'), ('INR', 'INR'), ('BRL', 'BRL'), ('DKK', 'DKK')], max_length=3),
        ),
    ]