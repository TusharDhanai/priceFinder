# Generated by Django 3.2.13 on 2022-12-12 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('link', models.URLField(max_length=2000)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('features', models.CharField(max_length=1000, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.FilePathField(max_length=255)),
            ],
        ),
    ]
