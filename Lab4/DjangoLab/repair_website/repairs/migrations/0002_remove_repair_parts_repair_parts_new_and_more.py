# Generated by Django 4.2.1 on 2023-06-05 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0002_part_price'),
        ('repairs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repair',
            name='parts',
        ),
        migrations.AddField(
            model_name='repair',
            name='parts_new',
            field=models.ManyToManyField(to='parts.part'),
        ),
        migrations.DeleteModel(
            name='RepairPart',
        ),
    ]