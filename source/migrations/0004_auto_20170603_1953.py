# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 00:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0003_file_file_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=3)),
                ('conversion_rate', models.DecimalField(decimal_places=5, max_digits=6)),
                ('conversion_rate_date', models.DateField()),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'currencies',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateField()),
                ('revenue', models.DecimalField(decimal_places=2, max_digits=5)),
                ('revshare', models.DecimalField(decimal_places=2, max_digits=5)),
                ('gross_profit', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='source.Book')),
            ],
            options={
                'db_table': 'transactions',
            },
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='apple_commission',
            new_name='apple_reveshare',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='createspace_commission',
            new_name='createspace_reveshare',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='google_commission',
            new_name='google_reveshare',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='kindle_inclusive_commission',
            new_name='kindle_inclusive_reveshare',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='kindle_non_inclusive_commission',
            new_name='kindle_non_inclusive_reveshare',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='lightningsource_commission',
            new_name='lightningsource_reveshare',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='nook_commission',
            new_name='nook_reveshare',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='smashwords_commission',
            new_name='smashwords_reveshare',
        ),
        migrations.RenameField(
            model_name='contract',
            old_name='wholesale_commission',
            new_name='wholesale_reveshare',
        ),
    ]