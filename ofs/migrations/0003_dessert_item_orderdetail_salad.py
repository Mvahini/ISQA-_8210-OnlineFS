# Generated by Django 3.1.6 on 2021-02-15 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ofs', '0002_auto_20210214_2135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dessert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dessert_name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Salad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salad_name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('Customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ofs.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_item', models.CharField(max_length=50)),
                ('Appetizer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ofs.appetizer')),
                ('Dessert', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ofs.dessert')),
                ('Salad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ofs.salad')),
            ],
        ),
    ]