# Generated by Django 3.2.7 on 2021-09-30 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255)),
                ('desc', models.TextField(max_length=1000)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('image', models.ImageField(upload_to='Images/')),
            ],
        ),
    ]