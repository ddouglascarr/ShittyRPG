# Generated by Django 2.0.10 on 2019-02-19 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('sell_value', models.IntegerField()),
                ('buy_value', models.IntegerField()),
            ],
        ),
    ]
