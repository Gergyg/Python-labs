# Generated by Django 4.2.1 on 2023-06-05 21:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parts', '0002_part_price'),
        ('customers', '0002_initial'),
        ('service_types', '0001_initial'),
        ('masters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('labour_cost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость работы')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masters.master')),
            ],
        ),
        migrations.CreateModel(
            name='RepairPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parts.part')),
                ('repair', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repairs.repair')),
            ],
        ),
        migrations.AddField(
            model_name='repair',
            name='parts',
            field=models.ManyToManyField(through='repairs.RepairPart', to='parts.part'),
        ),
        migrations.AddField(
            model_name='repair',
            name='service_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service_types.servicetype'),
        ),
    ]