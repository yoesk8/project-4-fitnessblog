# Generated by Django 4.1.5 on 2023-02-17 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='country',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='county',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='postcode',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='street_address1',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='street_address2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='town_or_city',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
