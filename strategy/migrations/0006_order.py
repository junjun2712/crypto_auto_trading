# Generated by Django 2.0.5 on 2018-05-21 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('strategy', '0005_auto_20180520_1404'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('quantity', models.DecimalField(decimal_places=8, max_digits=14)),
                ('price', models.DecimalField(decimal_places=8, max_digits=14)),
                ('is_valid', models.BooleanField()),
                ('status', models.CharField(help_text='交易平台返回的状态', max_length=15)),
                ('message', models.CharField(max_length=255)),
                ('strategy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strategy.Strategy')),
            ],
        ),
    ]
