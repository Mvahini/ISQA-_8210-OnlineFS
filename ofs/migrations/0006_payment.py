# Generated by Django 3.1.6 on 2021-02-15 04:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ofs', '0005_auto_20210214_2233'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Payment', to='ofs.customer')),
            ],
        ),
    ]
