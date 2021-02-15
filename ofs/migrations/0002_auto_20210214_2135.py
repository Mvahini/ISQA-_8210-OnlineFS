# Generated by Django 3.1.6 on 2021-02-15 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ofs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appetizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appetizer_name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='account_number',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='bldgroom',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='role',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='updated_date',
        ),
    ]