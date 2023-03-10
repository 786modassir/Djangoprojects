# Generated by Django 4.1.5 on 2023-01-31 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('Customer_Name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('Food_Name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Review_Name', models.CharField(max_length=50)),
                ('Rating', models.IntegerField()),
                ('Customer_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='play.customer')),
                ('Food_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='play.food')),
            ],
        ),
    ]
