# Generated by Django 4.2.1 on 2023-06-04 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='orders',
            field=models.ManyToManyField(related_name='customers', to='orders.order'),
        ),
        migrations.AddField(
            model_name='customer',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customers.profile'),
        ),
    ]