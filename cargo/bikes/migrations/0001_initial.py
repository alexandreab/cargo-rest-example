# Generated by Django 3.2.7 on 2021-09-12 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fleet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('unlocked', 'Unlocked'), ('locked', 'Locked')], max_length=15)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('fleet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bikes.fleet')),
            ],
        ),
    ]
