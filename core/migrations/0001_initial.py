# Generated by Django 4.1.7 on 2023-02-15 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Convict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('aliases', models.CharField(max_length=500)),
                ('gender', models.CharField(max_length=20)),
                ('place_of_birth', models.CharField(max_length=510)),
                ('date_of_birth', models.DateField()),
                ('education', models.CharField(max_length=100)),
                ('financial_background', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charges', models.CharField(max_length=100)),
                ('charges_code', models.CharField(max_length=200)),
                ('known_accomplices', models.CharField(max_length=100)),
                ('fir_date', models.DateField()),
                ('conviction_date', models.DateField()),
                ('comments', models.TextField(max_length=300)),
                ('sentencer', models.CharField(max_length=100)),
                ('sentence', models.CharField(max_length=100)),
                ('convict', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.convict')),
            ],
        ),
    ]
